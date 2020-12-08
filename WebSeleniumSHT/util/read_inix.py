#coding=utf-8
import configparser

class ReadIni():

    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "D:\\git\\test01\\WebSeleniumSHT\\config\\LocalElementSHT.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)


    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf

    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data


if __name__== '__main__':
    read_init = ReadIni()
    #如果查找元素可以找到输出：id>inputuserName3
    # 如果查找元素出现重复报错：option 'text_username' in section 'RegisterElement' already exists
    #如果差找不到元素出现：No option 'text' in section: 'RegisterElement'

    print(read_init.get_value('text_username'))

