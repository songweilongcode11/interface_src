#coding=utf-8
import unittest
from selenium import webdriver
import time
import HTMLTestRunner
import io
from ddt import ddt,data,file_data,unpack
import os
from src.config.config import  config
from src.testcase.login import login


def load_tests():
    testunit=unittest.TestSuite()
    #使用discover找出用例文件夹下test_casea的所有用例
    father_path=os.path.abspath(os.path.dirname(__file__)+os.path.sep+"../")
    discover =unittest.defaultTestLoader.discover(father_path+"/testcase", pattern="*.py", top_level_dir=None)
    for suite in discover:  #使用for循环出suite,再循环出case
        for case in suite:
            testunit.addTest(case)
    return testunit

#运行用例病生成suite
def run_testcase():
    #格式化报告名称与路径
    time_format = time.strftime("%Y%m%d%H%M",time.localtime())
    report_path = os.path.dirname(os.path.abspath("."))+"/reports"
    file_path = report_path+"/report"+time_format+".html"
    #生成测试报告
    fp = open(file_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"接口自动化测试报告",description=u"用例执行概要")
    runner.run(load_tests())
    fp.close()
    time.sleep(5)
    return file_path

if __name__=="__main__":
    report_path=run_testcase()
