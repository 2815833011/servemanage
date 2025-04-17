# _*_ coding: utf-8 _*_
from src.utils.conf import Conf
class Report:
    def get_result(self,terminalreporter):
        '''
        获取测试结果
        '''
        print(terminalreporter.stats)
        passed,failed,skipped,errors,warning=[],[],[],[],[]
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

            if status == "error":
                for report in reports:
                    nodeid=report.nodeid
                    reason=report.longreprtext
                    errors.append({nodeid:reason})

            if status == "warnings":
                for report in reports:
                    nodeid=report.nodeid
                    reason=report.message
                    warning.append({nodeid:reason})

        print(passed,failed,skipped,errors)
        return passed,failed,skipped,errors,warning     
     
    def recourd_result(self,passed,failed,skiped,errors,warning):
        '''
        执行成功用例，失败用例，跳过用例大结果记录
        ''' 
        retval=True
        try:
            filepath=Conf().get_case_result()
            with open(file=filepath,mode="w",encoding="utf-8") as f:
                f.write(f"{len(passed)}:{len(failed)}:{len(skiped)}:{len(errors)}:{len(warning)}")
        except:
            retval=False 
        finally:
            return retval
        