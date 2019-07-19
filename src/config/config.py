# coding=utf-8
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
class config(object):
    #**************配置邮件******************
    smtpserver = 'smtp.qiye.163.com'
    sender_username = ''
    sender_password = ''
    subject="UI自动化报告"
    mail_to=["56825486@qq.com"]
    msg_body="接口自动化测试报告，系统自动发送，请勿回复！"
    mail_cc=[]

    def get_mail_content(self):
        msg_body="Hi All<br>" 
        msg_body=msg_body+'&nbsp; &nbsp;<span style="font-weight:bold;">接口自动化测试报告，请勿回复！</span><br>'
        msg_body=msg_body+'&nbsp; &nbsp;<span style="font-weight:bold;">详情请查看附件！</span><br>'
        return msg_body

#发送邮箱
sent_qq = '528039361'
#发送密码
qq_pwd = 'hpmvqyrksahjbhef'
#收件人邮箱receiver
receiver = '2208410357@qq.com'
mail_msg = 'hello this test qq sent msg!'
mail_title = 'grant test'
def sent_email(sent_qq, qq_pwd, receiver, mail_msg, mail_title):
    host_server = 'smtp.qq.com'
    sent_qq_email = sent_qq+'@qq.com'
    #ssl登陆
    smtp = SMTP_SSL(host_server)
    #开启邮箱调试1为开启，2为关闭邮箱调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sent_qq, qq_pwd)
    msg = MIMEText(mail_msg,'plain','utf-8')
    msg["Subject"] = Header(mail_title,'utf-8')
    msg['From'] = sent_qq_email
    msg['To'] = receiver
    smtp.sendmail(sent_qq_email,receiver,msg.as_string())
    smtp.quit()

sent_email(sent_qq=sent_qq,qq_pwd=qq_pwd,receiver=receiver,mail_msg=mail_msg,mail_title=mail_title)
