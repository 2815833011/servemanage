import pytest
import time
import pyautogui
from selenium.webdriver.common.by import By
from src.utils.pyselenium import PySelenium

class TestBanner:
    def setup_class(self):
        ''''登录一次'''
        self.driver=PySelenium()
        self.driver.get("http://www.liuyanzu.tech/task/manage/#/login")
        username=(By.XPATH,'//input[@class="el-input__inner" and @type="text"]')
        password=(By.XPATH,'//input[@class="el-input__inner" and @type="password"]')
        button=(By.XPATH,"//*[text()='登录']")
        loginres=(By.XPATH,"//*[text()='登录成功']")

        self.driver.type(username,"admin")
        self.driver.type(password,"123456")
        self.driver.click(button)
        assert self.driver.asster(loginres)

    def setup_method(self):
        '''
        前置条件
        '''
        self.driver.get("http://www.liuyanzu.tech/task/manage/#/login")
            
    @pytest.mark.skip(reason="1")   
    def test_add_banner(self):
        '''
        新增轮播图
        '''       
        annner_link=(By.XPATH,"//*[text()='轮播图管理']")
        annner_new=(By.XPATH,"//*[text()='新增Banner']")
        submit=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[3]/span/button[2]/span")
        upload=(By.NAME,"file")
        tittle=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[1]/div/div/input")
        link=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[4]/div/div/input")
        ass=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div")
        self.driver.click(annner_link)
        self.driver.force_wait(1)
        self.driver.click(annner_new)
        self.driver.type(tittle,"测试")
        self.driver.exeute_js('document.querySelector(".el-upload__input").style.display="block"')
        self.driver.force_wait(1)
        self.driver.type(upload,r"C:\\Users\\EDY\Desktop\Snipaste_2025-02-17_14-18-48.png")
        self.driver.force_wait(1)
        self.driver.type(link,"https://www.baidu.com")
        self.driver.click(submit)
        self.driver.force_wait(1)
        assert self.driver.text(ass)=="测试"
        time.sleep(5)
    
    @pytest.mark.skip(reason="2")
    def test_add_pyautogui_banner(self):
        '''
        另一种上传文件的方式
        '''
        annner_link=(By.XPATH,"//*[text()='轮播图管理']")
        annner_new=(By.XPATH,"//*[text()='新增Banner']")
        tittle=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[1]/div/div/input")
        upload=(By.XPATH,"//*[text()='点击上传']")
        link=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[4]/div/div/input")
        submit=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[3]/span/button[2]/span")
        ass=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div")
        
        self.driver.click(annner_link)
        self.driver.force_wait(1)
        self.driver.click(annner_new)
        self.driver.type(tittle,"测试")
        self.driver.force_wait(1)
        self.driver.click(upload)
        self.driver.force_wait(1)
        pyautogui.write(r"C:\Users\EDY\Desktop\Snipaste_2025-02-17_14-18-48.png")
        self.driver.force_wait(1)
        pyautogui.press("enter")
        self.driver.force_wait(1)
        pyautogui.press("enter")
        self.driver.force_wait(1)
        self.driver.type(link,"https://www.baidu.com")
        self.driver.click(submit)
        self.driver.force_wait(1)
        assert self.driver.text(ass)=="测试"
        time.sleep(5)


    def test_update_banner(self):
        annner_link=(By.XPATH,"//*[text()='轮播图管理']")
        self.driver.click(annner_link)
        tr=(By.XPATH,'//*[text()="测试"]')
        upddate=(By.XPATH,"./following-sibling::td/button[1]")
        self.driver.find_fa_element(tr,upddate)

    def teardown_class(self):
        self.driver.delete_all_cookies()
        self.driver.quit()