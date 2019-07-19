# coding=utf-8
import requests
from common.logger import logger
import json
logger = logger('base_interface').getlog()
class base_interface(object):
    
    def post(self,url,data={},headers={}):
        logger.info("执行post请求开始")
        try:
            response = requests.post(url, data=data, headers=headers)
            logger.info("执行post请求成功")
            return response
        except BaseException as e:
            logger.info("请求失败！", str(e))
            return ""

    def get(self,url,data={},headers={}):
        logger.info("执行get请求开始")
        try:
            response=requests.get(url, data=data, headers=headers)
            logger.info("执行get请求成功")
            return response.content
        except BaseException as e:
            print ()
            logger.info("执行get请求失败！",str(e))
            return ""

    def put(self,url,data={},headers={}):
        logger.info("执行put请求开始")
        try:
            response = requests.put(url, data=data, headers=headers)
            logger.info("执行put请求成功")
            return response.content
        except BaseException as e:
            print ()
            logger.info("执行put请求失败！", str(e))
            return ""


# # 发送Post请求
# base_interface=base_interface()
# response1 = base_interface.post('http://httpbin.org/post',data = {'key':'value'})
# print response1.text
# 
# 发送get请求
# response2 = base_interface.get('https://api.github.com/events')
# print res_str.headers
# print res_str.content
# print response2.text
