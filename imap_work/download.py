import configparser
from imap_tools import MailBox
from bs4 import BeautifulSoup

# 读取配置文件
config = configparser.ConfigParser()
config.read("config.cfg")

# 获取用户名和密码
username = config.get("mail", "username")
password = config.get("mail", "password")
imap = config.get("mail", "imap")

# 连接IMAP服务器
with MailBox(imap).login(username, password) as mailbox:
    # 遍历邮件
    for msg in mailbox.fetch():
        # 获取邮件正文
        if msg.text:
            body = msg.text
        elif msg.html:
            soup = BeautifulSoup(msg.html, "html.parser")
            body = soup.get_text()
        else:
            continue

        # 提取最后一次回复内容
        soup = BeautifulSoup(body, "html.parser")
        last_div = soup.find_all("div")[-1]
        text_content = last_div.get_text()
        print(text_content)
