#coding=utf-8
from business.businesssht import RegisterBusiness
class RegisterHandle(object):

    def __init__(self,driver):
        self.business = RegisterBusiness(driver)

    # ----------------------------登录功能login_handle----------------------------------------------------------------
    # 参数说明：  （username：用户名，password：登录密码）
    def login_handle(self,username,password,expect,testtitle):
        self.business.login_business(username,password,expect,testtitle)


    def close_driver_handle(self):
        self.business.close_driver()

