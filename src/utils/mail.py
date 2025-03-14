import yagmail
import traceback
from src.utils.conf import Conf

# sender={
#         "host":"smtp.qq.com",
#         "user":"2815833011@qq.com",
#         "password":"qyrultzvywigdcid"
#         }  #发件人

# to ={"2815833011@qq.com":"niubi"} #收件人
# cc={} #抄送人
# ymail=yagmail.SMTP(**sender) #解包
# ymail.send(to=to,subject="测试报告",contents="正文",attachments=r"D:\\新建文件夹\shopxowebrunner\data\\test_login_param.yaml") #发送邮件 标题 正文 附件

# ymail.close() #关闭


class Mail:

    def __init__(self):
        con = Conf()
        self.sender = con.get_mailsenduserdata()
        self.to = con.get_mailtouserdata()
        self.cc = con.get_mailccuserdata()
        self.active = con.get_mailactive()

    def send_mail(self, subject, contents, attachments=None):
        """
        发送邮件
        """
        retval = True #是否发送成功
        if self.active:
            """
            开始发送邮件
            """
            try:
                ymail = yagmail.SMTP(**self.sender)
                ymail.send(
                    to=self.to,
                    cc=self.cc,
                    subject=subject,
                    contents=contents,
                    attachments=attachments,
                )
                ymail.close()
            except:
                retval = False
                msg=traceback.format_exc()
                raise msg
        return retval


if __name__ == "__main__":
    Mail().send_mail(
        subject="报告",
        contents="封装",
        attachments=r"D:\\新建文件夹\shopxowebrunner\data\\test_login_param.yaml",
    )
