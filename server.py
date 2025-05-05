from flask import Flask, request
from collections import defaultdict

应用 = Flask(__name__)
访问记录 = defaultdict(int)

@应用.route("/")
def 首页():
    客户端IP = request.headers.get("CF-Connecting-IP") or request.remote_addr
    访问记录[客户端IP] += 1
    print(f"访问者 IP: {客户端IP}, 访问次数: {访问记录[客户端IP]}")
    return f"IP{客户端IP}  访问次数:{访问记录[客户端IP]}"

if __name__ == "__main__":
    应用.run(host="0.0.0.0", port=5000)
