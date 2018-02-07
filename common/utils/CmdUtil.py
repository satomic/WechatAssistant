# coding=utf-8

from PIL import ImageGrab


class CmdUtil(object):

    @staticmethod
    def print_screen(img_save_path=None):
        try:
            pic = ImageGrab.grab()
            p = "temp.jpg"
            if img_save_path:
                p = img_save_path
            pic.save(p)
            return p
        except:
            return False
