import pytest
import os
from random import randint
from selenium.webdriver.common.by import By
from src.utils.pyselenium import PySelenium
from selenium.webdriver.common.action_chains import ActionChains

class TestUser:
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
        self.tele=str(randint(10000,800000))
        assert self.driver.asster(loginres)

    def setup_method(self):
        '''
        前置条件
        '''
        self.driver.get("http://www.liuyanzu.tech/task/manage/#/userList")
        self.name=f"用户测试{randint(10000,888888)}"
        self.driver.refresh()
        # userpage=(By.XPATH,"//*[@class='el-icon-lx-group']")
        # self.driver.click(userpage)
    
    def test_add_user(self):
        '''
        新增用户
        '''
        hh=os.path.abspath("data")
        path=os.path.join(hh,"Snipaste_2025-03-18_19-36-22.png")
        adduser =(By.XPATH,"//*[text()='新增用户']")
        inputname=(By.XPATH,"//*[text()='昵称']/../div/div/input")
        inputtele=(By.XPATH,"//*[text()='手机']/../div/div/input")
        filupbut=(By.XPATH,"//*[@class='el-upload el-upload--picture']/input")
        surebut=(By.XPATH,"//*[@id='app']/div/div[3]/div[2]/div/div[4]/div/div[3]/span/button[2]")
        teleinput=(By.XPATH,'//*[@placeholder="手机号"]')
        surebutton=(By.XPATH,'//button[@class="el-button el-button--primary el-button--small"]/span[text()="搜索"]')
        asstel=(By.XPATH,f"//*[text()='{self.tele}']")
        asstuser=(By.XPATH,f"//*[text()='{self.name}']")
        
        self.driver.force_wait(1)
        self.driver.click(adduser)
        self.driver.force_wait(1)
        self.driver.type_clear(inputname)
        self.driver.force_wait(1)
        self.driver.type(inputname,self.name)
        self.driver.force_wait(1)
        self.driver.type_clear(inputtele)
        self.driver.force_wait(1)
        self.driver.type(inputtele,self.tele)
        self.driver.exeute_js('document.querySelector(".el-upload__input").style.display="block"')
        self.driver.force_wait(1)
        self.driver.type(filupbut,path)
        self.driver.force_wait(1)
        self.driver.click(surebut)
        self.driver.force_wait(5)
        self.driver.refresh()
        self.driver.force_wait(1)
        self.driver.type(teleinput,self.tele)
        self.driver.force_wait(1)
        self.driver.click(surebutton)
        self.driver.force_wait(1)
        print(type(self.driver.text(asstuser)),type(self.name),self.driver.text(asstel),self.tele)
        assert self.driver.text(asstuser)==self.name 
        assert self.driver.text(asstel)==self.tele

    def test_updata(self):
        '''
        编辑用户
        '''
        teleinput=(By.XPATH,'//*[@placeholder="手机号"]')
        surebutton=(By.XPATH,'//button[@class="el-button el-button--primary el-button--small"]/span[text()="搜索"]')
        updatabut=(By.XPATH,f'//*[text()="{self.tele}"]/../../td[8]/div/button[2]')
        form_inputname=(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input')
        form_surebut=(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/span/button[2]')
        form_fileinput=(By.NAME,'file')
        assdataname=(By.XPATH,f'//*[text()="{self.name}"]')

        self.driver.type_clear(teleinput)
        self.driver.type(teleinput,self.tele) 
        self.driver.force_wait(1)
        self.driver.click(surebutton)
        self.driver.force_wait(1)
        self.driver.click(updatabut)
        self.driver.force_wait(1)
        
        self.driver.type(form_inputname,self.name)
        self.driver.force_wait(1)
        self.driver.exeute_js('document.querySelector(".el-upload__input").style.display="block"')
        self.driver.force_wait(1)
        self.driver.type(form_fileinput,'/Users/admin/Documents/pythonproject/servemanage/data/Snipaste_2025-03-18_19-36-22.png')
        self.driver.force_wait(1)
        self.driver.click(form_surebut)
        self.driver.force_wait(1)
        assert self.driver.find_element(assdataname)
        self.driver.force_wait(1)
    @pytest.mark.parametrize("data",["正常","已冻结","禁止发布任务"])
    def test_status_user(self,data):
        '''
        状态查询
        '''
        
        


        
        