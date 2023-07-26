import os
import smtplib
import datetime as dt
import random
import pandas as pd
import numpy as np
from dotenv import load_dotenv
load_dotenv()
current= dt.datetime.now()
current_tuple=(current.month, current.day)
# year=current.year
# print(year)
# can print day of the week, where 0 means monday. 1 means tuesday and so on

my_email=os.environ.get("from_mail")
app_password=os.environ.get("to_mail")

data=pd.read_csv("exams.csv")

p=data['date']
r=data['month']
date_array = p.to_numpy()
month_array = r.to_numpy()
#check month since they have 30/31/28 days depending on month. this way message pops up only before 7days irrespective of total no of days
for i in range(len(date_array)):
    if date_array[i]>7:
        date_array[i] -= 7
    elif date_array[i] < 7:
        if month_array[i] == 1 or month_array[i]==2 or month_array[i] == 4 or month_array[i] == 6 or month_array[i]== 8 or month_array[i]== 9 or month_array[i]== 11:
            date_array[i] += 24
            month_array[i]-= 1
        elif month_array[i] == 5 or month_array[i]== 7 or month_array[i]== 10 or month_array[i]== 12:
            date_array[i] += 23
            month_array[i] -= 1
        elif month_array[i]==3:
            date_array[i] += 21
            month_array[i] -= 1

exam_dict={(data_row["month"], data_row["date"]): data_row for (index,data_row) in data.iterrows()}

if current_tuple in exam_dict:
    exam_students=exam_dict[current_tuple]
    # letter_r=random.randint(1,3)
    file_path="new_data.csv"
#print(birthday_person)
    with open(file_path) as f:
        contents=f.read()
        #checking if it is end of the month or not and also changing dates back to normal
        if exam_students['date']>24 and (exam_students['month']==1 or exam_students['month']==3 or exam_students['month']==5
                                         or exam_students['month']==7 or exam_students['month']==8 or exam_students['month']==10 or exam_students['month']==12):
            exam_students["date"]=exam_students["date"]-24
            exam_students["month"]+=1
        elif exam_students['date']>23 and (exam_students['month']==4 or exam_students['month']==6 or exam_students['month']==9 or exam_students['month']==11):
            exam_students['date']=exam_students['date']-23
            exam_students['month']+=1
        elif exam_students['date']>21 and exam_students['month']==2:
            exam_students['month']+=1
            exam_students['date']=exam_students['date']-21
        else:
            exam_students['date']+=7
        contents=contents.replace("[Year]", str(exam_students["course_year"]))
        contents = contents.replace("[Number]", str(exam_students["sem"]))
        contents = contents.replace("[Date]", str(exam_students["date"]))
        contents = contents.replace("[Month]", str(exam_students["month"]))
        
        #print(contents)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                                to_addrs=os.environ.get("to_mail"),
                                msg=f"Subject:Hello\n\n{contents}")



