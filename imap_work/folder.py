import configparser
import datetime
from imbox import Imbox

# 读取配置文件
config = configparser.ConfigParser()
config.read("data/config.cfg", encoding="utf-8")
# 获取用户名和密码
username = config.get("mail", "username")
password = config.get("mail", "password")
imap = config.get("mail", "imap")


def main():
    with Imbox(imap, username, password, ssl=True) as mailbox:
        # 获取文件夹
        folders = mailbox.folders()
        print(folders)
