# import os,sys
# sys.path.append(os.getcwd)
import pytest
from src.utils.pyselenium import PySelenium
from selenium.webdriver.common.by import By
from src.utils.conf import Conf
# from src.po.login_page import LoginPage
from src.utils.report import Report
from src.utils.mail import Mail
from src.utils.logger import Logger
import allure
# @pytest.fixture(params=[['123456','123456','A1B2']])
# def login(request):
#     '''
#     前置条件
#     '''
#     pyselenium=PySelenium()
#     pyselenium.get("http://192.168.45.32/shopxo/")
#     pyselenium.click((By.LINK_TEXT, "登录"))
#     pyselenium.type((By.NAME, "accounts"), request.param[0])
#     pyselenium.type((By.NAME, "pwd"), request.param[1])
#     pyselenium.type((By.NAME, "verify"), request.param[2])
#     pyselenium.click((By.XPATH, "//button[text()='登录']"))
#     d = datetime.datetime.now()
#     pyselenium.save_screenshot(f"report/{d.strftime('%Y%m%d%H%M%S')}.png")  # 截图
#     assert pyselenium.asster((By.NAME, "verify"))

# @pytest.fixture(params=[['123456','123456','A1B2']])
# def login_po(request):
#     '''
#     po模式的例子  前置条件
#     '''
#     loginpage=LoginPage(PySelenium())
#     loginpage.navigate()
#     loginpage.login(*request.param)




def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''
        获取所有测试结果
    '''
    passed,failed,skipped,errors,warning= Report().get_result(terminalreporter)
    travel=Report().recourd_result(passed=passed,failed=failed,skiped=skipped,errors=errors,warning=warning)
    if travel:
        print("测试报告保存成功")
    else:
        print("测试报告保存失败")
    subjiect="shopxotestrunnner执行结果"
    content=f"通过用例数{len(passed)},失败用例{len(failed)},跳过用例{len(skipped)},errors{len(errors)}"
    Logger().info(content)
    Mail().send_mail(subject=subjiect,contents=content)


@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    '''
        每次执行都来收集结果
    '''
    report= yield
    report= report.get_result()
    passed=Conf().get_conftest()["passed"]
    failed=Conf().get_conftest()["failed"]
    pyselenium=PySelenium()
    if report.when=="call":
        if passed and report.outcome=="passed":
             with allure.step("成功截图"):
                allure.attach(
                    name="执行结果",
                    body=pyselenium.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG,
                )
        if failed and report.outcome=="failed":
             with allure.step("失败截图"):
                allure.attach(
                    name="执行结果",
                    body=pyselenium.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG,
                )
    


   
# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     '''
#         获取所有测试结果
#     '''
#     print(terminalreporter.stats)
#     passed,failed,skipped=[],[],[]
#     for status,reports in terminalreporter.stats.items():
#         if status == "passed":
#             for report in reports:
#                 nodeid=report.nodeid
#                 reason=report.longreprtext
#                 passed.append({nodeid:reason})

#         if status == "failed":
#             for report in reports:
#                 nodeid=report.nodeid
#                 reason=report.longreprtext
#                 failed.append({nodeid:reason})

#         if status == "skipped":
#             for report in reports:
#                 nodeid=report.nodeid
#                 reason=report.longreprtext
#                 skipped.append({nodeid:reason})
#     print(passed,failed,skipped)
#     return passed,failed,skipped                
            
            
            