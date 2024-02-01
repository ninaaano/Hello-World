import argparse
import subprocess
import socket
from datetime import datetime
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

#xoxo토큰

def check_service_status(service_name):
    try:
        status = subprocess.check_output(["systemctl", "is-active", service_name]).decode().strip()
        return f"{service_name} - {status}"
    except subprocess.CalledProcessError as e:
        if "inactive" in e.output.decode():
            return f"{service_name} - inactive"
        else:
            return f"{service_name} - Unknown"


def get_system_ip():
    return socket.gethostbyname(socket.gethostname())


def main(token, channel, services):
    prev_statuses = {service: None for service in services}

    client = WebClient(token=token)

    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message = f"Timestamp: {current_time}\nIP Address: {get_system_ip()}\n\n"
        temp = message

        for service in services:
            current_status = check_service_status(service)
            if current_status != prev_statuses[service]:
                message += f"{current_status}\n"
                prev_statuses[service] = current_status
        if message != temp:
            try:
                # Send message to Slack
                response = client.chat_postMessage(
                    channel=channel,
                    text=message,
                )
                print("Message sent to Slack successfully")
            except SlackApiError as e:
                print(f"Failed to send message to Slack: {e.response['error']}")

        time.sleep(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor system services and send status updates to Slack. Run in the background by adding '&' at the end of the command.")

    parser.add_argument("--token", required=True, help="Slack API token")
    parser.add_argument("--channel", required=True, help="Slack channel name or ID")
    parser.add_argument("--services", required=True, help="Services to monitor (comma-separated)")

    args = parser.parse_args()

    services = [service.strip() for service in args.services.split(",")]
    main(args.token, args.channel, services)
