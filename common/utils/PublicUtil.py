# coding=utf-8

from Environment import environment
import os
import random


class PublicUtil(object):

    @staticmethod
    def get_file_from_dir_randomly(dir, index=None):
        file_list = []
        for parent, dirnames, filenames in os.walk(dir):
            for file in filenames:
                file_list.append(os.path.join(parent, file))
        if not (index is not None and index < len(file_list) - 1):
            index = random.randint(0, len(file_list) - 1)
        return file_list[index]