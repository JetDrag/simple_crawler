#-*-coding:utf8-*-
__author__ = 'i'

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import smtplib
import os

class Email():
    def send(self, host, mail_from, mail_to_l, subject, text, files = []):
        text += '''<br/><br/><br/><br/>---------------------------------<br/>
        <b>Note:</b><br/>
        This is an automatic notification email, <br/>
        please <b>DO NOT</b> replay this email directly.'''
        try:
            msg = MIMEMultipart()
            msg['From'] = mail_from
            msg['Subject'] = subject
            msg['To'] = ','.join(mail_to_l)  # COMMASPACE==', '
            msg['Date'] = formatdate(localtime=True)
            msg.attach(MIMEText(text, _subtype='html', _charset='utf-8'))

            for _file in files:
                part = MIMEBase('application', 'octet-stream')  # 'octet-stream': binary data
                part.set_payload(open(_file, 'rb').read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(_file))
                msg.attach(part)

            smtp = smtplib.SMTP(host)
            # smtp.login(Mail.USER, Mail.PWD)
            smtp.sendmail(mail_from, mail_to_l, msg.as_string())
            smtp.quit()
            # smtp.close()
            print True
        except Exception, e:
            print e
            print False

    def start(self, IP, address, mail_to_list, function, data_str, file_list):
        self.send(IP, address, mail_to_list, function, data_str, file_list)
