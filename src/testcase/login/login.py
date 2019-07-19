#coding=utf-8
import unittest
import ddt
import sys
from ddt import ddt,data,file_data,unpack
from common.excel_util import excel_util
import os
from base.base_interface import base_interface
from common.logger import logger


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
        print(testData)
        data["name"] = testData["username"] #admin
        print(type(data["name"]))
        data["pwd"] = int(testData["password"]) #1234
        print(data["pwd"])
        data["submit"] = testData["confirm"] #1234
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                   "Cookie":"JSESSIONID=23D6CB92B7284700889D520E85FC353F"}
        res = self.post(testData["url"], data, headers)
        # print res.text
        self.assertIn(testData["username"], res.text, "请求成功")
        print(res.text)



if __name__=="__main__":
    unittest.main()
