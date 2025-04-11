# _*_ coding: utf-8 _*_
from src.utils.conf import Conf
class Report:
    def get_result(self,terminalreporter):
        '''
        获取测试结果
        '''
        print(terminalreporter.stats)
        passed,failed,skipped=[],[],[]
        for status,reports in terminalreporter.stats.items():
            if status == "passed":
                for report in reports:
                    nodeid=report.nodeid
                    reason=report.longreprtext
                    passed.append({nodeid:reason})

            if status == "failed":
                for report in reports:
                    nodeid=report.nodeid
                    reason=report.longreprtext
                    failed.append({nodeid:reason})

            if status == "skipped":
                for report in reports:
                    nodeid=report.nodeid
                    reason=report.longreprtext
                    skipped.append({nodeid:reason})
        print(passed,failed,skipped)
        return passed,failed,skipped       
    def recourd_result(self,passed,failed,skiped):
        '''
        执行成功用例，失败用例，跳过用例大结果记录
        ''' 
        retval=True
        try:
            filepath=Conf().get_case_result()
            with open(file=filepath,mode="w",encoding="utf-8") as f:
                f.write(f"{passed}{failed}{skiped}")
        except:
            retval=False
        finally:
            return retval
        