import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#please specify these environment variables before runnung the script
username = 'testmailabc123456@gmail.com'
password = 'helloworld123'


def send_email(text='Email Body', subject='Hello World', from_email='Test mail <testmailabc123456@gmail.com>', to_emails=['testmailabc123456@gmail.com'], html=None):
    assert isinstance(to_emails,list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != none:
        html_part = MIMEText("<h1>This is working</h1>", 'html')
        msg.attach(html_part)

    msg_str= msg.as_string()

    # loging in to smtp server 
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()