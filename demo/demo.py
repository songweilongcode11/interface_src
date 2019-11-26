# coding=utf-8
import unittest
import ddt
import sys
from ddt import ddt, data, file_data, unpack
from src.common.excel_util import excel_util
import os
from src.base.base_interface import base_interface
from src.common.logger import logger

logger = logger("login").getlog()


@ddt
class login(unittest.TestCase, base_interface):
    father_path = os.path.abspath(os.path.dirname(__file__) + os.path.sep + "../../")
    curpath = father_path + "/data/login.xls"
    print(curpath)
    excel = excel_util(curpath, "Sheet1")
    testData = excel.next()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*testData)
    def test_login(self, testData):
        logger.info("执行登录接口开始")
        data = {}
        # print(testData)
        data["username"] = testData["username"]  # admin
        data["password"] = int(testData["password"])  # 1234
        print(data)
        # # data["submit"] = testData["confirm"] #1234
        # headers = {
        #     "Content-Typ":"application/json"
        # }
        # res = self.post(testData["url"], data, headers)
        # print(res.text)
        # self.assertIn(testData["username"], res.text, "请求成功")
        #


if __name__ == "__main__":
    unittest.main()

