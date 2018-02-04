# coding=utf-8
import os
import logging
from common.log.mylogging import mylogger
import traceback


class Environment(object):

    def __init__(self,is_logger=True,logs_dir="logs"):

        self.version = '0.0.4'
        self.update_time = '2018.02.04'

        # 日志打印开关
        self.is_logger = is_logger

        # 基础根目录
        self.work_dir = os.path.abspath(os.path.dirname(__file__.split('?')[0]))

        # 日志目录
        self.logs_dir = os.path.join(self.work_dir,logs_dir)

        try:
            if self.is_logger:
                mylogger.addLogFilePath(os.path.join(self.work_dir, self.logs_dir))
        except Exception as e:
            logging.error(traceback.format_exc())

        logging.info("hello 鏡ちゃん")

environment = Environment()



