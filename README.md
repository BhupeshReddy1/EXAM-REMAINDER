# EXAM-REMAINDER
#DESCRIPTION:
-
This project is used to automatically remind The PRINCIPAL about examinations one week prior to original schedule.
This is designed to automate the process of sending timely alerts via email and SMS to officers based on events specified in uploaded Excel files. Users can securely log in to the system. The alert message can be sent using email(ASSUMING INTERNET) or can be sent to their mobile number(Via SMS). Users can securely log in to the system, upload officer details and timesheet files, and specify a reference date (t). The application processes these files to identify events occurring at specified intervals relative to t (e.g., t-5, t-2). It then calculates the actual dates for these events and sends personalized alerts to the relevant officers 7 days before each event. The system includes robust user authentication, secure password management, session handling, and cache control , thereby ensuring secure and efficient communication of critical information. I am using pythonanywhere as a cloud service which runs the program daily at our given time.
Main advantage of my project is that it doesnt need a real app since everything can be done using APIs.

STEPS TO SETUP THIS APPLICATION:
-
1. Create a virtual environment for flask application.
2. First make sure to create a twilio account(https://www.twilio.com/en-us) and enter the corresponding account_sid, auth_token in main.py file.
3. Create a .env file with the following details ""from_mail=your_gmail_address@gmail.com app_pass=your_app_password""(create a app password from your email security settings).
4. Run the application

LOGIN
-
-> Login

-> Navigate to the login page.

-> Enter the username and password as specified in dir_details.xlsx.

UPLOAD FILES
 -  
-> Go to the file upload page after logging in.

-> Select and upload the officer details file (.xlsx) and the timesheet file (.xlsx).

-> Enter the reference date in dd-mm-yyyy format to update the timesheets.

-> Click the upload button.

SEND ALERTS
-
-> Go to the alerts page.

-> If valid timesheet and officer files are available, alerts will be sent automatically.

-> You will receive a message indicating the status of the alerts.

CHANGE PASSWORD
-
-> Navigate to the change password page.

-> Enter your old password, new password, and confirm the new password.

-> Click the change password button to update your password.

LOGOUT
-
Click the logout button to end your session.
