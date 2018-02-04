# coding=utf-8

from Environment import environment
from datetime import datetime


class TimeUtil(object):

    @staticmethod
    def current_time(cut_tail=3,time_pattern='%Y-%m-%d %H:%M:%S.%f'):
        '''
        :param cut_tail: 返回值末位需要去除的个数
        :param time_pattern: 时间戳的格式
        :return: 
        '''
        t = datetime.now().strftime(time_pattern)
        if cut_tail is not None:
            t = t[:-cut_tail]
        return t