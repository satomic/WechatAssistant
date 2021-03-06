﻿# coding=utf-8
import os
import logging
from common.log.mylogging import mylogger
import traceback


class Environment(object):

    def __init__(self, work_dir=None, is_logger=True, logs_dir="logs"):

        self.version = '0.0.5'
        self.update_time = '2018.02.06'

        # 日志打印开关
        self.is_logger = is_logger

        # 基础根目录
        self.work_dir = work_dir
        if self.work_dir is None:
            self.work_dir = os.path.abspath(os.path.dirname(__file__.split('?')[0]))
        # self.work_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\","/") # exe也能加载为真实路径

        # 日志目录
        self.logs_dir = os.path.join(self.work_dir,logs_dir)

        # 测试资源目录
        self.test_res_dir = os.path.join(self.work_dir,"testcase","test_res")

        try:
            if self.is_logger:
                mylogger.addLogFilePath(os.path.join(self.work_dir, self.logs_dir))
        except Exception as e:
            logging.error(traceback.format_exc())

        # logging.info("work dir: %s" % self.work_dir)
        # logging.info("hello 鏡ちゃん")

# 在main中，这个实例化也会执行一次
environment = Environment()

if __name__ == "__main__":
    print(environment.work_dir)



