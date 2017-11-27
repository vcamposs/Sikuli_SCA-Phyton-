import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import Uteis
from Uteis import *
reload(Uteis)

def Email(toaddr,subject,body):
  fromaddr = "victor.campos.silva09@gmail.com"
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'plain'))
  server = smtplib.SMTP('smtp.googlemail.com:587')
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(fromaddr, "SENHA EMAIL")
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()

Email("victor.campos.silva09@gmail.com","ploc","plac")