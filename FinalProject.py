import pyttsx3
import smtplib
import time
import datetime
import speech_recognition as sr
email=""
c=0
message=""
engine=pyttsx3.init()
engine.setProperty('rate',100)
print("Hello boss")
engine.say("Hello boss")
time.sleep(1)
print("How may i help you sir !!")
engine.say("How may i help you sir !!")
engine.runAndWait()
data=""
r=sr.Recognizer()
with sr.Microphone() as source:
    def s1(txt):
        engine=pyttsx3.init()
        engine.setProperty('rate',100)
        engine.say(txt)
        engine.runAndWait()
def r1():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now")
        audio=r.listen(source)
        
    try:
        data=r.recognize_google(audio)
        
        print("You said: ",data)

    except sr.UnknownValueError:
        print("Audio is not recognizable")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service")
    return data
data=r1()
def check(d):
    print("please enter the email address of reciever")
    s1("please enter the email address of reciever")
    email=r1()
    print("email recognition complete")
    s1("email recognition complete")
    print("what was the message boss")
    s1("what was the message boss")
    message=r1()
    print("Message recorded successfully")
    s1("Message recorded successfully")
    yield email
    yield message

server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
try:
    server.login("9793anjalraj@gmail.com","*******")
    print('Login is done,you can now send emails')
    s1("Login is done,you can now send emails")
except smtplib.SMTPHeloError:
    print('The server responded weird stuff to my login request,please try again')
except smtplib.SMTPAuthenticationError:
    print('Your account name or password is incorrect,please try again using the correct stuff')
except smtplib.SMTPException:
    print('SMTP Error')
print("Data:",data)
if(data=="send mail"):
        y=check(data)
try:
    time.sleep(1)
    email=y.__next__()
    email=email.lower()
    s_email=""
    for s in email:
        if(s!=' '):
            s_email=s_email+s
    print("Email:",s_email)
    print("Message:")
    print("At what time you want to send mail !! Make sure that timing is in minute ")
    s1("At what time you want to send mail !! Make sure that timing is in minute")
    m=r1()
    current=datetime.datetime.now()
    while(True):
        if(current.now().minute==int(m)):
            server.sendmail("9793anjalraj@gmail.com",s_email,y.__next__())
            print("Mail Sent")
            s1("Mail Sent")
            c=c+1
            break
except:
    print("error")
    s1("error")
server.quit()
        

