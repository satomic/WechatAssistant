# coding=utf-8
from Environment import Environment
import os
import logging
import wxpy
from chatbot.AppMethods import *
from sys import argv
import sys
from chatbot.MasterMsgHandler import MasterMsgHandler

# main方法调用则传入真实参数
work_dir = os.path.dirname(argv[0])
environment = Environment(work_dir=work_dir)

# logging.info("the script is called: %s", argv[0])
nickname = "default"
if len(argv) > 1:
    '''
    nickname
    -v
    -h
    '''
    argv_1 = argv[1]
    if argv_1 in ["-v","-V","-version","--version"]:
        print("version: %s" % environment.version)
        sys.exit(0)
    if argv_1 in ["-h","-H","-help","--help"]:
        print(\
'''
double click the exe, with nickname: default
nickname: start with nickname
-v version
-h help
''')
        sys.exit(0)
    nickname = argv[1]



# 初始化bot
login_pkl, puid_pkl = get_pkls_path(nickname, environment.work_dir)
bot = wxpy.Bot(login_pkl)
bot.enable_puid(path=puid_pkl)

# 在 Web 微信中把自己加为好友
# bot.self.add()
# bot.self.accept()

# 发送消息给自己
# bot.self.send('能收到吗？')

# master消息处理
# master = bot.friends().search("master")[0]
master_msg_handler = MasterMsgHandler(bot, [], environment.work_dir)

# 自动回复所有好友（非群）的消息
# 初始化图灵机器人 (API key 申请: http://tuling123.com)，这个KEY是我自己的
tuling = wxpy.Tuling(api_key='2913bf7a0ff24d998c2149f6a9bc0dc7')

# 这里的except_self启动之后，对群里面的自己的消息也是生效的，我简直无语了。。。
@bot.register(bot.friends(update=True),except_self=False)
def reply_friends(msg):
    # logging.info("%s -> %s" % (msg.sender, msg.text))
    if msg.sender in master_msg_handler.masters:
        logging.info("self msg: %s" % msg.text)
        master_msg_handler.handle(msg.text)
        return

    # tuling.do_reply(msg)

# @bot.register(bot.groups())
# def reply_groups(msg):
#     print(msg)
#     print(msg.sender)
#     print(master_msg_handler.masters)
#     if msg.sender in master_msg_handler.masters:
#         logging.info("%s -> %s" % (msg.sender, msg.text))
#         logging.info("self msg: %s" % msg.text)
        # master_msg_handler.handle(msg.text, msg.chat)


# 开始运行
wxpy.embed()


