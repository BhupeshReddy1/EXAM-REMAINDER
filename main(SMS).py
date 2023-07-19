import requests
import os
import smtplib
import datetime as dt
import random
import pandas as pd
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
current= dt.datetime.now()
#from twilio.http.http_client import TwilioHttpClient

account_sid=os.environ.get("S_ID")
auth_token=os.environ.get("AUTH_TOKEN")

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

        #proxy_client=TwilioHttpClient()
        #proxy_client.session.proxies={'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"exam remainder ,{contents}",
            from_=os.environ.get("TWILIO_NUMBER"), # this is twilio phone number
            to=os.environ.get("TO_NUMBER")
            # actual number to receive sms
        )
        # print(message.status)


#use python anywhere to run it daily/automatically once per day.