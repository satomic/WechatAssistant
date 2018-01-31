#coding=utf-8

import os
import logging
from common.log.mylogging import mylogger
import traceback

# 日志打印开关
IS_LOGGER = True
# IS_LOGGER = False

def initlogging():
    try:
        gv_path = os.path.abspath(os.path.dirname(__file__.split('?')[0]))
        if IS_LOGGER:
            mylogger.addLogFilePath(os.path.join(gv_path, 'logs'))
    except Exception as e:
        logging.error(traceback.format_exc())
        # traceback.print_stack()

if __name__ == "__main__":
    initlogging()
    logging.info("hello 鏡ちゃん")
