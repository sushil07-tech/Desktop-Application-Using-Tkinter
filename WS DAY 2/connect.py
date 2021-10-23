# from tkinter import *
# import mysql.connector
# import tkinter.messagebox as m
# import smtplib
# from email.mime.text import MIMEText
# import random
 

# mainWindow = Tk() #initialize
# mainWindow.title("Login & Registration")
# mainWindow.geometry("400x400")
# mainWindow.config(background="#0D4F8B")

# bigText = Label(text="Welcome to ISA-VESIT",bg="#0D4F8B",fg="white", font="Verdana 20 bold")
# bigText.place(x=30,y=30)
# #register function
# def Register():
#     registerWindow = Tk()
#     registerWindow.title("Register")
#     registerWindow.geometry("400x400")
#     registerWindow.config(background="#0D4F8B")

#     mainWindow.destroy()
#     #for connecting database
#     con = mysql.connector.connect(host="localhost", user="root",passwd="password", database="person") 
#     cursor = con.cursor()
    
#     bigText1 = Label(registerWindow,text="Registration",bg="#0D4F8B",fg="white", font="Verdana 20 bold")
#     bigText1.place(x=120,y=50)

#     username = Label(registerWindow,text="Username:",bg="#0D4F8B",fg="white", font="poppins 12 bold")
#     username.place(x=50,y=120)

#     email = Label(registerWindow,text="Email:",bg="#0D4F8B",fg="white", font="poppins 12 bold")
#     email.place(x=50,y=170)

#     password = Label(registerWindow,text="Password:",bg="#0D4F8B",fg="white", font="poppins 12 bold")
#     password.place(x=50,y=220)

#     confirmpassword = Label(registerWindow,text="Confirm \n Password:",bg="#0D4F8B",fg="white", font="poppins 12 bold")
#     confirmpassword.place(x=50,y=270)

#     e1 = Entry(registerWindow, font="poppins 12 bold")
#     e1.place(x=150,y=120)

#     e2 = Entry(registerWindow, font="poppins 12 bold")
#     e2.place(x=150,y=170)

#     e3 = Entry(registerWindow,show="*", font="poppins 12 bold")
#     e3.place(x=150,y=220)

#     e4 = Entry(registerWindow,show="*", font="poppins 12 bold")
#     e4.place(x=150,y=270)

#     def error():
#         m.showerror(title="Error", message="Password not same")

#     def insert():
#         insert = ("insert into student (name,email,password,confirmpassword) value(%s,%s,%s,%s)")
#         values = [e1.get(),e2.get(),e3.get(),e4.get()]
#         cursor.execute(insert,values)
#         if e3.get() == e4.get():
#             con.commit()
#             sendmail()
#         else:
#             error()
#     btnregister = Button(registerWindow,text="Register",bg='#C6E2FF',width=10,font="poppins 12 bold")
#     btnregister.place(x=150,y=340)

#     btnlogin = Button(registerWindow,text="Login",bg='#C6E2FF',width=7,font="poppins 12 bold")
#     btnlogin.place(x=30,y=10) 

#     btnexit = Button(registerWindow,text="Exit",bg='red',width=7,fg='white',font="poppins 12 bold", command=registerWindow.destroy)
#     btnexit.place(x=280,y=10)

#     def sendmail():
#         sendWindow = Tk()
#         sendWindow.title("Verify Email")
#         sendWindow.geometry("400x400")
#         sendWindow.config(background="#0D4F8B")

#         con1 = mysql.connector.connect(host="localhost", user="root",passwd="password", database="person")
#         cursor1 = con1.cursor()

#         def generateOTP():
#             otp = str(random.randint(1000,9999))
#              #	Generate random floating numbers
            
#             insertotp = ("insert into otp (otp) value(%s)")
#             valuesotp = [otp]
#             cursor1.execute(insertotp,valuesotp)
#             con1.commit()
#             body = otp
#             msg = MIMEText(body)
#             #Multipurpose Internet Mail Extensions
#             fromaddr='sender email Id'
#             toaddr = e5.get()
#             msg['From']=fromaddr
#             msg['To']=toaddr
#             msg['subject']="OTP"

#             server=smtplib.SMTP('smtp.gmail.com',587)
#             server.starttls()
#             server.login(fromaddr,'Sender Email password')

#             server.send_message(msg)
#             m.showinfo(title="Done",message="Mail sent to your email ID")
#             server.quit()

#         def verify():
#             sql_select_Query = "SELECT * FROM otp WHERE id=(SELECT MAX(id) FROM otp)"
#             cursor1.execute(sql_select_Query)
#             records = []
#             records = cursor1.fetchall()
#             c = records[-1][-1]
#             b = e6.get()
#             if  c == b:
#                 m.showinfo(title="Done",message="Email Verified You can login")
#                 sendWindow.destroy()
#             else:
#                 m.showinfo(title="Error",message="OTP not match")
                
#         bigText1 = Label(sendWindow,text="Verify Email", bg="#0D4F8B",fg="white", font="Verdana 20 bold")
#         bigText1.place(x=100,y=50)

#         sendemail = Label(sendWindow,text="Email:",bg="#0D4F8B",fg="white", font="poppins 12 bold")
#         sendemail.place(x=50,y=120)

#         e5 = Entry(sendWindow, font="poppins 12 bold")
#         e5.place(x=150,y=120)
        
#         verifyotp = Label(sendWindow,text="OTP:",bg="#0D4F8B",fg="white", font="poppins 12 bold")
#         verifyotp.place(x=50,y=220)

#         e6 = Entry(sendWindow, font="poppins 14 bold")
#         e6.place(x=150,y=220)
        
#         btnmail = Button(sendWindow,text="Send OTP",bg='#C6E2FF',width=10,font="poppins 12 bold")
#         btnmail.place(x=170,y=170)

#         btnotp = Button(sendWindow,text="Verify OTP",bg='#C6E2FF',width=10,font="poppins 12 bold")
#         btnotp.place(x=170,y=270)
   
# def Login():
#     loginWindow = Tk()
#     loginWindow.title("Login")
#     loginWindow.geometry("400x400")
#     loginWindow.config(background="#0D4F8B")

#     bigText1 = Label(loginWindow,text="Login",bg="#0D4F8B",fg="white", font="poppins 20 bold")
#     bigText1.place(x=140,y=50)

#     email = Label(loginWindow,text="Email:",bg="#0D4F8B",fg="white", font="poppins 14 bold")
#     email.place(x=40,y=160)

#     password = Label(loginWindow,text="Password:",bg="#0D4F8B",fg="white", font="poppins 14 bold")
#     password.place(x=40,y=210)

#     e1 = Entry(loginWindow, font="poppins 14 bold")
#     e1.place(x=150,y=162)

#     e2 = Entry(loginWindow,show="*", font="poppins 14 bold")
#     e2.place(x=150,y=212)

#     def check():
#         con1 = mysql.connector.connect(host="localhost", user="root",passwd="Asmita@01", database="person")
#         cursor1 = con1.cursor()
#         con2 = mysql.connector.connect(host="localhost", user="root",passwd="Asmita@01", database="person")
#         cursor2 = con2.cursor()
#         cursor1.execute("select email from student")
#         cursor2.execute("select password from student")

#         email = e1.get()
#         password = e2.get()
#         e = []
#         p = []
#         for i in cursor1:
#             e.append(i)
#         for j in cursor2:
#             p.append(j)

#         k = len(e)
#         i = 0
#         while i<k:
#             if e[i][0] == email and p[i][0] == password:
#                 m.showinfo(title="Done",message="Login Is Done")
#                 break
#             i += 1
#         else:
#             m.showerror(title="Error",message="Something went wrong")

#     login = Button(loginWindow,text="Login",bg='#C6E2FF',width=10,font="poppins 12 bold")
#     login.place(x=170,y=280)

#     btnexit = Button(loginWindow,text="Exit",bg='red',width=7,fg='white',font="poppins 12 bold",command=loginWindow.destroy)
#     btnexit.place(x=250,y=350)

# btnstart = Button(mainWindow, text="Let's Start",bg='#C6E2FF',width=8,font="poppins 12 bold")
# btnstart.place(x=150,y=190)

# btnExit = Button(mainWindow,text="Exit",bg='red',width=7,fg='white',font="poppins 12 bold", command=mainWindow.destroy)
# btnExit.place(x=250,y=320)

# mainloop()
