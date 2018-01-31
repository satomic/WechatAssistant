#coding=utf-8
import logging.handlers
import time,os
import sys


class MyLogger(object):

    def __init__(self,logName='MyLogger'):
        # create formatter
        self.formatter = logging.Formatter('%(asctime)s:%(thread)s:%(levelname)s:%(message)s')
        self.logger = None
        self._initLogger(logName)

    def addLogFilePath(self,logFilePath=None):
        if logFilePath:
            logPath = logFilePath
        else:
            logPath = os.curdir
        if not os.path.isdir(logPath):
            os.makedirs(logPath)
        logfileName = str(time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time())))+'.log'
        sLogFile = os.path.join(logPath,logfileName)

        # create rotating file handler and set level to debug
        handlerFile = logging.handlers.RotatingFileHandler(sLogFile,maxBytes=5*1024*1024,backupCount=10)
        handlerFile.setLevel(logging.DEBUG)

        # add formatter to ch
        handlerFile.setFormatter(self.formatter)

        # add ch to logger
        self.logger.addHandler(handlerFile)

    def _initLogger(self,logName='MyLogger'):
        if self.logger is not None:
            return

        # create logger
        self.logger = logging.getLogger(logName)
        self.logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        handlerStream = logging.StreamHandler(sys.stdout)
        handlerStream.setLevel(logging.INFO)

        # add formatter to ch
        handlerStream.setFormatter(self.formatter)

        # add ch to logger
        self.logger.addHandler(handlerStream)

if __name__ == '__main__':
    # import mylogging
    logging.info('this is a test log')

