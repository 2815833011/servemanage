
from src.utils.yamloder import Yamloader

class Conf:
    def __init__(self):
        self.yaml=Yamloader().loder(filpath=r"conf\\conf.yaml")
        

    def get_driver_path(self,browser="chrome"):
        '''
        获取浏览器驱动地址
        '''
        return self.yaml["chromedriver"][browser]
    
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

if __name__ == "__main__":
    con=Conf()
    print(con.get_test_data())