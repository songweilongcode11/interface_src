#coding=utf-8
import unittest
import time
import ddt
from ddt import ddt,data,file_data,unpack
from common.excel_util import  excel_util
import os
from base.base_interface import  base_interface
from common.logger import logger
from testcase.login.login import login
class login_def(base_interface):
    def login_func(self,username,password):
        data={}
        data["name"] = username #admin
        data["pwd"] = password #1234
        data["submit"] = "确定" #1234       
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                   "Content-Type":"application/x-www-form-urlencoded",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                   "Cookie":"JSESSIONID=23D6CB92B7284700889D520E85FC353F"}
        res = self.post("http://47.98.180.183:8080/JspLibrary/manager.do?action=login",data=data,headers=headers)
        print (res.headers)
        return res.headers["Set-Cookie"]
    
login_def =login_def()
login_def.login_func("java1234", "12345")