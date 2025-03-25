
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from src.utils.conf import Conf
from src.utils.logger import log
class PySelenium:
    __instance =None
    __driver=None
    __timeout=None
    def __new__(cls,brower="chrome",driverpath="driver/chromedriver.exe",timeout=30):
        '''
        单例化driver
        '''
        if not cls.__instance :
            cls.__instance =super().__new__(cls)  #判断对象是否存在 没有就创建一个
            cls.__timeout=timeout
            driverpath=Conf().get_driver_path(brower)
            options=cls.get_options(brower=brower)  #初始化时 会自动调用静态方法赋值
            service=cls.getserices(brower=brower,driverpath=driverpath)
            cls.__driver= getattr(cls,brower.lower())(options,service) #driver 没有就创建一个 通过反射获取 chrome/firefox 函数名对象 （）表示直接调用并传入参数
            cls.__driver.maximize_window()
        return cls.__instance   
            
    def __init__(self,): #初始化关键参数
       pass

    @classmethod
    def get_options(cls,brower):
        '''
            根据浏览器获取options
        '''
        if brower =="chrome":
            from selenium.webdriver import ChromeOptions as Options
        elif brower =="firefox":
            from selenium.webdriver import FirefoxOptions as Options

        option =Options()
        option.add_argument("--log-level=3")
        option.add_argument("--startmaximized")
        option.add_experimental_option("excludeSwitches", ["enable-automation"])

        return option
    @classmethod
    def getserices(cls,brower,driverpath):
        '''
            根据浏览器获取service
        '''
        if brower=="chrome" :
            from selenium.webdriver import ChromeService as service
        elif brower=="firefox":
            from selenium.webdriver import FirefoxService as service
        
        return service(executable_path=driverpath)
        
                  
    @classmethod
    def chrome(cls,option,services):
        '''
        打开谷歌浏览器
        '''
        return webdriver.Chrome(options=option,service=services)    
    
    @classmethod
    def firefox(cls,option,services):
        '''
        打开火狐浏览器
        '''
        return webdriver.Firefox(options=option,service=services)
    
    @log
    def get_origin_driver(self):
        '''
        获取driver
        '''
        return self.__driver
    
    @log
    def get(self,url):
        '''
        打开网页
        '''
        self.__driver.get(url)

    @log
    def find_element(self,locator):
        '''
        动态查找元素，默认超时时间30秒
        '''
        if not isinstance(locator,tuple):
            raise Exception('输入的格式必须时（by,value）')
        
        return WebDriverWait(self.__driver,self.__timeout).until(lambda a: a.find_element(*locator))
    
    @log
    def find_elements(self,locator):
        '''
        动态查找元素，默认超时时间30秒 显式等待
        '''
        if not isinstance(locator,tuple):
            raise Exception('输入的格式必须时（by,value）')
        
        return WebDriverWait(self.__driver,self.__timeout).until(lambda a: a.find_elements(*locator))
  

    @log
    def click(self,locator):
        '''
        点击元素
        '''
        return self.find_element(locator=locator).click()

    @log
    def type(self,locator,content):
        '''
        输入
        '''
        return self.find_element(locator=locator).send_keys(content)
    
    @log
    def asster(self,locator):
        '''
        断言
        '''
        return self.find_elements(locator=locator)
    @log
    def switch_to_alert(self):
        '''
        切换作用域
        '''
        self.__driver.switch_to_alert
    @log
    def switch_to_frame(self,locator=(By.TAG_NAME,'iframe')):
        '''
        切换到frame
        '''
        iframe= self.find_element(locator=locator)
        self.__driver.switch_to.frame(iframe)
    @log   
    def switch_to_new_window(self):
        """
        切换窗口
        """     
        window=self.__driver.window_handles
        self.__driver.switch_to.window(window[-1])
    @log
    def switch_to_default_content(self):
        '''
        切换回默认的作用域
        '''
        self.__driver.switch_to.default_content()
    @log
    def move_to_element(self,locator):
        '''
        移动到某个元素上
        '''
        ActionChains(self.__driver).move_to_element(self.find_element(locator=locator)).perform() #悬停
    @log
    def double_click(self,locator):
        '''
        双击
        '''
        ActionChains(self.__driver).double_click(self.find_element(locator=locator)).perform() #双击
    @log  
    def close(self):
        '''
        关闭浏览器
        '''
        self.__driver.close()
    @log
    def quit(self):
        '''
        销毁driver
        '''
        self.__driver.quit()
    @log
    def get_attribute(self,locator,attribute):
        '''
        获取元素属性
        '''
        return self.find_element(locator=locator).get_attribute(attribute)
    
    @log
    def text(self,locator):
        '''
        获取元素标签文本
        '''
        return self.find_element(locator=locator).text
    @log
    def refresh(self):
        '''
        浏览器刷新
        '''
        self.__driver.refresh()
    @log
    def wait(self,timeout=10):
        '''
        隐式等待
        '''
        self.__driver.implicitly_wait(timeout)
    @log
    def force_wait(self,timeout=10):
        '''
        强制等待
        '''
        time.sleep(timeout)

    @log
    def exeute_js(self,*args):
        '''
        执行js
        '''
        self.__driver.execute_script(*args)

    @log
    def maximize_window(self):
        '''
        浏览器最大化
        '''
        self.__driver.maximize_window()
    @log
    def minimize_window(self):
        '''
        浏览器最小化
        '''
        self.__driver.minimize_window()
    @log
    def set_window_size(self,height,width):
        '''
        设定打开浏览器窗口大小
        '''
        self.__driver.set_window_size(height,width)
    @log
    def save_screenshot(self,file):
        '''
        屏幕截图
        '''
        self.__driver.save_screenshot(file)
    @log
    def get_screenshot_as_png(self):
        '''
        屏幕截图png
        '''
        return self.__driver.get_screenshot_as_png()
    
    @log
    def delete_all_cookies(self):
        '''
        删除所有的 cookie
        '''
        self.__driver.delete_all_cookies()
        
    @log
    def movepage(self,locator):
        '''
        滚动界面
        '''
        e=self.find_element(locator)
        self.__driver.execute_script("arguments[0].scrollIntoView()",e)
    
    @log
    def type_clear(self,locator):
        '''
        清空输入框
        '''
        self.find_element(locator).clear()
        
    