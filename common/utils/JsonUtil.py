#coding=utf-8

from Environment import environment
import os
import logging
import json
import traceback
from common.utils.TimeUtil import TimeUtil


class JsonUtil(object):

    @staticmethod
    def load_dict_from_json_file(json_path):
        with open(json_path,"r") as f:
            return json.loads(f.read())

    @staticmethod
    def format(original, fp=None, indent=4):
        '''
        :param original: json file / json object/  json str
        :param fp: None to str/ fp to filepath, the file root dir is based on the calling script
        :param indent: indent with how many blanks
        :return: formatted json str / save to fp
        '''
        # i
        json_obj = None
        try:
            if isinstance(original, dict):
                json_obj = original
            elif isinstance(original,str): # pytohn3里面不区分str,unicode所以没有basestring，只有str
                # is json file
                if os.path.isfile(original):
                    json_obj = JsonUtil.load_dict_from_json_file(original)
                else:
                    # is json str
                    if isinstance(eval(original), dict):
                        json_obj = eval(original)

            if fp is None:
                # return formatted json str
                return json.dumps(json_obj,indent=indent)
            else:
                # write to file and return str
                with open(fp,"w") as fp:
                    json.dump(json_obj, fp, indent=indent)
                return json.dumps(json_obj, indent=indent)

        except Exception as e:
            # logging.error(e)
            logging.error(traceback.format_exc())



if __name__ == "__main__":
    # pp = pprint.PrettyPrinter(indent=4)
    path = r"D:\workspace\WechatAssistant\testcase\test_res\JsonUtil_hello.json"
    o = {'megamisama':17}
    logging.info(JsonUtil.format(path))
    logging.info(environment.logs_dir)
    logging.info(environment.version)
    logging.info(TimeUtil.current_time(3))