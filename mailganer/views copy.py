# -*- encoding: utf-8 -*-
import string
import smtplib
import os, time
from .models import Email

from dotenv import load_dotenv

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from django.shortcuts import render
from django.http import HttpResponse


load_dotenv ()

def index(request):

    def get_templates_info():
        data = []
        try:
            with open("subscribers.txt", 'r', encoding='utf-8') as f:
                list = [line.split(", ") for line in f]
        except IOError:
            return "Файл подписчиков не найден!"

        for a in list:
            data.append({
                "mail_to":a[0],
                "name":a[1],
                "date_of_birth":a[2]
                })
        return data

    def message_formation(id, name, date_of_birth):
        data = {
            "name":name,
            "date_of_birth":date_of_birth
        }
        mail_subj = name+" "+date_of_birth  # Theme message
        mail_coding = "utf-8"
        multi_msg = MIMEMultipart()
        multi_msg["Subject"] = Header(mail_subj, mail_coding)


        try:
            with open("template.html", 'r', encoding='utf-8') as file:
                temp = file.read()
        except IOError:
            return "Файл шаблона не найден!"

        template = string.Template(temp)
        new_template = template.substitute(data)
        msg = MIMEText(new_template, "html", mail_coding)
        msg.set_charset(mail_coding)
        multi_msg.attach(msg)
        return multi_msg.as_string()
                 

    def send_email():
        data = get_templates_info()
        # emails = Email.objects.all()
        for email in data:
            id = ""
            mail_to=email["mail_to"]
            name=email["name"]
            date_of_birth=email["date_of_birth"]
            # Параметры SMTP-сервера
            smtp_server = "smtp.mail.ru"
            smtp_port = 25
            smtp_pwd = os.getenv("PASS")  # pass smtp
            mail_from = os.getenv("USER")

            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(mail_from, smtp_pwd)
                Email.objects.create(name=name, mail_to=mail_to, track="NO")
                emails = Email.objects.all()
                message=message_formation(id, name, date_of_birth)
                server.sendmail(mail_from, mail_to, message)
                # emails.append(email)
                time.sleep(1)
                server.quit()
            except Exception as _ex:
                return "Не верный логин или пароль!"

        return Email.objects.all()

    if request.method == "POST":
        run = send_email()
        all_emails=[]
        if run == "Не верный логин или пароль!":
            context = {
                "all_info": [run]
            }
        else: 
            for email in run:
                email_info = {
                    "mail_to":email.mail_to,
                    "name":email.name
                }
                all_emails.append(email_info)
            context = {
                "all_info": all_emails
            }

    else:
        emails = Email.objects.all()
        all_emails=[]
        for email in emails:
            email_info = {
                "mail_to":email.mail_to,
                "name":email.name
            }
            all_emails.append(email_info)
        context = {
            "all_info": all_emails
        }


    return render(request, 'mailganer/index.html', context)