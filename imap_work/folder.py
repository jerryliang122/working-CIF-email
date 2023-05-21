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

def folder_list():
    # 连接到IMAP服务器
    with Imbox(imap, username=username, password=password) as mailbox:
        # 获取所有文件夹
        status , folders = mailbox.folders()
        # 打印所有文件夹
        for folder in folders:
            print(folder)
        return folders  
