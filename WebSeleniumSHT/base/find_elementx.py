#coding=utf-8

from util.read_inix import ReadIni
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
class FindElement(object):
    def __init__(self,driver):
         self.driver = driver
         self.read_ini = ReadIni()

    # ------------------------------------------------------------------------------------------------------------------
    #  显示等待：通过设置最大等待时间，检查频率对页面的元素来进行等待，一旦找到该元素，则停止等待，进入后续操作
    # 编辑人员：景召盼    时间：2020年4月2日
    #  需要导入的包：from selenium.webdriver.support.wait import WebDriverWait
    #  语法：  WebDriverWait(driver,t1,t2).until(lambda el: driver.find_element_by_xpath("//div[@id='1']/h3/a"))
    #   t1 设置等待的总时长， t2 设置检查频率的时间
    def get_WebDriverWait(self,t,element):
        WebDriverWait(self.driver,t,0.3).until(lambda el: self.get_element(element))

    # ------------------------------------------------------------------------------------------------------------------
    # 连续点击标题栏操作
    def get_elements_span(self,dictname):

        dict = {
            "span_BrowsingStatistics":["//span[text()='数据统计管理']","//span[text()='浏览量统计']"],
            "span_MobileBusinessOrder": ["//span[text()='订单管理']","//span[text()='移动业务订单']"]


        }
        # print(dict[dictname])
        # #  ["//label[text()='卡券类型']/../div/select", "//label[text()='卡券类型']/../div/select/option[2]"]
        # print(dict[dictname][0])
        # #  //label[text()='卡券类型']/../div/select
        # print(dict[dictname][1])
        # #   //label[text()='卡券类型']/../div/select/option[2]
        # print(len(dict[dictname]))
        #   2

        for x in range(len(dict[dictname])):
            #print(dict[dictname][x])
            time.sleep(2)
            self.driver.find_element_by_xpath(dict[dictname][x]).click()






    # ------------------------------------------------------------------------------------------------------------------
    # 输入框操作---------（key:定位的元素属性，keyvalue：输入框中填写的内容）
    # 输入框操作
    # 编辑人员：景召盼    时间：2020年4月1日
    # 执行步骤：先输入元素值 ，在输入输入框中要输入的内容
    # 使用方法如下，在Business中使用
    #举例：self.fd.get_element_send_keys("text_username",username)
    def get_element_send_keys(self,key,keyvalue):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value).send_keys(keyvalue)
            elif by == 'name':
                return self.driver.find_element_by_name(value).send_keys(keyvalue)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value).send_keys(keyvalue)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value).send_keys(keyvalue)
            else:
                return self.driver.find_element_by_xpath(value).send_keys(keyvalue)
        except:
            self.driver.save_screenshot('D:\idea_workSpace\PythonDemoVenv\WebSeleniumXF\Image/%s.png' %value)
            return None

    # ------------------------------------------------------------------------------------------------------------------
    # 点击操作---------（key:定位的元素属性）
    # 点击操作
    # 编辑人员：景召盼    时间：2020年4月1日
    # 执行步骤：先输入元素值 ，找到该元素属性后点击操作
    # 使用方法如下，在Business中使用
    # 举例：
    def get_element_click(self,key):

        data = self.read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value).click()
            elif by == 'name':
                return self.driver.find_element_by_name(value).click()
            elif by == 'className':
                return self.driver.find_element_by_class_name(value).click()
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value).click()
            else:
                return self.driver.find_element_by_xpath(value).click()
        except:
            self.driver.save_screenshot('D:\idea_workSpace\PythonDemoVenv\WebSeleniumXF\Image/%s.png' % value)
            return None


    def get_element(self,key):

        data = self.read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            self.driver.save_screenshot('D:\idea_workSpace\PythonDemoVenv\WebSeleniumXF\Image/%s.png' % value)
            return None

    def get_element01(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = (data.split('>')[1]).split('<')
        #print(value[0])
        #print(value[1])
        try:
            if by == 'xpath':
                return self.driver.find_element_by_xpath(value[0]).find_element_by_xpath(value[1]).click()
            else:
                return self.driver.find_element_by_id(value)
        except:
            return None

    # -----------------------------------------------------------------------------------------------------------------------
    # 判断页面元素是否存在-----()
    def isElementPresent(self,by,value):
        try:
            element = self.driver.find_element(by=by,value=value)
        except NoSuchElementException :
            print('页面元素不存在')
            return False
        else:
            return True

    # -----------------------------------------------------------------------------------------------------------------------
    #页面跳转制定的url---------（url:输入需要打开的浏览器地址）
    #浏览器页面刷新
    # 编辑人员：景召盼    时间：2019年8月31日
    # 执行步骤：先打开URL ，在进行页面刷新
    # 使用方法如下，在register_page中使用
    #def get_driver_into_url(self,getUrl):
    #   return self.fd.driver_get(getUrl)
    def driver_get(self,url):

        self.driver.get(url)
        self.driver.refresh()

    # -----------------------------------------------------------------------------------------------------------------------
    # c操作浏览器---------(driver_quit:关闭浏览器  ;driver_back: 返回上一次访问过的页面 ;driver_forward: 退回到首页面 ;driver_refresh: 刷新当前页面)
    # 编辑人员：景召盼    时间：2019年8月8日
    # 使用方法如下，在register_page中使用
    # def get_driver_quit(self):
    #    return self.fd.driver_quit()
    def driver_quit(self):
        self.driver.quit()

    # driver_back: 返回上一次访问过的页面
    def driver_back(self):
        self.driver.back()

    # driver_forward: 退回到首页面
    def driver_forward(self):
        self.driver.forward()

    # driver_refresh: 刷新当前页面
    def driver_refresh(self):
        self.driver.refresh()

    # -----------------------------------------------------------------------------------------------------------------------
    # 获取当前页面Url 链接---------()
    # 编辑人员：景召盼    时间：2020年8月27日
    # 使用方法如下，在register_page中使用
    #使用方法如下，在register_business中使用
    def driver_currentUrl(self):
        currentPageUrl = self.driver.current_url
        print("当前页面的url是：",currentPageUrl)
        return currentPageUrl


    # -----------------------------------------------------------------------------------------------------------------------
    # 模拟键盘单个按键操作下拉框-----from selenium.webdriver.common.keys import Keys
    # 编辑人员：景召盼    时间：2019年7月14日
    # query = driver.find_element_by_xpath("//label[text()='地市']/../div//input[@placeholder='请选择']")
    # query.click()
    # query.send_keys(Keys.ARROW_DOWN)
    # query.send_keys(Keys.ARROW_DOWN)
    # query.send_keys(Keys.ENTER)
    # time.sleep(3)
    # 需要导入from selenium.webdriver.common.keys import Keys
    # ele=query（定位元素） long表示点击次数send_keys(Keys.ARROW_DOWN)

    def down_box(self,ele,long):
        query = ele
        query.click()
        for i in range(1, long, 1):
            query.send_keys(Keys.ARROW_DOWN)
            time.sleep(3)
        query.send_keys(Keys.ENTER)
        time.sleep(3)
    #-----------------------------------------------------------------------------------------------------------------------
    # 滚动条移动到指定的元素位置-----()
    # 编辑人员：景召盼    时间：2019年7月23日
    # element = driver.find_element_by_xpath("//div[@class='el-scrollbar']//span[text()='高新']")
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    # time.sleep(3)

    def scrollInto_target(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)


    def scrollInto_target_click(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        time.sleep(3)
        ele.click()

    # def scroll_element(self):
    #     driver.execute_script("arguments[0].scrollIntoView();", element)
    #     time.sleep(3)
    #     element.click()

    def scroll_top(self):
        time.sleep(2)
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    def scroll_foot(self):
        time.sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)




    # -----------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------
    # 期望结果与实际结果对比判断-----(expect:期望结果，actual：实际结果)
    # 编辑人员：景召盼    时间：2019年7月29日
    #  内容说明：actual == expect、 else
    #  该功能使用def login_handle
    def test_result_comparison(self, expect, actual,testtitle):
        if actual == expect:
            #result = "test_ture"
            print(testtitle + "\033[34m实际结果与期望结果测试一致，\nexpect=\033[0m" + expect)
        else:
            #result = "test_false"
            print(testtitle + "\033[31m实际结果与期望结果测试不一致，\nexpect=\033[0m" + expect + "实际结果：" + actual)
        #return result

    # -----------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------
    # 操作IFrame中的页面元素-----
    # 编辑人员：景召盼    时间：2019年11月11日
    #  内容说明：
    #  该功能使用handle 层中直接调用get_iframe方法  传入参数Key : 为元素的定位
    # 使用举例：
    # self.fe.get_iframe("iframe_text_month_details")
    def get_iframe(self,key,businessname):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = (data.split('>')[1]).split('<')
        print(value[0])
        print(value[1])
        # str=data.split('>')
        # for i in str:
        #     print(i)

        try:
            iframe = self.driver.find_element_by_xpath(value[0])
            self.driver.switch_to.frame(iframe)
            self.driver.find_element_by_xpath(value[1]).send_keys(businessname+"月费详情内容输入")
            self.driver.switch_to.default_content()
        except:
            return None



