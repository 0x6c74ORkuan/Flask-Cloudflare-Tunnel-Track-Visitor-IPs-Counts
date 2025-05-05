#导入flask
from flask import Flask, request
#自动初始化不存在的键
from collections import defaultdict

#创建一个flask应用对象，__name__ 表示当前模块名
应用 = Flask(__name__)

#创建一个字典，记录每个IP的访问次数（默认值为 0）
访问记录 = defaultdict(int)

#定义网站首页的路由
@应用.route("/")
def 首页():
    #获取访问者IP 如果通过Cloudflare访问，用CF-Connecting-IP；否则用本地IP
    客户端IP = request.headers.get("CF-Connecting-IP") or request.remote_addr

    访问记录[客户端IP] += 1

    #输出
    print(f"IP: {客户端IP}, 访问次数: {访问记录[客户端IP]}")

    #给访问者输出
    return f"IP：{客户端IP}  访问次数:{访问记录[客户端IP]}"

if __name__ == "__main__":
    应用.run(host="0.0.0.0", port=5000)
