import psutil
import requests
import datetime
import subprocess

# 서버 IP 주소 및 Slack Webhook URL 설정
server_ip = 'NAT IP'
# Slack API 토큰
slack_token = '슬랙토큰'
# Slack 채널 ID
slack_channel = '채널주소'
slack_webhook_url = "웹훅주소"

# 서버별 서비스 목록
services = [
        'cron',
        'dbus',
        'nginx',
        'apache2',
        'named'
]


def check_service_status(service_name):
    """서비스 상태 체크 함수"""
    result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE)
    if result.stdout.decode('utf-8').strip() != 'active':
        return False  # 서비스가 비활성 상태
    return True  # 서비스 활성 상태


def send_slack_notification(service_name):
    """Slack으로 알림 메시지 전송 함수"""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = {
            "text" : f"서버 IP 주소: {server_ip}, 문제가 발생한 서비스명: {service_name}, 문제 발생 확인 시간: {timestamp}"
    }
    response = requests.post(slack_webhook_url, json=message)
    if response.status_code != 200:
        print(f"Slack notification failed. Status code: {response.status_code}, response: {response.text}")

# 각 서비스 상태 체크 및 문제가 있는 경우 Slack에 알림
for service in services:
    if not check_service_status(service):
        send_slack_notification(service)