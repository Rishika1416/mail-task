import smtplib
from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from download_bs4 import *

class SendEmail:
    #loading login credentials 
    def __init__(self, to_):
        self.gmail_user = config('GMAIL_ID')
        self.gmail_password = config('GMAIL_PASSWORD')

        #to_=''vaishrishika@gmail.com''
        self.to_=to_

    #for appple mail make changes here
    def create_msg(self,file,msg_html,subject):
        msgRoot = MIMEMultipart('related')
        msgRoot['From'] = self.gmail_user
        msgRoot['To'] = self.to_
        msgRoot['Subject'] = subject
        message =MIMEMultipart('alternative')
        #message.attach(MIMEText('<b>This is the <i>HTML</i> content of this email</b> it contains an image.<br><img src="cid:image1"><br>This is a text below the image<br>',_subtype='html'))
        message.attach(MIMEText(msg_html,_subtype='html'))
        msgRoot.attach(message)

        #adding attachment to mail  'cats_img/images2.jpg'
        if file==None:
            return msgRoot
        else:
            with open(file, 'rb') as f:
                image=MIMEImage(f.read(),_subtype="jpg")
                if msgRoot.is_multipart():
                    print("yes_mail is multiport")
                image.add_header('Content-ID', '<image1>')
                msgRoot.attach(image)
                f.close()
                return msgRoot
    
    def send_mail(self,msgRoot):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            #text= message.as_string()
            smtp.login(self.gmail_user, self.gmail_password) #Login to SMTP server
            smtp.send_message(msgRoot, self.gmail_user,self.to_)