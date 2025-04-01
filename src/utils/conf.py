# _*_ coding: utf-8 _*_
from src.utils.yamloder import Yamloader
import platform

class Conf:
    def __init__(self):
        self.yaml=Yamloader().loder(filpath="/Users/admin/Documents/pythonproject/servemanage/conf/conf.yaml")
        

    def get_driver_path(self,browser="chrome"):
        '''
        获取浏览器驱动地址
        '''
        return self.yaml["selenium"]["chromedriver"][platform.system()][browser]
    
    def get_test_data(self,method):
        '''
        获取数据文件地址
        '''
        return f"{self.yaml["testdata"]}/{method}.yaml"

    def get_mailsenduserdata(self):
        '''
        获取发件信息
        '''
        return self.yaml["mail"]["sender"]
        
    def get_mailtouserdata(self):
        '''
        获取收件信息
        '''
        return self.yaml["mail"]["to"]
    
    def get_mailccuserdata(self):
        '''
        获取抄写人信息
        '''
        return self.yaml["mail"]["cc"]
    
    def get_mailactive(self):
        '''
        是否发邮件
        '''
        return self.yaml["mail"]["active"]
    
    def get_conftest(self):
        '''
        是否发邮件
        '''
        return self.yaml["conftest"]["screenshot"]
    
    def get_opention(self):
        '''
        浏览器头参数
        '''
        return self.yaml["selenium"]["opentions"]["add_argument"]

if __name__ == "__main__":
    con=Conf()
    print(con.get_driver_path(),platform.system())