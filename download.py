import configparser
from imbox import Imbox
# 读取配置文件
config = configparser.ConfigParser()
config.read("data/config.cfg", encoding="utf-8")

# 获取用户名和密码
username = config.get("mail", "username")
password = config.get("mail", "password")
imap = config.get("mail", "imap")


# 连接到IMAP服务器
with Imbox(imap, username=username, password=password) as mailbox:
    # 获取所有文件夹
    status , folders = mailbox.folders()
    data = {}
    # 获取每个邮件夹的邮件
    for folder in folders:
        #将二进制转为字符串
        folder = folder.decode()
        #对folder 进行转义
        folder = folder.split('"')[-2]
        #设计一个字典，用于存储邮件夹的邮件头
        data[folder] = []
        #获取邮件夹的邮件
        try:
            for uid , msg in mailbox.messages(folder=folder):
                data[folder].append(msg.subject)
        except Exception as e:
            print(f"Error occurred while fetching messages from folder {folder}: {e}")
            continue

#保存邮件头
with open("data/subject.txt", "w", encoding="utf-8") as f:
    f.write(str(data))

