import pandas as pd
import smtplib

SenderAddress = "your email"
password = "your password"

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Dear Partners, \n For your ease we have uploaded a tutorial on youtube about using our site as a partner.This video covers topics like how signup, signin, reset and change password, add packs and a lot more.You are now supposed to upload your packs from tommorrow onwards.Thanks \n Url: https://youtu.be/hWbj9VIwCJQ \n Sincerely, \n Developer"
subject = "How to use our site as a partner tutorial uploaded!!"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
