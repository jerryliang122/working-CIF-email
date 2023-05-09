import os
import shutil

# 初始化查看data目录中是否有config.cfg文件
if not os.path.exists("data/config.cfg"):
    # 复制init_config.cfg文件到data目录中
    shutil.copy("init_config.cfg", "data/config.cfg")
    # 初始化结束退出程序
    print("初始化完成，请修改data/config.cfg文件中的配置信息")
    exit()

# 准备读取邮件的文件夹
import imap_work.folder as folder

folders = folder.main()
