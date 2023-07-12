import requests
import os
import smtplib
import datetime as dt
import random
import pandas as pd
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid="AC6acdcd1c63d8fb69516c916c2bb92cbb"
auth_token="7f7d33098fa6a480f0ed46c3a3ece5cd"

current= dt.datetime.now()
current_tuple=(current.month, current.day)

data=pd.read_csv("exams.csv")
p=data['date']
r=data['month']
date_array = p.to_numpy()
month_array = r.to_numpy()
for i in range(len(date_array)):
    if date_array[i] > 7:
        date_array[i] -= 7
    else:
        date_array[i] += 23
        month_array[i] -= 1


exam_dict={(data_row["month"], data_row["date"]): data_row for (index,data_row) in data.iterrows()}
if current_tuple in exam_dict:
    exam_students=exam_dict[current_tuple]
    file_path="new_data.csv"
    with open(file_path) as f:
        contents=f.read()
        if exam_students['date']>23:
            exam_students["date"]=exam_students["date"]-23
            exam_students["month"]+=1
        else:
            exam_students['date']+=7
        contents=contents.replace("[Year]", str(exam_students["course_year"]))
        contents = contents.replace("[Number]", str(exam_students["sem"]))
        contents = contents.replace("[Date]", str(exam_students["date"]))
        contents = contents.replace("[Month]", str(exam_students["month"]))

        proxy_client=TwilioHttpClient()
        proxy_client.session.proxies={'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"hello,{contents}",
            from_="+12705887289", # this is twilio phone number
            to="+916304512130" # actual number to receive sms
        )
        print(message.status)


#use python anywhere to run it daily/automatically once per day.