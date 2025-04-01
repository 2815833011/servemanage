# _*_ coding: utf-8 _*_
import pytest
import time
# import pyautogui 无法在服务器环境使用这个包
from random import randint
from selenium.webdriver.common.by import By
from src.utils.pyselenium import PySelenium

@pytest.mark.skip
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
        self.title=f"测试{randint(10000,888888)}"
        assert self.driver.asster(loginres)

    # def setup_method(self):
    #     '''
    #     前置条件
    #     '''
    #     self.driver.get("http://www.liuyanzu.tech/task/manage/#/login")
            
    @pytest.mark.skip(reason="1")  
    def test_01_add_banner(self):
        '''
        新增轮播图
        '''       
        
        annner_link=(By.XPATH,"//*[@class='el-icon-lx-hot']")
        annner_new=(By.XPATH,"//*[text()='新增Banner']")
        submit=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[3]/span/button[2]/span")
        upload=(By.NAME,"file")
        tittle=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[1]/div/div/input")
        link=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[4]/div/div/input")
        ass=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div")
        self.driver.click(annner_link)
        self.driver.force_wait(1)
        self.driver.click(annner_new)
        self.driver.type_clear(tittle)
        self.driver.type(tittle,self.title)
        self.driver.exeute_js('document.querySelector(".el-upload__input").style.display="block"')
        self.driver.force_wait(1)
        self.driver.type(upload,"/Users/admin/Documents/pythonproject/servemanage/data/Snipaste_2025-03-18_19-36-22.png")
        self.driver.force_wait(1)
        self.driver.type(link,"https://www.baidu.com")
        self.driver.click(submit)
        self.driver.force_wait(1)
        assert self.driver.text(ass)==f"{self.title}"
        print(self.title+"====================================================================")
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
        self.driver.find_element(tittle)
        self.driver.type(tittle,f"{self.title}")
        self.driver.force_wait(1)
        self.driver.click(upload)
        self.driver.force_wait(1)
        # pyautogui.write(r"C:/Users/EDY/Desktop/Snipaste_2025-02-17_14-18-48.png")
        self.driver.force_wait(1)
        # pyautogui.press("enter")
        self.driver.force_wait(1)
        # pyautogui.press("enter")
        self.driver.force_wait(1)
        self.driver.type(link,"https://www.baidu.com")
        self.driver.click(submit)
        self.driver.force_wait(1)
        assert self.driver.text(ass)==f"测试{self.title}"
        time.sleep(5)

    @pytest.mark.skip(reason="跳过")
    def test_02_update_banner(self):
        annner_link=(By.XPATH,"//*[@class='el-icon-lx-hot']")
        edite=(By.XPATH,f'//*[text()="{self.title}"]/../following-sibling::td[4]/div/button[1]')  #通过找子元素的 父元素来找出子元素的兄弟元素的子元素
        print(f'//*[text()="{self.title}"]/../following-sibling::td[4]/div/button[1]')
        tittle=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input")
        submit=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[3]/div/div[3]/span/button[2]")
        self.driver.click(annner_link)
        self.driver.click(edite)
        self.driver.type_clear(tittle)
        self.driver.type(tittle,f"奥特曼{self.title}")
        self.driver.click(submit)
        self.driver.force_wait(5)
    
    @pytest.mark.parametrize('data',[['禁用','停用'],['启用','启用']])
    def test_disable_banner(self,data):
        '''
        停用启用用例
        '''
        print(f'开始执行{data[0]}的用例')
        annner_link=(By.XPATH,"//*[@class='el-icon-lx-hot']")
        edite=(By.XPATH,'//*[text()="奥特曼测试707600"]/../following-sibling::td[4]/div/button[2]')  #通过找子元素的 父元素来找出子元素的兄弟元素的子元素
        stat=(By.XPATH,'//*[text()="奥特曼测试707600"]/../following-sibling::td[3]/div/span')
        self.driver.click(annner_link)
        self.driver.force_wait(3)
        self.driver.click(edite)
        self.driver.force_wait(1)
        assert self.driver.text(stat) == data[1]
        

    @pytest.mark.skip(reason="跳过")
    @pytest.mark.parametrize('data',['启用','禁用'])
    def test_select_banner(self,data):
        '''
        状态查询
        '''
        print(f"当前执行的是{data}用例===================")
        selector=(By.XPATH,'//*[@placeholder="状态"]')
        status=(By.XPATH,f'//ul[contains(@class,"el-scrollbar__view el-select-dropdown__list")]/li/span[text()="{data}"]')
        search=(By.XPATH,'//*[text()="搜索"]/..')
        actual=(By.XPATH,'//*[@class="el-pagination__total"]')
        expect=(By.XPATH,'//*[@class="el-table__row"]')
        listbutton=(By.XPATH,'//*[@ placeholder ="请选择"]')
        listpads=(By.XPATH,'//*[text()="100条/页"]')
        self.driver.click(selector)
        self.driver.force_wait(1)
        self.driver.click(status)
        self.driver.force_wait(1)
        self.driver.click(search)
        self.driver.force_wait(1)
        self.driver.click(listbutton)
        self.driver.force_wait(1)
        self.driver.click(listpads)
        self.driver.force_wait(1)
        expect_val=len(self.driver.find_elements(expect))
        actual_val=self.driver.find_element(actual).text
        print(f"{expect_val},{actual_val}====================")
        #  assert str(395) in actual_val

    @pytest.mark.skip
    @pytest.mark.parametrize('data',['1','2','3'])
    def test_lable_search(self,data):
        '''
        标题搜索
        '''
        bannerpage=(By.XPATH,"//i[@class='el-icon-lx-hot']")
        lasearch=(By.XPATH,'//input[@placeholder="标题"]')
        search=(By.XPATH,'//*[text()="搜索"]/..')
        actual=(By.XPATH,'//*[@class="el-pagination__total"]')
        expect=(By.XPATH,'//*[@class="el-table__row"]')
        listbutton=(By.XPATH,'//*[@ placeholder ="请选择"]')
        listpads=(By.XPATH,'//*[text()="100条/页"]')
        self.driver.click(bannerpage)
        self.driver.force_wait(1)
        self.driver.type_clear(lasearch)
        self.driver.force_wait(1)
        self.driver.type(lasearch,data)
        self.driver.force_wait(1)
        self.driver.click(search)
        self.driver.force_wait(1)
        self.driver.click(listbutton)
        self.driver.force_wait(1)
        self.driver.click(listpads)
        self.driver.force_wait(1)
        
        expect_val=len(self.driver.find_elements(expect))
        actual_val=self.driver.text(actual)

        # assert str(expect_val) in actual_val
    
    def teardown_class(self):
        self.driver.delete_all_cookies()
        self.driver.quit()