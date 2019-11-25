#coding=utf-8
import unittest
import ddt
import sys
import json
from ddt import ddt,data,file_data,unpack
from src.common.excel_util import excel_util
import os
from src.base.base_interface import base_interface
from src.common.logger import logger
import queue


logger = logger("login").getlog()

@ddt
class login(unittest.TestCase,base_interface):
    father_path=os.path.abspath(os.path.dirname(__file__)+os.path.sep+"../../")
    curpath = father_path+"/data/login/login.xls"
    print(curpath)
    excel = excel_util(curpath,"Sheet1")
    testData = excel.next()

    def setUp(self):
        pass
    def tearDown(self):
        pass
    @data(*testData)
    def test_login(self, testData):
        logger.info("执行登录接口开始")
        data = {}
        data["username"] = testData["username"] #admin
        data["password"] = int(testData["password"])#1234
        print(data)
        # get_data = queue.Queue()
        # # forword = get_data.qsize()
        # # print(forword)
        # login_msg = get_data.put(data, timeout=5)
        # after = get_data.qsize()
        # # print(after)
        # # print(login_msg)
        # get_logindata = get_data.get()
        # # print(get_logindata)
        # username = get_data.get(data, timeout=5)
        # # # print(login_msg)
        # print(data)
        headers = {
            "Content-Typ":"application/json"
        }
        res = self.post(testData["url"],data, headers)
        print(res.json())
        self.assertIn(testData["username"], res.json(), "请求成功")


if __name__=="__main__":
    unittest.main()

