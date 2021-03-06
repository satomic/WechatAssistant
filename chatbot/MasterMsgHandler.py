# coding=utf-8

from Environment import environment
import os
import logging
import traceback
from common.utils.CmdUtil import CmdUtil

class MasterMsgHandler(object):

    def __init__(self, bot, masters, work_dir):
        self.work_dir = work_dir
        self.scripts_dir = os.path.join(work_dir,"scripts")
        self.bot = bot

        if not isinstance(masters,list):
            masters = [masters]
        self.masters = masters
        if self.bot.self not in self.masters:
            self.masters.append(self.bot.self)
        logging.info("masters: %s" % self.masters)

    def handle(self,cmd, receiver=None):
        if self.basic_cmds(cmd, receiver):
            return
        try:
            self.pro_cmds(cmd, receiver)
        except Exception as e:
            logging.error(traceback.format_exc())

    def basic_cmds(self, cmd, receiver=None):
        if cmd == "截屏":
            logging.info("开始截屏")
            img_save_path = os.path.join(self.work_dir,"temp.jpg")
            if CmdUtil.print_screen(img_save_path):
                logging.info("截屏成功: %s" % img_save_path)
                if receiver is None:
                    for master in self.masters:
                        master.send_image(img_save_path)
                else:
                    receiver.send_image(img_save_path)
                logging.info("截屏已发送")
            return True
        return False

    def pro_cmds(self,cmd,receiver):
        pass