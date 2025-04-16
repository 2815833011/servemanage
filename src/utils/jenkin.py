# _*_ coding: utf-8 _*_
from jenkins import Jenkins

import os

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
                msg=f"****************************{file.read()},构建地址:{url},报告地址{url}**************************"

        return msg

if __name__=="__main__":
    print(JenkinsRead().get_info())
# for k,v in job_name.items():
#     print(k,v)


# dmin@admindeMacBook-Pro servemanage % allure generate report/result -o report/report --clean
# Report successfully generated to report/report
# admin@admindeMacBook-Pro servemanage % allure open report/report