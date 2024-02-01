# 데이터베이스 백업 스크립트

### 사용 방법
    Monitor system services and send status updates to Slack. Run in the background by adding '&' at the end of the command.

    ex) python3 service-check.py --token api토큰 --channel "#채널명" --service 서비스명1,서비스명2

- 마지막에 &를 붙이면 백그라운드에서 실행 가능
  
![image](https://github.com/ninaaano/PythonHome/assets/95615105/a7fa04fe-ab32-46af-818e-7dc85d31287f)



- API 토큰은 워크 스페이스에서 만든다
  
![image](https://github.com/ninaaano/PythonHome/assets/95615105/7e2c2f07-133c-47d8-a915-76b31322b40b)


options:
  -h, --help           show this help message and exit
  --token TOKEN        Slack API token
  --channel CHANNEL    Slack channel name or ID
  --services SERVICES  Services to monitor (comma-separated)
    
change service status freely
    sudo systemctl stop named
    sudo systemctl start apache2

kill %1 when done

![image](https://github.com/ninaaano/PythonHome/assets/95615105/88c34835-676d-446f-8c5e-cc4339074f5d)

### 사용

![image](https://github.com/ninaaano/PythonHome/assets/95615105/8c2fca04-be3b-4d58-8c80-7dcf96cf3b26)

