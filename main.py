#coding=utf-8

import os
import logging
from common.log.mylogging import mylogger
import traceback
import wxpy
from chatbot.AppMethods import *
from sys import argv


# 日志打印开关
IS_LOGGER = True
# IS_LOGGER = False

work_dir = os.path.abspath(os.path.dirname(__file__.split('?')[0]))


def init_logging():
    try:
        if IS_LOGGER:
            mylogger.addLogFilePath(os.path.join(work_dir, 'logs'))
    except Exception as e:
        logging.error(traceback.format_exc())

init_logging()
logging.info("hello 鏡ちゃん")

logging.info("the script is called: %s", argv[0])
if len(argv) > 1:
    logging.info("the first variable is: %s", argv[1:])
    nickname = argv[1]

# 初始化bot
login_pkl, puid_pkl = get_pkls_path(nickname, work_dir)
bot = wxpy.Bot(login_pkl)
bot.enable_puid(path=puid_pkl)


# 初始化图灵机器人 (API key 申请: http://tuling123.com)，这个KEY是我自己的
tuling = wxpy.Tuling(api_key='2913bf7a0ff24d998c2149f6a9bc0dc7')


# 自动回复所有好友（非群）的消息
@bot.register(bot.friends(update=True))
def reply_friends(msg):
    tuling.do_reply(msg)

# 开始运行
wxpy.embed()


