#coding=utf-8
import sys

from handle.handlesht import RegisterHandle
from selenium import webdriver
import time
class FirstCase(object):

    def __init__(self):
        driver = webdriver.Chrome()
        #driver.implicitly_wait(30)
        driver.get('http://www.testclass.net/readers/sign_in')
        driver.maximize_window()
        self.register_h = RegisterHandle(driver)


    # ----------------------------登录功能login_case---------------------------------------
    def test_login(self):
        self.register_h.login_handle("757639413@qq.com","123456","http://www.testclass.net/","登录功能测试")

    # ----------------------------移动业务订单MobileBusinessOrder---------------------------------------


    def test_close(self):
        self.register_h.close_driver_handle()


if __name__ == '__main__':
    fc = FirstCase()
    fc.test_login()
    fc.test_close()
