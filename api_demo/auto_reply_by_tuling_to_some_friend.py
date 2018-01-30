#coding=utf-8

from wxpy import *

# 默认cache_path参数为False，如果为True，会保存当前登录信息到pkl文件，下次不用扫码。
# bot = Bot(cache_path=True)
bot = Bot()

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
# 打开则每个人有全局唯一，且保持不变的puid
bot.enable_puid(path='wxpy_puid.pkl')

# 检索一个朋友
# founds = bot.friends().search('镜子')

# 确保搜索结果是唯一的，并取出唯一结果
# friend = ensure_one(founds)

# 初始化图灵机器人 (API key 申请: http://tuling123.com)，这个KEY是我自己的
tuling = Tuling(api_key='2913bf7a0ff24d998c2149f6a9bc0dc7')


# 自动回复所有好友（非群）的消息
@bot.register(bot.friends(update=True))
def reply_friends(msg):
    tuling.do_reply(msg)

# 开始运行
embed()
