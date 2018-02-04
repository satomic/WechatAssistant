# coding=utf-8

from Environment import environment


class ModelUtil(object):

    @staticmethod
    def demo(name="world"):
        print("hello {0}".format(name))



if __name__ == "__main__":
    ModelUtil.demo()