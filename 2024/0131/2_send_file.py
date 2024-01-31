import subprocess
import requests
import csv
import json
import yaml
from ping3 import ping, verbose_ping
from datetime import datetime
import time
# 슬랙 웹훅 URL 설정
SLACK_WEBHOOK_URL = '웹훅주소'

# 결과 파일 경로 설정
CSV_FILE_PATH = 'network_stats.csv'
JSON_FILE_PATH = 'network_stats.json'
YAML_FILE_PATH = 'network_stats.yaml'
slack_access_token = '슬랙 토큰'

# 관리 대상 서버 IP 주소 설정
TARGET_SERVER_IP = 'google.com'
def check_network_status():
    try:
        # ping 명령 실행
        result = ping(TARGET_SERVER_IP, unit='ms', size=40, timeout=2)  # 2초 동안 대기 후 응답 확인
        # 결과를 파일에 저장
        save_to_csv(result)
        save_to_json(result)
        save_to_yaml(result)
        return result
    except Exception as e:
        return f"Error checking network status: {str(e)}"
def save_to_csv(data):
    with open(CSV_FILE_PATH, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), data])
def save_to_json(data):
    with open(JSON_FILE_PATH, 'a') as json_file:
        json.dump({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data': data
        }, json_file, indent=2)
def save_to_yaml(data):
    with open(YAML_FILE_PATH, 'a') as yaml_file:
        yaml.dump({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data': data
        }, yaml_file, default_flow_style=False)
def upload_files_to_slack():
    # CSV 파일을 슬랙에 업로드
    upload_file_to_slack(CSV_FILE_PATH, 'text/csv')
    # JSON 파일을 슬랙에 업로드
    upload_file_to_slack(JSON_FILE_PATH, 'application/json')
    # YAML 파일을 슬랙에 업로드
    upload_file_to_slack(YAML_FILE_PATH, 'application/x-yaml')
def upload_file_to_slack(file_path, file_type):
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file, file_type)}
            payload = {
                'initial_comment': f'Network Status Report - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            }
            requests.post(SLACK_WEBHOOK_URL, params=payload, files=files)
    except Exception as e:
        print(f"Error uploading file to Slack: {str(e)}")
def send_slack_notification(message):
    payload = {
        'text': message
    }
    requests.post(SLACK_WEBHOOK_URL, json=payload)
def send_file():
    url = "https://slack.com/api/files.upload"
    headers = {
        "Authorization": "Bearer " + slack_access_token,
        # "Content-Type": "multipart/form-data"
    }
    data = {
        # "token": slack_access_token,
        "channels": "C06G6U66T0B",
        "filename": "test.csv"
    }
    files = {
        'file': ('network_stats.csv', open('network_stats.csv', 'rb'), 'text/csv')
    }
    response = requests.post(url, headers=headers, data=data, files=files)
    print('HTTP Status Code:', response.status_code)
    print('Response:', response.text)
if __name__ == '__main__':
    # 주기적으로 실행되도록 루프 설정 (예: 1시간마다)
    for _ in range(2):
        network_status = check_network_status()
        # 슬랙으로 알림 전송
        send_slack_notification(f"Network Status for {TARGET_SERVER_IP}:\n{network_status}")
        # 슬랙으로 업로드
        send_file()
        upload_files_to_slack()
        # 1시간 대기 (3600초)
        time.sleep(3)