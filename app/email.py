from flask import render_template
from flask_mail import Message
from . import email 

'''
Function for sending email 
'''

def mail_message(subject , template , to , **kwargs):
    sender_email = "support@talanta.co.ke"
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    email.send(email)
    