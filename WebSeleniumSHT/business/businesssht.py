#coding=utf-8
from base.find_elementx import FindElement
import time
class RegisterBusiness(object):

    def __init__(self,driver):
        self.fd = FindElement(driver)

    #--------------登录功能测试用例---------------------------------------------------------------------------------
    def login_business(self,username,password,expect,testtitle):

        self.fd.get_element_send_keys("text_username",username)
        print("shuru-----------1111111111111")
        self.fd.get_element_send_keys("text_password",password)
        print("shuru-----------2222222222222")
        time.sleep(2)
        self.fd.get_element_click("button_login")
        time.sleep(3)
        # 登录成功后获取首页面的Url做对比
        actual = self.fd.driver_currentUrl()
        self.fd.test_result_comparison(expect,actual,testtitle)


    def close_driver(self):
        self.fd.driver_quit()