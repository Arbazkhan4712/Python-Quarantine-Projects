
# STANDARD LIBRARY IMPORTS
import smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import sys

# THIRD PARTY IMPORTS
import cv2

# gmail must be set to allow less secure apps, so you can send emails.
# set it up on:
# https://myaccount.google.com/u/1/lesssecureapps?pli=1


def send_mail(frame):

    path = os.path.dirname(sys.argv[0])

    log_file = path + '/email.log'

    # Check if the last email was sent in an 1 minute tolerance.
    # We are going to use a .log file to keep track of it.
    if os.path.isfile(log_file):  # First check if file exists.
        with open(log_file, 'r') as f:
            date = f.read()
            date_to_datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

            if datetime.now() < date_to_datetime + timedelta(minutes=1):
                return

    # Update the email log.
    with open(log_file, 'w') as f:
        f.write(str(datetime.now()))

    # Create the jpg picture to attach.
    cv2.imwrite("intrude.jpg", frame)

    gmail_user = 'Enter_gmail-ID_to_be_used_for_sending_the_email'
    gmail_password = 'Enter_gmail-ID_password_here'
    recipient = 'Enter_gmailID_of_the_recipient'
    recipient = 'Enter_gmailID_of_the_recipient'
    message = 'Hey! It appears that someone is at home!!!'

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = recipient
    msg['Subject'] = "Someone is at Home!"
    msg.attach(MIMEText(message))

    # Attachment
    file = path + '/intrude.jpg'
    filename = 'intrude.jpg'
    attachment = open(file, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s"
                    % filename)
    msg.attach(part)

    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(gmail_user, gmail_password)
    mail_server.sendmail(gmail_user, recipient, msg.as_string())
    mail_server.close()
