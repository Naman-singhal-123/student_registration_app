import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import font as tkFont
######### Thanks page ###############
class thankspage:
    def __init__(self,master1):
        self.master1=master1
        screen_width=master1.winfo_screenwidth()
        screen_height=master1.winfo_screenheight()
        master1.geometry(f"{screen_width}x{screen_height}")
        master1.resizable(True,False)
        master1.title("Thanks for registration")

        # background()
        try:
            self.bg_img = Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/thanks2.jpg")
            self.bg_img_resized = ImageTk.PhotoImage(self.bg_img.resize((2000,860)))
            bg_label = Label(master1, image=self.bg_img_resized)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Background not loaded:", e)
        def website():
           webbrowser.open_new("https://www.mlncollegeynr.ac.in")
           print("mission sucessful")
        def exists():
            master1.destroy()
            print("mission sucessful")
        
    #button wisit website()
        custom_font=tkFont.Font(family="Arial",size=15,weight="bold",slant="roman")
        Thanks=tk.Button(master1, text="Click FOR website", font=custom_font, fg="black",borderwidth=12,bg="#4CAF50",cursor="hand2",command=website).place(x=950, y=600)
        # exit button
        exits=tk.Button(master1,text="Click For Exit",font=custom_font,fg="black",borderwidth=12,bg="#4CAF50",cursor="hand2",command=exists).place(x=950,y=677)
        

# -------- STUDENT REGISTRATION FORM --------
class StudentRegistrationApp:
    def __init__(self, master):
        
        self.master = master
        screen_width=master.winfo_screenwidth()
        screen_height=master.winfo_screenheight()
        master.geometry(f"{screen_width}x{screen_height}")
        master.resizable(True,False)
        master.title("Student Registration")
        # Background
        try:
            self.bg_img = Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/dark.jpg")
            self.bg_img_resized = ImageTk.PhotoImage(self.bg_img.resize((1640,1000)))
            bg_label = Label(master, image=self.bg_img_resized)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Background not loaded:", e)

        # Title
        Label(master, text="STUDENT REGISTRATION FORM", bg="#0096DC", fg="black", font=("Helvetica", 33)).pack()

        # Student Images
        try:
            img1 = Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/students.jpg").resize((200, 200))
            self.tk_img1 = ImageTk.PhotoImage(img1)
            img_label1 = Label(master, image=self.tk_img1)
            img_label1.place(x=260, y=80)
        except Exception as e:
            print("Image 1 not found:", e)

        try:
            img2 = Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/mukund.jpg").resize((200, 200))
            self.tk_img2 = ImageTk.PhotoImage(img2)
            img_label2 = Label(master, image=self.tk_img2)
            img_label2.place(x=600, y=80)
        except Exception as e:
            print("Image 2 not found:", e)

        try:
            img3 = Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/girlsstudents.jpg").resize((200, 200))
            self.tk_img3 = ImageTk.PhotoImage(img3)
            img_label3 = Label(master, image=self.tk_img3)
            img_label3.place(x=1000, y=80)
        except Exception as e:
            print("Image 3 not found:", e)

        #frame 1
        Label(master, text="First Name", font="45", fg="black", bg="white").place(x=300,y=320,anchor="center")
        # frame2
        Label(master, text="Last Name", font="45", fg="black", bg="white").place(x=890, y=300)
        #frame3
        Label(master,text="D-O-B",font="45",fg="black",bg="white").place(x=320,y=400,anchor="center")
        #frame4
        Label(master,text="Father Name",font="45",fg="black",bg="white").place(x=930,y=400,anchor="center")
        #frame 5
        Label(master,text="12th Marks",font="45",fg="black",bg="white").place(x=305,y=475,anchor="center")
        #frame 6
        Label(master,text="Country",font="45",fg="black",bg="white").place(x=950,y=475,anchor="center")
        #frame 7
        Label(master,text="District",font="45",fg="black",bg="white").place(x=320,y=560,anchor="center")
        #frame 8
        Label(master,text="Pin-Code",font="45",fg="black",bg="white").place(x=940,y=560,anchor="center")
        #frame 9
        COURSE=Label(master,text="Choose_Course",font="45",fg="black",bg="white").place(x=280,y=630,anchor="center")
        # Entry 1
        # Entry 1
        self.name_entry = Entry(master, font="10", bd=4,relief=SOLID)
        self.name_entry.place(x=400, y=300)
        # Entry2
        self.last_name = Entry(master, font="7", bd=4,relief=SOLID)
        self.last_name.place(x=1030, y=300)
        #Entry3
        self.dob_entry = Entry(master, font="10", bd=4,relief=SOLID)
        self.dob_entry.place(x=400, y=380)
        #Entry4
        self.Father_name=Entry(master,font="10",bd=4,relief=SOLID)
        self.Father_name.place(x=1030,y=380)
        #Entry5
        self.marks=Entry(master,font="10",bd=4,relief=SOLID)
        self.marks.place(x=400,y=457)
        #Entry 6
        self. country=Entry(master,font="10",bd=4,relief=SOLID)
        self.country.place(x=1030,y=457)
        #Entry 7
        self.district=Entry(master,font="10",bd=4,relief=SOLID)
        self.district.place(x=400,y=540)
        # Entry 8
        self.pincode=Entry(master,font="10",bd=4,relief=SOLID)
        self.pincode.place(x=1030,y=540)
        ############################## radio button ###############
        # Course Radio Buttons
        self.course_var = IntVar()
        self.course_var.set(1)
        courses = [
            ("Bachelor of Computer Application", 1, 435, 620),
            ("Bachelor of Business Administration", 2, 435, 660),
            ("Bachelor of Arts", 3, 850, 620),
            ("Bachelor of Science with CS", 4, 1130, 620),
            ("Bachelor of Education", 5, 850, 660),
            ("Bachelor of Science with IT", 6, 1130, 660)
        ]
        for text, val, x, y in courses:
            tk.Radiobutton(master, text=text, font=12,variable=self.course_var, value=val).place(x=x, y=y)
            tk.Radiobutton(master,text="this is inform to you all the information are submitted to mukund lal national college Haryana",font="1",variable=self.course_var,value=val).place(x=220,y=720)
        ############## submit button #################
        Button(master, text="Submit", font="12", bg="#4CAF50", command=self.details).place(x=1130, y=710)
        ############### clear button #################
        Button(master, text="Clear", font="12", bg="#f44336", command=self.clear).place(x=1265, y=710)

    def details(self):
          import mysql.connector as m
          db=m.connect(host="localhost",user="root",password="ROOT",database="student_registration")
          mycursor=db.cursor()
          nam=self.name_entry.get()
          dob=self.dob_entry.get()
          mark=self.marks.get()
          dis=self.district.get()
          father=self.Father_name.get()
          count=self.country.get()
          last=self.last_name.get()
          pin=self.pincode.get()
          if nam=="":
            messagebox.showerror("Error Generate", "ALL Field Requires to fill")
          elif dob=="":
            messagebox.showerror("Error Generate", "ALL Field Requires to fill")
          elif mark=="":
            messagebox.showerror("Error Generate", "ALL Field Requires to fill")
          elif dis=="":
            messagebox.showerror("Error Generate", "ALL Field Requires to fill")
          elif father=="":
            messagebox.showerror("Error Generate", "ALL Field Requires to fill")
          elif count=="":
            messagebox.showerror("Error Generate", "ALL Field Requires to fill")
          elif last=="":
            messagebox.showerror("Error Generate", "ALL Field Requires to fill")
          elif pin=="":
            messagebox.showerror("Error Generate", "ALL Field Requires to fill")
          elif  mark.isalpha():#and pin.isalpha:
              messagebox.showerror("NUMERIC value","please enter the numeric value of MARKS")
             # marks.delete(0,END)
          elif pin.isalpha():
              messagebox.showerror("NUMERIC VALUE","please enter the numeric value pf PINCODE")
              #pincode.delete(0,END)
          else:
             l=[]
             l.append([nam,dob,mark,dis,father,count,last,pin])
             print(l)
             z="insert into student_registration_details(First_Name,date_of_birth,Marks,Districts,Father_name,Country_name,Last_name,pin_codes)values(%s,%s,%s,%s,%s,%s,%s,%s)"
             data=(nam,dob,mark,dis,father,count,last,pin)
             mycursor.execute(z,data)
             db.commit()
             print("data sucessfully going on database")
             ## after input data deleted
             self.name_entry.delete(0,END)
             self.dob_entry.delete(0,END)
             self.marks.delete(0,END)
             self.district.delete(0,END)
             self.Father_name.delete(0,END)
             self.pincode.delete(0,END)
             self.last_name.delete(0,END)
             self.country.delete(0,END)
             messagebox.showinfo("Thanks for submission", "YOUR Registration details has been submitted, MLN team contact you soon thanks !...")
             self.master.destroy()
             done_page()
    def clear(self):
        confirm = messagebox.askyesno("Confirm", "Do you want to clear the form?")
        if confirm:
            self.name_entry.delete(0, END)
            self.last_name.delete(0, END)
            self.dob_entry.delete(0, END)
            self.Father_name.delete(0, END)
            self.marks.delete(0, END)
            self.country.delete(0, END)
            self.district.delete(0, END)
            self.pincode.delete(0, END)
            

# -------- LOGIN PAGE --------
def show_login():
    login_win = tk.Tk()
    login_win.title("Student Authentication")
    screen_width=login_win.winfo_screenwidth()
    screen_height=login_win.winfo_screenheight()
    login_win.geometry(f"{screen_width}x{screen_height}")
    login_win.resizable(True,True)

    try:
        original_img = Image.open(r"C:\Users\hp\OneDrive\Desktop\studentapp\cloud blue.jpg") # r laga sa
        resized = original_img.resize((1640,1000)) # back slash ki direction change karna ki need nahi hai
        bg_img = ImageTk.PhotoImage(resized)
        bg_label = Label(login_win, image=bg_img)
        bg_label.image = bg_img
        bg_label.place(x=0, y=0, relheight=1, relwidth=1)
    except Exception as e:
        print("Login background error:", e)

    Label(login_win, text="STUDENT AUTHENTICATION PROCESS", fg="black", bg="yellow", font=("Helvetica", 25)).pack()

    try:
        auth_img = Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/verify.jpg")
        resized_auth = auth_img.resize((160, 160))
        auth_photo = ImageTk.PhotoImage(resized_auth)
        img_label = Label(login_win, image=auth_photo)
        img_label.image = auth_photo
        img_label.place(x=630,y=60) #shakal

        lockimg = Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/lock.jpg")
        resized_lock = lockimg.resize((160, 160))
        lock_photo = ImageTk.PhotoImage(resized_lock)
        img_label = Label(login_win, image=lock_photo)
        img_label.image = lock_photo
        img_label.place(x=1100,y=60) #lock

        lockimg2 = Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/login1.jpg")
        resized_lock2 = lockimg2.resize((80, 80))
        lock_photo2 = ImageTk.PhotoImage(resized_lock2)
        img_label = Label(login_win, image=lock_photo2)
        img_label.image = lock_photo2
        img_label.place(x=430, y=570)

        lockimg3=Image.open("C:/Users/hp/OneDrive/Desktop/studentapp/auth.jpg")
        resized_lock3 = lockimg3.resize((160, 160))
        lock_photo3 = ImageTk.PhotoImage(resized_lock3)
        img_label = Label(login_win, image=lock_photo3)
        img_label.image = lock_photo3#gola
        img_label.place(x=150,y=60)



    except Exception as e:
        print("Login image error:", e)

    Label(login_win, text="Username",font=("Arial",24),fg="black", bg="White").place(relx=0.3, rely=0.4, anchor="center")
    # frame2
    Label(login_win, text="E-mail", font=("Arial",24),fg="black", bg="white").place(relx=0.3, rely=0.5, anchor="center")
    # frame3
    Label(login_win, text="Password", font=("Arial",24), fg="black", bg="white").place(relx=0.3, rely=0.6, anchor="center")
    # Entry 1
    username_entry = Entry(login_win, font="10", bd=4,relief=SOLID)
    username_entry.place(x=620, y=408)
    # Entry2
    Email_name = Entry(login_win, font="10", bd=4,relief=SOLID)
    Email_name.place(x=620, y=320)
    # Entry3
    password_name = Entry(login_win, font="10", bd=4,show="*",relief=SOLID)
    password_name.place(x=620, y=491)

    # login

    def clear_fields():
        result=messagebox.askyesno("Confirm", "Do you want to deleted your log in details")
        if result:
          username_entry.delete(0, END)
          Email_name.delete(0, END)
          password_name.delete(0, END)
          messagebox.showinfo("Deleted", "Your login details have been deleted!")
        else:
            pass
    def login():
        import mysql.connector as m
        db=m.connect(host="localhost",user="root",password="ROOT",database="student_registration")
        mycursor=db.cursor()
        uname = username_entry.get()
        email = Email_name.get()
        pwd = password_name.get()
        if uname and email and pwd:
            Result=messagebox.askyesno("Confirm", "Do you want to take Admisssion in Mukund lal college, Haryana")
            if Result:
               l=[]
               l.append([uname,email,pwd])
               print(l)
               z="insert into privacy(username,E_mail,Password)values(%s,%s,%s)"
               data=(uname,email,pwd)
               mycursor.execute(z,data)
               login_win.destroy()
               db.commit()
               print("data transfer sucessfully")
               open_registration_form()
            else:
                messagebox.showerror("Login Fast",f"please log in fast {uname}!")
        else:
            messagebox.showerror("Login Failed", "All fields are required.")

    Button(login_win, text="Log In", font="12", bg="#4CAF50", command=login).place(x=600, y=600)
    Button(login_win, text="Clear", font="12", bg="#f44336", command=clear_fields).place(x=750, y=600)

    Label(login_win, text="Made by: Naman Singhal", font=("Arial", 24, "bold"), fg="black", bg="white").place(relx=0.6, rely=0.9, anchor="se")
    login_win.mainloop()

def done_page():
    reg_win1=tk.Tk()
    thanks=thankspage(reg_win1)
    reg_win1.mainloop()
    
def open_registration_form():
    reg_win = tk.Tk()
    app = StudentRegistrationApp(reg_win)
    reg_win.mainloop()
show_login()


# --- START THE APP ---
#show_login()
