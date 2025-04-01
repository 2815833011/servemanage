# _*_ coding: utf-8 _*_
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