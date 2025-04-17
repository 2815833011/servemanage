# _*_ coding: utf-8 _*_
from jenkins import Jenkins
import requests
import os
import time
import hmac
import hashlib
import base64
import urllib.parse
CONFIG={
        "url":"http://42.194.159.123:8081",
        "username":"tangying",
        "password":"123456",
        "job_name":"testrunner"

}


CASERESULT=os.path.join(os.path.abspath("report"),"case_result.text")

class JenkinsRead :

    def get_info(self):
        '''
        获取Jenkins 的最后一次配置信息   
        ''' 
        config=CONFIG
        job_name=config.pop("job_name")
        server=Jenkins(**config)
        job=server.get_job_info(job_name)["lastBuild"]
        print(job)
        url=job['url']+"allure/"
        num=job['number']

        with open(file=CASERESULT,mode="r" ,encoding="utf-8") as file:
                data=file.read().split(":")
                msg=f"**************************** \
                        \n成功用例:{data[0]}\
                        \n失败用例:{data[1]}\
                        \n跳过用例:{data[2]}\
                        \n报错用例:{data[3]}\
                        \n警告用例:{data[4]}\
                        \n构建地址:{url}\
                        \n报告地址:{url}\
                        \n****************************"

        return msg

DINGTALKAPI="https://oapi.dingtalk.com/robot/send"
DINGTOKEN="9b2475394f2c4f30e7af275d23f0a9eb3225493b7acfb185e6740a38ad974297"
APPSECRET="SEC834a32352ce2d37535f91d4b608e0ceb99571cbf4a37979e532a694af437474a"
class DingTalk: 
     def __init__(self):
                self.timestamp = str(round(time.time() * 1000))
                secret_enc = APPSECRET.encode('utf-8')
                string_to_sign = '{}\n{}'.format(self.timestamp, APPSECRET)
                string_to_sign_enc = string_to_sign.encode('utf-8')
                hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
                self.sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
                print(self.timestamp)
                print(self.sign)

     def send_msg(self,msg):
          '''
                发送消息
          '''
          params={"access_token":DINGTOKEN,"timestamp":self.timestamp,"sign":self.sign}
          
          data={"text":{"content":msg},"msgtype":"text"}
          retval=True
          try:
                res=requests.post(url=DINGTALKAPI,json=data,params=params)
                print(res.text)
          except :
                retval=False

          return retval
        
          
          
if __name__=="__main__":
       
        DingTalk().send_msg(JenkinsRead().get_info())
    
# for k,v in job_name.items():
#     print(k,v)


# dmin@admindeMacBook-Pro servemanage % allure generate report/result -o report/report --clean
# Report successfully generated to report/report
# admin@admindeMacBook-Pro servemanage % allure open report/report