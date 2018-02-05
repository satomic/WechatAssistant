# coding=utf-8

import os,sys
import unittest

from Environment import environment
sys.path.append(environment.work_dir)

from common.utils.JsonUtil import JsonUtil



class Test_JsonUtil(unittest.TestCase):

    def setUp(self):
        self.test_res_dir = environment.test_res_dir
        self.json_path = os.path.join(self.test_res_dir,"JsonUtil_hello.json")

    def tearDown(self):
        pass

    def test_load_dict_from_json_file(self):
        target = {
            "hello": [
                "yao",
                "hui"
            ]
        }
        json_obj = JsonUtil.load_dict_from_json_file(json_path=self.json_path)
        self.assertDictEqual(target,json_obj)

    def test_format(self):
        target = '''{
    "hello": [
        "yao",
        "hui"
    ]
}'''
        json_formated_str = JsonUtil.format(self.json_path)
        self.assertEquals(target,json_formated_str)

    def _running_all(self):
        unittest.main()

if __name__ == "__main__":
    # import sys
    # sys.argv = ['', 'Test_JsonUtil.test_format']
    unittest.main()
