import os
import smtplib
import datetime as dt
import random
import pandas as pd
import numpy as np
current= dt.datetime.now()
current_tuple=(current.month, current.day)
# year=current.year
# print(year)
# can print day of the week, where 0 means monday. 1 means tuesday and so on

my_email=os.environ['from_mail']
app_password="jdtkyjnhuikjthgr"

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
    # letter_r=random.randint(1,3)
    file_path="new_data.csv"
#print(birthday_person)
    with open(file_path) as f:
        contents=f.read()
        #checking if it is end of the month or not
        if exam_students['date']>23:
            exam_students["date"]=exam_students["date"]-23
            exam_students["month"]+=1
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
                                to_addrs=os.environ['to_mail'],
                                msg=f"Subject:Hello\n\n{contents}")


