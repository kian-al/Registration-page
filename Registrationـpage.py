import mysql.connector
import re
from colorama import Fore
cnx=mysql.connector.connect(user='kian', password='Kian.py192',host='127.0.0.1', database='email') #If you want to use this code, enter your database information in this line
cursor=cnx.cursor()
email_result=False
email_pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email_domain_pattern=["gmail.com","yahoo.com","hotmail.com","outlook.com","live.com","aol.com","icloud.com","me.com","protonmail.com","zoho.com"]
while not email_result:
    input_email=input("please enter the email address :")
    if re.match(email_pattern,input_email):
        input_email_separate=input_email.split("@")[1]
        input_email_separate2=input_email_separate.split(".")[1]            
        if input_email_separate in email_domain_pattern:
            if input_email_separate2=="com":
                email_result=True
    else:
        print("Invalid email address format! Please try again.")
password_result=False
while not password_result:
    input_password=input("please enter the email address password :")
    if len(input_password) < 8:
        print("Password must be at least 8 characters long! Please try again.")
    elif not any(char.isalpha() for char in input_password):
        print("Password must contain at least one letter! Please try again.")
    elif not any(char.isdigit() for char in input_password):
        print("Password must contain at least one digit! Please try again.")
    else:
        password_result = True
query_login="INSERT INTO info (email,password) VALUES (%s,%s);"
cursor.execute(query_login,(input_email,input_password))
cnx.commit()
query_result="SELECT * FROM info;"
cursor.execute(query_result)
result=cursor.fetchall()

for email,password in result:
    print(Fore.GREEN+"this is your email","\t"+Fore.WHITE+email , Fore.GREEN+"\t" ,"and this is your email passeord","\t"+Fore.WHITE+password)
cursor.close()
cnx.close()




