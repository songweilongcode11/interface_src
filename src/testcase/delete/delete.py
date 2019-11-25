# coding=utf-8
import unittest
import ddt
import sys
from ddt import ddt, data, file_data, unpack
from src.common.excel_util import excel_util
import os
from src.base.base_interface import base_interface
from src.common.logger import logger

logger = logger("delete").getlog()


@ddt
class delete(unittest.TestCase, base_interface):
    father_path = os.path.abspath(os.path.dirname(__file__) + os.path.sep + "../../")
    curpath = father_path + "/data/Delete_Listing/listing.xls"
    print(curpath)
    excel = excel_util(curpath, "Sheet1")
    testData = excel.next()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*testData)
    def test_delete(self, testData):
        logger.info("执行登录接口开始")
        data = {}
        # print(testData)

        data["listingID"] = int(testData["listingID"])
        print(data["listingID"])
        # # data["password"] = int(testData["password"])
        # # data["submit"] = testData["confirm"] #1234
        # headers = {
        #     "Content-Typ": "application/json"
        # }
        # res = self.delete(url=' https://bindo.com/api/v2/stores/36323/listings/'+listing_id ,
        #                   headers=headers
        #                   )
        # # self.assertIn(testData["username"], res.text, "请求成功")
        # print(res.text)



if __name__ == "__main__":
    unittest.main()

