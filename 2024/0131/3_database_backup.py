import os
import time
import datetime
import subprocess
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import mysql.connector

# MySQL 연결 설정
mysql_config = {
    'host': '%',
    'user': 'db 아이디',
    'password': 'db 비밀번호',
    'database': '데이터베이스 이름'
}

# Slack 연결 설정
slack_token = '토큰'
channel_id = '채널ID'
client = WebClient(token=slack_token)

# 백업 파일 이름 설정
backup_file = f"backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.sql"

try:
    # MySQL 백업 실행
    dump_cmd = f"mysqldump -h {mysql_config['host']} -u {mysql_config['user']} -p{mysql_config['password']} {mysql_config['database']} > {backup_file}"
    subprocess.run(dump_cmd, shell=True, check=True)

    # 백업 파일 압축
    compressed_backup_file = f"{backup_file}.gz"
    compress_cmd = f"gzip {backup_file}"
    subprocess.run(compress_cmd, shell=True, check=True)

    # 백업 파일 크기 계산
    backup_size = os.path.getsize(compressed_backup_file)

    # Slack으로 결과 전송
    message = f"백업 파일: {compressed_backup_file}\n데이터베이스: {mysql_config['database']}\n백업 용량: {backup_size} bytes"
    client.chat_postMessage(channel=channel_id, text=message)

except (subprocess.CalledProcessError, FileNotFoundError, SlackApiError) as e:
    # 실패 시 예외 처리
    error_message = f"백업 실패: {str(e)}"
    client.chat_postMessage(channel=channel_id, text=error_message)