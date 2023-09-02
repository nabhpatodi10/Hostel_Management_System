import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import datetime
from time import strftime
import pickle

def db_func():

    cursor.execute("create database if not exists hostel_management")
    db_connection.commit()

    cursor.execute("use hostel_management")

    cursor.execute("create table if not exists login (Name varchar(30) not null, Username varchar(20) not null, Passwrd varchar(20) not null, Access varchar(20) not null)")
    db_connection.commit()

    cursor.execute("create table if not exists student_info (Name varchar(30), DOB varchar(50), Mobile_No varchar(15), Permanent_Address varchar(150), Educational_Qualification varchar(100), Educational_Institution_or_Working_Place varchar(200),  Blood_Group varchar(5), Medical_Condition varchar(500), Father_Name varchar(30), Father_Mob_No varchar(15), Father_Occupation varchar(100), Father_Office varchar(150), Mother_Name varchar(30), Mother_Mob_No varchar(15), Mother_Occupation varchar(100), Mother_Office varchar(150), L_G_Name varchar(30), L_G_Mob_No varchar(15), L_G_Address varchar(150), L_G_Occupation varchar(100), Entry_Date varchar(50))")
    db_connection.commit()

    cursor.execute("create table if not exists fee_info (Name varchar(30), Mobile_No varchar(15), Registration_Fee varchar(10), Caution_Money varchar(10), Monthly_Fee varchar(10))")
    db_connection.commit()

    cursor.execute("create table if not exists fee_stats (Name varchar(30), Mobile_No varchar(15), Month varchar(10), Year varchar(5), Paid_On varchar(10))")
    db_connection.commit()

    cursor.execute("create table if not exists monthly_total_fee (Month varchar(10), Year varchar(5), Total_Fee varchar(20))")
    db_connection.commit()

    cursor.execute("create table if not exists rooms (Name varchar(30), Mobile_No varchar(15), Room_No varchar(5), Bed_No varchar(2))")
    db_connection.commit()

    cursor.execute("create table if not exists expenses (Month varchar(10), Year varchar(5), Category varchar(50), Amount varchar(15))")
    db_connection.commit()

    def new_user_create():
        cursor.execute("select * from login")
        data_list=cursor.fetchall()

        root_new=Tk()
        root_new.title("Dream Catcher Girl's Hostel")
        root_new.state("zoomed")
        root_new.iconbitmap("Images/Logo_3.ico")
        root_new.configure(background="#ffedf3")

        new_name_var=StringVar()
        new_user_var=StringVar()
        new_pass_var=StringVar()
        new_access_var=StringVar()

        new_photo_label=Label(root_new, background="#ffedf3")
        class Example(Frame):
            def __init__(self, master, *pargs):
                Frame.__init__(self, master, *pargs)

                self.image = Image.open("Images/Logo_2.png")
                self.img_copy= self.image.copy()

                self.background_image = ImageTk.PhotoImage(self.image)

                self.background = Label(self, image=self.background_image)
                self.background.pack(fill=BOTH, expand=YES)
                self.background.bind('<Configure>', self._resize_image)

            def _resize_image(self,event):

                new_width = event.width
                new_height = event.height

                self.image = self.img_copy.resize((new_width, new_height))

                self.background_image = ImageTk.PhotoImage(self.image)
                self.background.configure(image =  self.background_image)

        e = Example(new_photo_label)
        e.pack(fill=BOTH, expand=YES)
        new_photo_label.place(relx=0.375, rely=0.05, relheight=0.4, relwidth=0.285)

        def add_user_func():
            if new_name_var.get()!="" and new_user_var.get()!="" and new_pass_var.get()!="":
                for i in data_list:
                    if i[0]==new_name_var.get() and i[1]==new_user_var.get() and i[2]==new_pass_var.get():
                        new_condition_label.configure(text="User Already Exists!", foreground="Red")
                        new_condition_label.place(relx=0.443, rely=0.82)
                        break
                else:
                    try:
                        cursor.execute(f"insert into login values ('{new_name_var.get()}', '{new_user_var.get()}', '{new_pass_var.get()}', '{new_access_var.get().lower()}');")
                        db_connection.commit()
                    except:
                        new_condition_label.configure(text="Error! Please Enter Valid Data", foreground="Red")
                        new_condition_label.place(relx=0.412, rely=0.82)
                    root_new.destroy()
                    main_function()
            else:
                    new_condition_label.configure(text="Error! Please Enter Valid Data", foreground="Red")
                    new_condition_label.place(relx=0.412, rely=0.82)

        new_name_label=Label(root_new, background="#ffedf3", text="Full Name:", font=("Haettenschweiler", 25), foreground="#811c98")
        new_name_label.place(relx=0.39, rely=0.5)
        new_name_entry=Entry(root_new,textvariable=new_name_var , background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", width=20)
        new_name_entry.place(relx=0.465, rely=0.5, relheight=0.045)
        new_user_label=Label(root_new, background="#ffedf3", text="Username:", font=("Haettenschweiler", 25), foreground="#811c98")
        new_user_label.place(relx=0.39, rely=0.55)
        new_user_entry=Entry(root_new,textvariable=new_user_var , background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", width=20)
        new_user_entry.place(relx=0.465, rely=0.55, relheight=0.045)
        new_pass_label=Label(root_new, background="#ffedf3", text="Password:", font=("Haettenschweiler", 25), foreground="#811c98")
        new_pass_label.place(relx=0.39, rely=0.6)
        new_pass_entry=Entry(root_new,textvariable=new_pass_var , background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", width=20, show="*")
        new_pass_entry.place(relx=0.465, rely=0.6, relheight=0.045)

        rest_access=Radiobutton(root_new, text="Restricted Access", value="Restricted Access", variable=new_access_var, background="#ffedf3", font=("Haettenschweiler", 20), foreground="#811c98")
        unrest_access=Radiobutton(root_new, text="Unrestricted Access", value="Unrestricted Access", variable=new_access_var, background="#ffedf3", font=("Haettenschweiler", 20), foreground="#811c98")
        new_access_var.set("Restricted Access")
        rest_access.place(relx=0.38, rely=0.67)
        unrest_access.place(relx=0.505, rely=0.67)

        new_condition_label=Label(root_new, background="#ffedf3", font=("Haettenschweiler", 25))

        add_button=Button(root_new, text="Add New User", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", command=add_user_func, activebackground="#811c98", activeforeground="#ffedf3")
        add_button.place(relx=0.46, rely=0.75, relheight=0.06)

        root_new.mainloop()

    def main_function():

        cursor.execute("select * from login")
        login_data=cursor.fetchall()

        if len(login_data)==0:

            new_user_create()

        else:

            root_login=Tk()
            root_login.title("Dream Catcher Girl's Hostel")
            root_login.state("zoomed")
            root_login.iconbitmap("Images/Logo_3.ico")
            root_login.configure(background="#ffedf3")

            user_var=StringVar()
            pass_var=StringVar()

            def login_function():

                for i in login_data:

                    if user_var.get()==i[1] and pass_var.get()==i[2]:

                        login_condition_label.configure(text="Access Granted!", foreground="Green")
                        root_login.destroy()

                        if i[3]=="unrestricted access":
                            
                            main_root=Tk()
                            main_root.title("Dream Catcher Girl's Hostel")
                            main_root.state("zoomed")
                            main_root.iconbitmap("Images/Logo_3.ico")
                            main_root.configure(background="#ffedf3")

                            month_dict={1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
                            room_dict={301:["A", "B", "C"], 302:["A", "B", "C"], 303:["A", "B", "C"], 304:["A", "B", "C"], 305:["A", "B", "C"], 306:["A", "B", "C"], 307:["A", "B", "C", "D"],
                            401:["A", "B", "C"], 402:["A", "B"], 403:["A", "B"], 404:["A", "B"], 405:["A", "B", "C", "D"], 406:["A", "B", "C", "D"], 407:["A", "B", "C"], 408:["A", "B", "C"],
                            409:["A", "B", "C"], 410:["A", "B", "C"], 411:["A", "B"], 412:["A", "B"], 413:["A", "B"], 414:["A", "B"], 415:["A", "B", "C"], 416:["A", "B", "C"], 417:["A", "B", "C"],
                            418:["A", "B", "C"], 419:["A", "B", "C"], 420:["A", "B", "C"], 501:["A", "B", "C"], 502:["A", "B"], 503:["A", "B"], 504:["A", "B"], 505:["A", "B", "C", "D"], 
                            506:["A", "B", "C", "D"], 507:["A", "B", "C"], 508:["A", "B", "C"], 509:["A", "B", "C"], 510:["A", "B", "C"], 511:["A", "B"], 512:["A", "B"], 513:["A", "B"],
                            514:["A", "B"], 515:["A", "B", "C"], 516:["A", "B", "C"], 517:["A", "B", "C"], 518:["A", "B", "C"], 519:["A", "B", "C"], 520:["A", "B", "C"], 601:["A", "B", "C"],
                            602:["A", "B"], 603:["A", "B"], 604:["A", "B"], 605:["A", "B", "C", "D"], 606:["A", "B", "C", "D"], 607:["A", "B", "C"], 608:["A", "B", "C"], 609:["A", "B", "C"],
                            610:["A", "B", "C"], 611:["A", "B"], 612:["A", "B"], 613:["A", "B"], 614:["A", "B"], 615:["A", "B", "C"], 616:["A", "B", "C"], 617:["A", "B", "C"], 618:["A", "B", "C"],
                            619:["A", "B", "C"], 620:["A", "B", "C"]}

                            def call_func():
                                global student_info
                                global fee_info
                                global fee_data_set
                                global expense_info
                                global total_fee_info
                                global room_info

                                cursor.execute("select * from student_info")
                                student_info=cursor.fetchall()
                                cursor.execute("select * from fee_info")
                                fee_info=cursor.fetchall()
                                cursor.execute("select * from fee_stats")
                                fee_data_set=cursor.fetchall()
                                cursor.execute("select * from expenses")
                                expense_info=cursor.fetchall()
                                cursor.execute("select * from monthly_total_fee")
                                total_fee_info=cursor.fetchall()
                                cursor.execute("select * from rooms")
                                room_info=cursor.fetchall()

                            call_func()

                            def home():
                                global page_frame
                                try:
                                    page_frame.destroy()
                                except:
                                    pass

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Main_BG.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(page_frame)
                                e.pack(fill=BOTH, expand=YES)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.525, rely=0.065, relheight=0.4, relwidth=0.285)

                                def TIME():
                                    string = strftime('%H:%M:%S')
                                    time_label.config(text = string)
                                    time_label.after(1000, TIME)

                                time_label=Label(page_frame, background="#ffedf3", font=("Anton", 25), foreground="#811c98")
                                time_label.place(relx=0.8675, rely=0.0335, relheight=0.05)
                                TIME()

                                def Date():
                                    now=datetime.datetime.now()
                                    date_label.config(text=str(now.day)+"/"+str(now.month)+"/"+str(now.year))
                                    date_label.after(1000, Date)

                                date_label=Label(page_frame, background="#ffedf3", font=("Anton", 25), foreground="#811c98")
                                date_label.place(relx=0.8675, rely=0.08, relheight=0.05)
                                Date()

                                week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

                                def Day():
                                    now=datetime.datetime.now()
                                    week_num=datetime.date(now.year, now.month, now.day).weekday()
                                    DAY=week_days[week_num]
                                    day_label.config(text=DAY)
                                    day_label.after(1000, Day)

                                day_label=Label(page_frame, background="#ffedf3", font=("Anton", 25), foreground="#811c98")
                                day_label.place(relx=0.8675, rely=0.1275, relheight=0.05)
                                Day()

                                now=datetime.datetime.now()

                                n_s_bar=Scrollbar(page_frame)
                                n_s_bar.place(relx=0.4625, rely=0.06, relwidth=0.015, relheight=0.4)

                                n_view_text=Text(page_frame, background="#ffedf3", foreground="#811c98", font=("Anton", 20), wrap=WORD, yscrollcommand=n_s_bar.set)

                                n_list=[]

                                for i in student_info:
                                    cursor.execute(f"select * from fee_stats where Name='{i[0]}' and Mobile_No='{i[2]}' and Month='{month_dict[now.month]}' and Year='{now.year}'")
                                    n_data=cursor.fetchall()
                                    if len(n_data)==0:
                                        n_list.append(f"{i[0]} hasn't paid the fee for {month_dict[now.month]}, {now.year}.")
                                
                                for i in student_info:
                                    cursor.execute(f"select * from rooms where Name='{i[0]}' and Mobile_No='{i[2]}'")
                                    n_data=cursor.fetchall()
                                    if len(n_data)==0:
                                        n_list.append(f"{i[0]} hasn't been alloted a room.")


                                if len(n_list)!=0:
                                    for i in n_list:
                                        n_view_text.insert(END, f"{i}\n")
                                else:
                                    n_view_text.insert(END, "No Notifications to show!")
                                
                                n_view_text.config(state="disabled")
                                
                                n_view_text.place(relx=0.0375, rely=0.06, relheight=0.4, relwidth=0.425)

                                s_bar=Scrollbar(page_frame)
                                s_bar.place(relx=0.4625, rely=0.54, relwidth=0.015, relheight=0.4)

                                exp_view_text=Text(page_frame, background="#ffedf3", foreground="#811c98", font=("Anton", 20), wrap=WORD, yscrollcommand=s_bar.set)
                                cursor.execute(f"select Category, Amount from expenses where Month='{month_dict[now.month]}' and Year='{now.year}'")
                                exp_data=cursor.fetchall()

                                if len(exp_data)!=0:
                                    total=0
                                    for i in exp_data:
                                        amt=i[1][1:]
                                        total+=int(amt)
                                        data=f"Category: {i[0]}\nAmount: {i[1]}\n\n"
                                        exp_view_text.insert(END, data)
                                    exp_view_text.insert(END, f"Total: ₹{total}")
                                else:
                                    exp_view_text.insert(END, "No Expenses for this Month!")
                                
                                exp_view_text.config(state="disabled")
                                
                                exp_view_text.place(relx=0.0375, rely=0.54, relheight=0.4, relwidth=0.425)

                                global num
                                num=1
                                def photo_func():
                                    global num
                                    if num <= 5:
                                        h_photo_label=Label(page_frame, background="#ffedf3")
                                        class Example(Frame):
                                            def __init__(self, master, *pargs):
                                                Frame.__init__(self, master, *pargs)

                                                self.image = Image.open(f"Images/{num}.png")

                                                self.img_copy= self.image.copy()
                                            
                                                self.background_image = ImageTk.PhotoImage(self.image)

                                                self.background = Label(self, image=self.background_image)
                                                self.background.pack(fill=BOTH, expand=YES)
                                                self.background.bind('<Configure>', self._resize_image)

                                            def _resize_image(self,event):

                                                new_width = event.width
                                                new_height = event.height

                                                self.image = self.img_copy.resize((new_width, new_height))

                                                self.background_image = ImageTk.PhotoImage(self.image)
                                                self.background.configure(image =  self.background_image)

                                        e = Example(h_photo_label)
                                        e.pack(fill=BOTH, expand=YES)
                                        h_photo_label.place(relx=0.595, rely=0.54, relheight=0.4, relwidth=0.3)

                                        if num >= 5:
                                            num=1
                                        else:
                                            num+=1

                                    condt_label.after(10000, photo_func)
                                
                                condt_label=Label(page_frame)
                                photo_func()

                            def exit():
                                main_root.destroy()

                            def log_out():
                                main_root.destroy()
                                main_function()

                            def new_user():
                                main_root.destroy()
                                new_user_create()

                            def add_data():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.85, rely=0.01, relheight=0.15, relwidth=0.1)

                                stu_name=StringVar()
                                dob_var=StringVar()
                                mob_no=StringVar()
                                menu_var_blood=StringVar()
                                address_var=StringVar()
                                edu_var=StringVar()
                                insti_var=StringVar()
                                med_var=StringVar()
                                father_name_var=StringVar()
                                father_mob_no=StringVar()
                                father_occ_var=StringVar()
                                father_off_var=StringVar()
                                mother_name_var=StringVar()
                                mother_mob_no=StringVar()
                                mother_occ_var=StringVar()
                                mother_off_var=StringVar()
                                lg_name_var=StringVar()
                                lg_mob_no=StringVar()
                                lg_occ_var=StringVar()
                                lg_add_var=StringVar()
                                entry_date_var=StringVar()

                                now=datetime.datetime.now()
                                entry_date_var.set(str(now.day)+"/"+str(now.month)+"/"+str(now.year)+", "+strftime('%H:%M:%S'))

                                menu_var_blood.set("Select-")

                                s_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_name_label.place(relx=0.03, rely=0.03)
                                s_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=stu_name)
                                s_name_entry.place(relx=0.075, rely=0.03, relwidth=0.12, relheight=0.045)

                                s_dob_label=Label(page_frame, background="#ffedf3", text="Date of Birth:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_dob_label.place(relx=0.23, rely=0.03)
                                s_dob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=dob_var)
                                s_dob_entry.place(relx=0.325, rely=0.03, relwidth=0.12, relheight=0.045)

                                s_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mob_label.place(relx=0.48, rely=0.03)
                                s_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mob_no)
                                s_mob_entry.place(relx=0.585, rely=0.03, relwidth=0.12, relheight=0.045)

                                s_add_label=Label(page_frame, background="#ffedf3", text="Permanent Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_add_label.place(relx=0.03, rely=0.1)
                                s_add_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=address_var)
                                s_add_entry.place(relx=0.175, rely=0.1, relwidth=0.5, relheight=0.045)

                                s_blood_label=Label(page_frame, background="#ffedf3", text="Blood Group:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_blood_label.place(relx=0.735, rely=0.24)
                                blood_list=["Select-", "A+ve", "B+ve", "O+ve", "AB+ve", "A-ve", "B-ve", "O-ve", "AB-ve"]
                                arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                s_blood_menu=OptionMenu(page_frame, menu_var_blood, *blood_list)
                                s_blood_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                s_blood_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                s_blood_menu.place(relx=0.825, rely=0.24, relwidth=0.085, relheight=0.045)
                                s_blood_menu.image=arrow

                                s_edu_label=Label(page_frame, background="#ffedf3", text="Educational Qualification:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_edu_label.place(relx=0.03, rely=0.17)
                                s_edu_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=edu_var)
                                s_edu_entry.place(relx=0.2, rely=0.17, relwidth=0.2, relheight=0.045)

                                s_insti_label=Label(page_frame, background="#ffedf3", text="Name and Address of Institution/Work Place:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_insti_label.place(relx=0.433, rely=0.17)
                                s_insti_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=insti_var)
                                s_insti_entry.place(relx=0.739, rely=0.17, relwidth=0.2, relheight=0.045)

                                s_med_label=Label(page_frame, background="#ffedf3", text="Medical Condition ( if any ):", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_med_label.place(relx=0.03, rely=0.24)
                                s_med_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=med_var)
                                s_med_entry.place(relx=0.21, rely=0.24, relwidth=0.5, relheight=0.045)

                                s_father_name_label=Label(page_frame, background="#ffedf3", text="Father's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_father_name_label.place(relx=0.03, rely=0.31)
                                s_father_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_name_var)
                                s_father_name_entry.place(relx=0.135, rely=0.31, relwidth=0.12, relheight=0.045)

                                s_father_mob_label=Label(page_frame, background="#ffedf3", text="Father's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_father_mob_label.place(relx=0.285, rely=0.31)
                                s_father_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_mob_no)
                                s_father_mob_entry.place(relx=0.45, rely=0.31, relwidth=0.12, relheight=0.045)

                                s_father_occ_label=Label(page_frame, background="#ffedf3", text="Father's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_father_occ_label.place(relx=0.6028, rely=0.31)
                                s_father_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_occ_var)
                                s_father_occ_entry.place(relx=0.745, rely=0.31, relwidth=0.12, relheight=0.045)

                                s_father_off_label=Label(page_frame, background="#ffedf3", text="Father's Office Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_father_off_label.place(relx=0.03, rely=0.38)
                                s_father_off_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_off_var)
                                s_father_off_entry.place(relx=0.2, rely=0.38, relwidth=0.5, relheight=0.045)

                                s_mother_name_label=Label(page_frame, background="#ffedf3", text="Mother's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mother_name_label.place(relx=0.03, rely=0.45)
                                s_mother_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_name_var)
                                s_mother_name_entry.place(relx=0.143, rely=0.45, relwidth=0.12, relheight=0.045)

                                s_mother_mob_label=Label(page_frame, background="#ffedf3", text="Mother's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mother_mob_label.place(relx=0.2925, rely=0.45)
                                s_mother_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_mob_no)
                                s_mother_mob_entry.place(relx=0.4675, rely=0.45, relwidth=0.12, relheight=0.045)

                                s_mother_occ_label=Label(page_frame, background="#ffedf3", text="Mother's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mother_occ_label.place(relx=0.6203, rely=0.45)
                                s_mother_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_occ_var)
                                s_mother_occ_entry.place(relx=0.77, rely=0.45, relwidth=0.12, relheight=0.045)

                                s_mother_off_label=Label(page_frame, background="#ffedf3", text="Mother's Office Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mother_off_label.place(relx=0.03, rely=0.52)
                                s_mother_off_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_off_var)
                                s_mother_off_entry.place(relx=0.205, rely=0.52, relwidth=0.5, relheight=0.045)

                                s_lg_name_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_lg_name_label.place(relx=0.03, rely=0.59)
                                s_lg_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_name_var)
                                s_lg_name_entry.place(relx=0.185, rely=0.59, relwidth=0.12, relheight=0.045)

                                s_lg_mob_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_lg_mob_label.place(relx=0.3425, rely=0.59)
                                s_lg_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_mob_no)
                                s_lg_mob_entry.place(relx=0.5575, rely=0.59, relwidth=0.12, relheight=0.045)

                                s_lg_occ_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_lg_occ_label.place(relx=0.705, rely=0.59)
                                s_lg_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_occ_var)
                                s_lg_occ_entry.place(relx=0.8975, rely=0.59, relwidth=0.09, relheight=0.045)

                                s_lg_add_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_lg_add_label.place(relx=0.03, rely=0.66)
                                s_lg_add_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_add_var)
                                s_lg_add_entry.place(relx=0.205, rely=0.66, relwidth=0.5, relheight=0.045)

                                s_entry_label=Label(page_frame, background="#ffedf3", text="Entry Date:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_entry_label.place(relx=0.03, rely=0.73)
                                s_entry_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=entry_date_var)
                                s_entry_entry.place(relx=0.11, rely=0.73, relwidth=0.15, relheight=0.045)

                                def add_data_button():
                                    if stu_name.get()!="" and dob_var.get()!="" and mob_no.get()!="" and menu_var_blood.get()!="Select-" and address_var.get()!="" and edu_var.get()!="" and insti_var.get()!="" and father_name_var.get()!="" and father_mob_no.get()!="" and father_occ_var.get()!="" and mother_name_var.get()!="" and mother_mob_no.get()!="" and mother_occ_var.get()!="" and entry_date_var.get()!="":

                                        for i in student_info:
                                            if i[0]==stu_name.get() and i[1]==dob_var.get() and i[2]==mob_no.get():
                                                main_conditional_label.configure(text="Data Set Alreaady Exists!", foreground="Red")
                                                main_conditional_label.place(relx=0.425, rely=0.87)
                                                break
                                        
                                        else:
                                            main_conditional_label.configure(text="", foreground="Red")
                                            main_conditional_label.place(relx=0.425, rely=0.87)
                                        
                                            try:
                                                name=stu_name.get()
                                                dob=dob_var.get()
                                                mobile=mob_no.get()
                                                addr=address_var.get()
                                                edu=edu_var.get()
                                                insti=insti_var.get()
                                                blood=menu_var_blood.get()
                                                med=med_var.get()
                                                f_name=father_name_var.get()
                                                f_mob=father_mob_no.get()
                                                f_occ=father_occ_var.get()
                                                f_off=father_off_var.get()
                                                m_name=mother_name_var.get()
                                                m_mob=mother_mob_no.get()
                                                m_occ=mother_occ_var.get()
                                                m_off=mother_off_var.get()
                                                lg_name=lg_name_var.get()
                                                lg_mob=lg_mob_no.get()
                                                lg_add=lg_add_var.get()
                                                lg_occ=lg_occ_var.get()
                                                entry_d=entry_date_var.get()

                                                global page_frame
                                                page_frame.destroy()

                                                page_frame=Frame(main_root, background="#ffedf3")
                                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                                main_photo_label=Label(page_frame, background="#ffedf3")
                                                class Example(Frame):
                                                    def __init__(self, master, *pargs):
                                                        Frame.__init__(self, master, *pargs)

                                                        self.image = Image.open("Images/Logo_2.png")
                                                        self.img_copy= self.image.copy()

                                                        self.background_image = ImageTk.PhotoImage(self.image)

                                                        self.background = Label(self, image=self.background_image)
                                                        self.background.pack(fill=BOTH, expand=YES)
                                                        self.background.bind('<Configure>', self._resize_image)

                                                    def _resize_image(self,event):

                                                        new_width = event.width
                                                        new_height = event.height

                                                        self.image = self.img_copy.resize((new_width, new_height))

                                                        self.background_image = ImageTk.PhotoImage(self.image)
                                                        self.background.configure(image =  self.background_image)

                                                e = Example(main_photo_label)
                                                e.pack(fill=BOTH, expand=YES)
                                                main_photo_label.place(relx=0.85, rely=0.01, relheight=0.15, relwidth=0.1)

                                                name_var=StringVar()
                                                mob_no_var=StringVar()
                                                reg_fee_var=StringVar()
                                                caution_var=StringVar()
                                                monthly_fee_var=StringVar()

                                                name_var.set(name)
                                                mob_no_var.set(mobile)
                                                reg_fee_var.set("₹")
                                                caution_var.set("₹")
                                                monthly_fee_var.set("₹")

                                                f_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_name_label.place(relx=0.03, rely=0.03)
                                                f_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=name_var, state="disabled")
                                                f_name_entry.place(relx=0.075, rely=0.03, relwidth=0.12, relheight=0.045)

                                                f_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_mob_label.place(relx=0.23, rely=0.03)
                                                f_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mob_no_var, state="disabled")
                                                f_mob_entry.place(relx=0.335, rely=0.03, relwidth=0.12, relheight=0.045)

                                                f_reg_label=Label(page_frame, background="#ffedf3", text="Registration Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_reg_label.place(relx=0.03, rely=0.1)
                                                f_reg_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=reg_fee_var)
                                                f_reg_entry.place(relx=0.15, rely=0.1, relwidth=0.12, relheight=0.045)

                                                f_caution_label=Label(page_frame, background="#ffedf3", text="Caution Money:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_caution_label.place(relx=0.3, rely=0.1)
                                                f_caution_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=caution_var)
                                                f_caution_entry.place(relx=0.405, rely=0.1, relwidth=0.12, relheight=0.045)

                                                f_monthly_label=Label(page_frame, background="#ffedf3", text="Monthly Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_monthly_label.place(relx=0.562, rely=0.1)
                                                f_monthly_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=monthly_fee_var)
                                                f_monthly_entry.place(relx=0.65, rely=0.1, relwidth=0.12, relheight=0.045)

                                                def fee_button():
                                                    if reg_fee_var.get()!="" and reg_fee_var.get()!="₹" and caution_var.get()!="" and caution_var.get()!="₹" and monthly_fee_var.get()!="" and monthly_fee_var.get()!="₹":
                                                        cursor.execute(f"insert into student_info values ('{name}', '{dob}', '{mobile}', '{addr}', '{edu}', '{insti}', '{blood}', '{med}', '{f_name}', '{f_mob}', '{f_occ}', '{f_off}', '{m_name}', '{m_mob}', '{m_occ}', '{m_off}', '{lg_name}', '{lg_mob}', '{lg_add}', '{lg_occ}', '{entry_d}')")
                                                        cursor.execute(f"insert into fee_info values ('{name_var.get()}', '{mob_no_var.get()}', '{reg_fee_var.get()}', '{caution_var.get()}', '{monthly_fee_var.get()}')")
                                                        db_connection.commit()
                                                        
                                                        date_list=entry_d.split(", ")
                                                        date_list_1=date_list[0].split("/")
                                                        m_number=date_list_1[1]
                                                        y=date_list_1[2]
                                                        m=month_dict[int(m_number)]

                                                        exist=0
                                                        for i in total_fee_info:
                                                            if i[0]==m and i[1]==y:
                                                                exist=1
                                                            else:
                                                                exist=0
                                                        
                                                        if exist==0:
                                                            cursor.execute(f"insert into monthly_total_fee values ('{month_dict[now.month]}', '{str(now.year)}', '₹{str(int(reg_fee_var.get()[1:])+int(caution_var.get()[1:])+int(monthly_fee_var.get()[1:]))}')")
                                                            db_connection.commit()
                                                        else:
                                                            cursor.execute(f"update monthly_total_fee set Total_Fee='₹{str(int(reg_fee_var.get()[1:])+int(caution_var.get()[1:])+int(monthly_fee_var.get()[1:]))}' where Month='{m}' and Year='{y}'")
                                                            db_connection.commit()
                                                        messagebox.showinfo("Action Successful", "Data Entry Successful!")
                                                        call_func()
                                                        add_data()
                                                    else:
                                                        f_conditional_label.configure(text="Please Enter all Essential Details!", foreground="Red")
                                                        f_conditional_label.place(relx=0.4, rely=0.87)
                                                
                                                f_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                                f_add_button=Button(page_frame, text="Add Data", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", command=fee_button)
                                                f_add_button.place(relx=0.475, rely=0.8, relheight=0.06)

                                            except:
                                                main_conditional_label.configure(text="Please Enter Valid Data!", foreground="Red")
                                                main_conditional_label.place(relx=0.4, rely=0.87)

                                    else:
                                        main_conditional_label.configure(text="Please Enter all Essential Details!", foreground="Red")
                                        main_conditional_label.place(relx=0.4, rely=0.87)

                                add_button=Button(page_frame, text="Add Data", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", command=add_data_button)
                                add_button.place(relx=0.475, rely=0.8, relheight=0.06)

                                main_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                            def delete_edit_data():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                search_var=StringVar()
                                search_var.set(None)

                                search_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=search_var)
                                search_entry.place(relx=0.03, rely=0.03, relwidth=0.7, relheight=0.045)

                                def search():

                                    global flag
                                    flag=0

                                    for i in student_info:
                                        for j in i:
                                            if j==search_var.get():

                                                flag=1

                                                cursor.execute(f"select * from fee_info where Name='{i[0]}' and Mobile_No='{i[2]}'")
                                                fee_list=cursor.fetchall()

                                                search_conditional_label.configure(text="")
                                                search_conditional_label.place(relx=0.45, rely=0.5)

                                                stu_name=StringVar()
                                                dob_var=StringVar()
                                                mob_no=StringVar()
                                                menu_var_blood=StringVar()
                                                address_var=StringVar()
                                                edu_var=StringVar()
                                                insti_var=StringVar()
                                                med_var=StringVar()
                                                father_name_var=StringVar()
                                                father_mob_no=StringVar()
                                                father_occ_var=StringVar()
                                                father_off_var=StringVar()
                                                mother_name_var=StringVar()
                                                mother_mob_no=StringVar()
                                                mother_occ_var=StringVar()
                                                mother_off_var=StringVar()
                                                lg_name_var=StringVar()
                                                lg_mob_no=StringVar()
                                                lg_occ_var=StringVar()
                                                lg_add_var=StringVar()
                                                entry_date_var=StringVar()
                                                s_reg_fee_var=StringVar()
                                                s_caution_var=StringVar()
                                                s_monthly_fee_var=StringVar()

                                                stu_name.set(i[0])
                                                dob_var.set(i[1])
                                                mob_no.set(i[2])
                                                menu_var_blood.set(i[6])
                                                address_var.set(i[3])
                                                edu_var.set(i[4])
                                                insti_var.set(i[5])
                                                med_var.set(i[7])
                                                father_name_var.set(i[8])
                                                father_mob_no.set(i[9])
                                                father_occ_var.set(i[10])
                                                father_off_var.set(i[11])
                                                mother_name_var.set(i[12])
                                                mother_mob_no.set(i[13])
                                                mother_occ_var.set(i[14])
                                                mother_off_var.set(i[15])
                                                lg_name_var.set(i[16])
                                                lg_mob_no.set(i[17])
                                                lg_occ_var.set(i[18])
                                                lg_add_var.set(i[19])
                                                entry_date_var.set(i[20])
                                                s_reg_fee_var.set(fee_list[0][2])
                                                s_caution_var.set(fee_list[0][3])
                                                s_monthly_fee_var.set(fee_list[0][4])

                                                s_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_name_label.place(relx=0.03, rely=0.1)
                                                s_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=stu_name)
                                                s_name_entry.place(relx=0.075, rely=0.1, relwidth=0.12, relheight=0.045)

                                                s_dob_label=Label(page_frame, background="#ffedf3", text="Date of Birth:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_dob_label.place(relx=0.23, rely=0.1)
                                                s_dob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=dob_var)
                                                s_dob_entry.place(relx=0.325, rely=0.1, relwidth=0.12, relheight=0.045)

                                                s_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mob_label.place(relx=0.48, rely=0.1)
                                                s_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mob_no)
                                                s_mob_entry.place(relx=0.585, rely=0.1, relwidth=0.12, relheight=0.045)

                                                s_add_label=Label(page_frame, background="#ffedf3", text="Permanent Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_add_label.place(relx=0.03, rely=0.17)
                                                s_add_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=address_var)
                                                s_add_entry.place(relx=0.175, rely=0.17, relwidth=0.5, relheight=0.045)

                                                s_blood_label=Label(page_frame, background="#ffedf3", text="Blood Group:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_blood_label.place(relx=0.735, rely=0.31)
                                                blood_list=["Select-", "A+ve", "B+ve", "O+ve", "AB+ve", "A-ve", "B-ve", "O-ve", "AB-ve"]
                                                arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                                s_blood_menu=OptionMenu(page_frame, menu_var_blood, *blood_list)
                                                s_blood_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                                s_blood_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                                s_blood_menu.place(relx=0.825, rely=0.31, relwidth=0.085, relheight=0.045)
                                                s_blood_menu.image=arrow

                                                s_edu_label=Label(page_frame, background="#ffedf3", text="Educational Qualification:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_edu_label.place(relx=0.03, rely=0.24)
                                                s_edu_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=edu_var)
                                                s_edu_entry.place(relx=0.2, rely=0.24, relwidth=0.2, relheight=0.045)

                                                s_insti_label=Label(page_frame, background="#ffedf3", text="Name and Address of Institution/Work Place:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_insti_label.place(relx=0.433, rely=0.24)
                                                s_insti_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=insti_var)
                                                s_insti_entry.place(relx=0.739, rely=0.24, relwidth=0.2, relheight=0.045)

                                                s_med_label=Label(page_frame, background="#ffedf3", text="Medical Condition ( if any ):", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_med_label.place(relx=0.03, rely=0.31)
                                                s_med_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=med_var)
                                                s_med_entry.place(relx=0.21, rely=0.31, relwidth=0.5, relheight=0.045)

                                                s_father_name_label=Label(page_frame, background="#ffedf3", text="Father's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_father_name_label.place(relx=0.03, rely=0.38)
                                                s_father_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_name_var)
                                                s_father_name_entry.place(relx=0.135, rely=0.38, relwidth=0.12, relheight=0.045)

                                                s_father_mob_label=Label(page_frame, background="#ffedf3", text="Father's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_father_mob_label.place(relx=0.285, rely=0.38)
                                                s_father_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_mob_no)
                                                s_father_mob_entry.place(relx=0.45, rely=0.38, relwidth=0.12, relheight=0.045)

                                                s_father_occ_label=Label(page_frame, background="#ffedf3", text="Father's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_father_occ_label.place(relx=0.6028, rely=0.38)
                                                s_father_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_occ_var)
                                                s_father_occ_entry.place(relx=0.745, rely=0.38, relwidth=0.12, relheight=0.045)

                                                s_father_off_label=Label(page_frame, background="#ffedf3", text="Father's Office Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_father_off_label.place(relx=0.03, rely=0.45)
                                                s_father_off_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_off_var)
                                                s_father_off_entry.place(relx=0.2, rely=0.45, relwidth=0.5, relheight=0.045)

                                                s_mother_name_label=Label(page_frame, background="#ffedf3", text="Mother's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mother_name_label.place(relx=0.03, rely=0.52)
                                                s_mother_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_name_var)
                                                s_mother_name_entry.place(relx=0.143, rely=0.52, relwidth=0.12, relheight=0.045)

                                                s_mother_mob_label=Label(page_frame, background="#ffedf3", text="Mother's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mother_mob_label.place(relx=0.2925, rely=0.52)
                                                s_mother_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_mob_no)
                                                s_mother_mob_entry.place(relx=0.4675, rely=0.52, relwidth=0.12, relheight=0.045)

                                                s_mother_occ_label=Label(page_frame, background="#ffedf3", text="Mother's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mother_occ_label.place(relx=0.6203, rely=0.52)
                                                s_mother_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_occ_var)
                                                s_mother_occ_entry.place(relx=0.77, rely=0.52, relwidth=0.12, relheight=0.045)

                                                s_mother_off_label=Label(page_frame, background="#ffedf3", text="Mother's Office Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mother_off_label.place(relx=0.03, rely=0.59)
                                                s_mother_off_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_off_var)
                                                s_mother_off_entry.place(relx=0.205, rely=0.59, relwidth=0.5, relheight=0.045)

                                                s_lg_name_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_lg_name_label.place(relx=0.03, rely=0.66)
                                                s_lg_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_name_var)
                                                s_lg_name_entry.place(relx=0.185, rely=0.66, relwidth=0.12, relheight=0.045)

                                                s_lg_mob_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_lg_mob_label.place(relx=0.3425, rely=0.66)
                                                s_lg_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_mob_no)
                                                s_lg_mob_entry.place(relx=0.5575, rely=0.66, relwidth=0.12, relheight=0.045)

                                                s_lg_occ_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_lg_occ_label.place(relx=0.705, rely=0.66)
                                                s_lg_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_occ_var)
                                                s_lg_occ_entry.place(relx=0.8975, rely=0.66, relwidth=0.09, relheight=0.045)

                                                s_lg_add_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_lg_add_label.place(relx=0.03, rely=0.73)
                                                s_lg_add_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_add_var)
                                                s_lg_add_entry.place(relx=0.205, rely=0.73, relwidth=0.5, relheight=0.045)

                                                s_entry_label=Label(page_frame, background="#ffedf3", text="Entry Date:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_entry_label.place(relx=0.03, rely=0.8)
                                                s_entry_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=entry_date_var)
                                                s_entry_entry.place(relx=0.11, rely=0.8, relwidth=0.15, relheight=0.045)

                                                s_reg_label=Label(page_frame, background="#ffedf3", text="Registration Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_reg_label.place(relx=0.2875, rely=0.8)
                                                s_reg_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=s_reg_fee_var)
                                                s_reg_entry.place(relx=0.405, rely=0.8, relwidth=0.075, relheight=0.045)

                                                s_caution_label=Label(page_frame, background="#ffedf3", text="Caution Money:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_caution_label.place(relx=0.505, rely=0.8)
                                                s_caution_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=s_caution_var)
                                                s_caution_entry.place(relx=0.61, rely=0.8, relwidth=0.075, relheight=0.045)

                                                s_monthly_label=Label(page_frame, background="#ffedf3", text="Monthly Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_monthly_label.place(relx=0.71, rely=0.8)
                                                s_monthly_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=s_monthly_fee_var)
                                                s_monthly_entry.place(relx=0.8, rely=0.8, relwidth=0.075, relheight=0.045)

                                                def delete_data():
                                                    cursor.execute(f"delete from student_info where Name='{stu_name.get()}' and DOB='{dob_var.get()}' and Mobile_No='{mob_no.get()}'")
                                                    cursor.execute(f"delete from fee_info where Name='{stu_name.get()}' and Mobile_No='{mob_no.get()}'")
                                                    db_connection.commit()

                                                    for i in room_info:
                                                        if i[0]==stu_name.get() and i[1]==mob_no.get():
                                                            cursor.execute(f"delete from rooms where Name='{stu_name.get()}' and Mobile_No='{mob_no.get()}'")
                                                            db_connection.commit()

                                                    now=datetime.datetime.now()

                                                    ins=0
                                                    for i in expense_info:
                                                        if i[0]==month_dict[now.month] and i[1]==str(now.year) and i[2]=="Caution Money Refund":
                                                            ins=1
                                                            break
                                                        else:
                                                            ins=0

                                                    if ins==0:
                                                        cursor.execute(f"insert into expenses values ('{month_dict[now.month]}', '{str(now.year)}', 'Caution Money Refund', '{s_caution_var.get()}')")
                                                        db_connection.commit()
                                                    else:
                                                        for i in expense_info:
                                                            if i[0]==month_dict[now.month] and i[1]==str(now.year) and i[2]=="Caution Money Refund":
                                                                Ref=int(i[3][1:])
                                                                cursor.execute(f"update expenses set Amount='{str(Ref+int(s_caution_var.get()[1:]))}' where Month='{month_dict[now.month]}' and Year='{str(now.year)}' and Category='Caution Money Refund'")
                                                                db_connection.commit()

                                                    call_func()
                                                    messagebox.showinfo("Action Successful", "Data Deleted Successfully!")
                                                    delete_edit_data()
                                                
                                                def edit_data():
                                                    cursor.execute(f"update student_info set Name='{stu_name.get()}', DOB='{dob_var.get()}', Mobile_No='{mob_no.get()}', Permanent_Address='{address_var.get()}', Educational_Qualification='{edu_var.get()}', Educational_Institution_or_Working_Place='{insti_var.get()}', Blood_Group='{menu_var_blood.get()}', Medical_Condition='{med_var.get()}', Father_Name='{father_name_var.get()}', Father_Mob_No='{father_mob_no.get()}',  Father_Occupation='{father_occ_var.get()}', Father_Office='{father_off_var.get()}', Mother_Name='{mother_name_var.get()}', Mother_Mob_No='{mother_mob_no.get()}', Mother_Occupation='{mother_occ_var.get()}', Mother_Office='{mother_off_var.get()}', L_G_Name='{lg_name_var.get()}', L_G_Mob_No='{lg_mob_no.get()}', L_G_Address='{lg_add_var.get()}', L_G_Occupation='{lg_occ_var.get()}', Entry_Date='{entry_date_var.get()}' where Name='{i[0]}' and DOB='{i[1]}' and Mobile_No='{i[2]}'")
                                                    db_connection.commit()
                                                    cursor.execute(f"update fee_info set Name='{stu_name.get()}', Mobile_No='{mob_no.get()}', Registration_Fee='{s_reg_fee_var.get()}', Caution_Money='{s_caution_var.get()}', Monthly_Fee='{s_monthly_fee_var.get()}' where Name='{fee_list[0][0]}' and Mobile_No='{fee_list[0][1]}'")
                                                    db_connection.commit()
                                                    call_func()
                                                    messagebox.showinfo("Action Successful", "Data Edited Successfully!")
                                                    delete_edit_data()

                                                edit_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), text="Edit Data", command=edit_data)
                                                edit_button.place(relx=0.4, rely=0.9, relheight=0.045)

                                                delete_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), text="Delete Data", command=delete_data)
                                                delete_button.place(relx=0.55, rely=0.9, relheight=0.045)

                                                break
                                    
                                    if flag==0:
                                        search_conditional_label.configure(text="No Match Found!", foreground="Red")
                                        search_conditional_label.place(relx=0.45, rely=0.5)

                                search_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.74, rely=0.03, relheight=0.052, relwidth=0.075)

                            def search_stu_data():

                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                fee_search_var=StringVar()

                                fee_search_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_search_var)
                                fee_search_entry.place(relx=0.03, rely=0.03, relwidth=0.7, relheight=0.045)

                                search_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                def fee_search():
                                    search_conditional_label.configure(text="", foreground="Red")
                                    search_conditional_label.place(relx=0.45, rely=0.5)
                                    
                                    cursor.execute("select * from student_info natural join fee_info")
                                    data_list_initial=cursor.fetchall()
                                    data_list=[]
                                    add=1
                                    if fee_search_var.get()=="":
                                        data_list=data_list_initial
                                    else:
                                        for i in data_list_initial:
                                            for j in i:
                                                if j==fee_search_var.get() or fee_search_var.get() in j or j==fee_search_var.get().lower() or fee_search_var.get().lower() in j or j==fee_search_var.get().upper() or fee_search_var.get().upper() in j or j==fee_search_var.get().title() or fee_search_var.get().title() in j:
                                                    for k in data_list:
                                                        if k!=i:
                                                            add=1
                                                        else:
                                                            add=0
                                                    if add==1:
                                                        data_list.append(i)
                                    
                                    if len(data_list)==0:
                                        search_conditional_label.configure(text="No Match Found!", foreground="Red")
                                        search_conditional_label.place(relx=0.45, rely=0.5)
                                    else:
                                        cols=("Name", "Mobile Number", "Date of Birth", "Permanent Address", "Educational Qualification", "Educational Institution/Office", "Blood Group", "Medical Condition", "Father's Name", "Father's Mobile Number", "Father's Occupation", "Father's Office", "Mother's Name", "Mother's Mobile Number", "Mother's Occupation", "Mother's Office", "Local Guardian's Name", "Local Guardian's Mobile Number", "Local Guardian's Address", "Local Guardian's Occupation", "Entry Date", "Registration Fee", "Caution Money", "Monthly Fee")

                                        search_result=ttk.Treeview(page_frame, columns=cols, show="headings")
                                        for i in cols:
                                            search_result.heading(i, text=i)

                                        for i in data_list:
                                            search_result.insert("", END, values=i)

                                        y_scroll=Scrollbar(page_frame, command=search_result.yview)

                                        x_scroll=Scrollbar(page_frame, command=search_result.xview, orient="horizontal")

                                        search_result.config(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

                                        search_result.place(relx=0.03, rely=0.15, relheight=0.8, relwidth=0.94)
                                        y_scroll.place(relx=0.971, rely=0.15, relheight=0.8, relwidth=0.01)
                                        x_scroll.place(relx=0.03, rely=0.951, relheight=0.01, relwidth=0.94)

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=fee_search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.74, rely=0.0275, relheight=0.052, relwidth=0.075)

                            def fee_add_data():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.85, rely=0.01, relheight=0.15, relwidth=0.1)

                                fee_name_var=StringVar()
                                fee_mob_no_var=StringVar()
                                fee_month_var=StringVar()
                                fee_year_var=StringVar()
                                fee_monthly_fee_var=StringVar()
                                fee_date_var=StringVar()

                                now=datetime.datetime.now()

                                global flag_2
                                flag_2=0

                                def check_func():
                                    global flag_2
                                    if flag_2==0:
                                        for i in fee_info:
                                            if i[0]==fee_name_var.get() and i[1]==fee_mob_no_var.get():
                                                fee_monthly_fee_var.set(i[4])
                                                fee_date_var.set(str(now.day)+"/"+str(now.month)+"/"+str(now.year))
                                                fee_year_var.set(str(now.year))
                                                fee_month_var.set(month_dict[now.month])
                                                fee_monthly_entry.configure(state="disabled")
                                                flag_2=1
                                                break
                                        fee_conditional_label.after(1000, check_func)

                                fee_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_name_label.place(relx=0.03, rely=0.03)
                                fee_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_name_var)
                                fee_name_entry.place(relx=0.075, rely=0.03, relwidth=0.12, relheight=0.045)

                                fee_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_mob_label.place(relx=0.23, rely=0.03)
                                fee_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_mob_no_var)
                                fee_mob_entry.place(relx=0.335, rely=0.03, relwidth=0.12, relheight=0.045)

                                fee_month_label=Label(page_frame, background="#ffedf3", text="Month:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_month_label.place(relx=0.03, rely=0.1)
                                fee_month_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_month_var)
                                fee_month_entry.place(relx=0.08, rely=0.1, relwidth=0.1, relheight=0.045)

                                fee_year_label=Label(page_frame, background="#ffedf3", text="Year:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_year_label.place(relx=0.21, rely=0.1)
                                fee_year_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_year_var)
                                fee_year_entry.place(relx=0.25, rely=0.1, relwidth=0.075, relheight=0.045)

                                fee_monthly_label=Label(page_frame, background="#ffedf3", text="Monthly Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_monthly_label.place(relx=0.3575, rely=0.1)
                                fee_monthly_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_monthly_fee_var)
                                fee_monthly_entry.place(relx=0.445, rely=0.1, relwidth=0.075, relheight=0.045)

                                fee_date_label=Label(page_frame, background="#ffedf3", text="Paid On:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_date_label.place(relx=0.03, rely=0.17)
                                fee_date_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_date_var)
                                fee_date_entry.place(relx=0.085, rely=0.17, relwidth=0.1, relheight=0.045)

                                def fee_status_button():
                                    fee_set=[]
                                    for i in fee_data_set:
                                        if i[0]==fee_name_var.get() and i[1]==fee_mob_no_var.get():
                                            fee_set.append(i)

                                    for i in fee_info:
                                        if i[0]==fee_name_var.get() and i[1]==fee_mob_no_var.get():
                                            if fee_name_var.get()!="" and fee_mob_no_var.get()!="" and fee_month_var.get()!="" and fee_year_var.get()!="" and fee_date_var.get()!="":
                                                if (fee_name_var.get(), fee_mob_no_var.get(), fee_month_var.get(), fee_year_var.get(), fee_date_var.get()) not in fee_set:
                                                    cursor.execute(f"insert into fee_stats values ('{fee_name_var.get()}', '{fee_mob_no_var.get()}', '{fee_month_var.get()}', '{fee_year_var.get()}', '{fee_date_var.get()}')")
                                                    db_connection.commit()
                                                    for i in total_fee_info:
                                                        if i[0]==fee_month_var.get() and i[1]==fee_year_var.get():
                                                            cursor.execute(f"update monthly_total_fee set Total_Fee='₹{str(int(i[2][1:])+int(fee_monthly_fee_var.get()[1:]))}' where Month='{fee_month_var.get()}' and Year='{fee_year_var.get()}'")
                                                            db_connection.commit()
                                                            messagebox.showinfo("Action Successful", "Data Entry Successful!")
                                                            call_func()
                                                            fee_add_data()
                                                            break
                                                    else:
                                                        cursor.execute(f"insert into monthly_total_fee values ('{fee_month_var.get()}', '{fee_year_var.get()}', '{fee_monthly_fee_var.get()}')")
                                                        db_connection.commit()
                                                        messagebox.showinfo("Action Successful", "Data Entry Successful!")
                                                        call_func()
                                                        fee_add_data()
                                                        break
                                                else:
                                                    fee_conditional_label.configure(text="Data Already Exists!", foreground="Red")
                                                    fee_conditional_label.place(relx=0.44, rely=0.87)
                                                    break
                                            else:
                                                fee_conditional_label.configure(text="Please Enter all Essential Details!", foreground="Red")
                                                fee_conditional_label.place(relx=0.4, rely=0.87)
                                                break
                                    else:
                                        fee_conditional_label.configure(text="Student Not Found!", foreground="Red")
                                        fee_conditional_label.place(relx=0.45, rely=0.87)
                                                
                                fee_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))
                                check_func()

                                f_add_button=Button(page_frame, text="Add Data", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3",command=fee_status_button)
                                f_add_button.place(relx=0.475, rely=0.8, relheight=0.06)

                            def fee_search_data():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                fee_search_var=StringVar()
                                fee_search_var.set("")

                                fee_search_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_search_var)
                                fee_search_entry.place(relx=0.03, rely=0.03, relwidth=0.7, relheight=0.045)

                                search_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                def fee_search():
                                    search_conditional_label.configure(text="", foreground="Red")
                                    search_conditional_label.place(relx=0.45, rely=0.5)
                                    cursor.execute("select Name, Mobile_No, Month, Year, Monthly_Fee, Paid_On from fee_stats natural join fee_info")
                                    data_list_initial=cursor.fetchall()
                                    data_list=[]
                                    add=1
                                    if fee_search_var.get()=="":
                                        data_list=data_list_initial
                                    else:
                                        for i in data_list_initial:
                                            for j in i:
                                                if j==fee_search_var.get() or fee_search_var.get() in j or j==fee_search_var.get().lower() or fee_search_var.get().lower() in j or j==fee_search_var.get().upper() or fee_search_var.get().upper() in j or j==fee_search_var.get().title() or fee_search_var.get().title() in j:
                                                    for k in data_list:
                                                        if k!=i:
                                                            add=1
                                                        else:
                                                            add=0
                                                    if add==1:
                                                        data_list.append(i)
                                    
                                    if len(data_list)==0:
                                        search_conditional_label.configure(text="No Match Found!", foreground="Red")
                                        search_conditional_label.place(relx=0.45, rely=0.5)
                                    else:
                                        cols=("Name", "Mobile Number", "Month", "Year", "Monthly Fee", "Paid On")

                                        search_result=ttk.Treeview(page_frame, columns=cols, show="headings")
                                        search_result.heading("Name", text="Name")
                                        search_result.heading("Mobile Number", text="Mobile Number")
                                        search_result.heading("Month", text="Month")
                                        search_result.heading("Year", text="Year")
                                        search_result.heading("Monthly Fee", text="Monthly Fee")
                                        search_result.heading("Paid On", text="Paid On")

                                        for i in data_list:
                                            search_result.insert("", END, values=i)

                                        y_scroll=Scrollbar(page_frame, command=search_result.yview)

                                        search_result.config(yscrollcommand=y_scroll.set)

                                        search_result.place(relx=0.03, rely=0.15, relheight=0.825, relwidth=0.94)
                                        y_scroll.place(relx=0.971, rely=0.15, relheight=0.825, relwidth=0.01)

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=fee_search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.74, rely=0.0275, relheight=0.052, relwidth=0.075)

                            def add_expenses():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Expense_Add_BG.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(page_frame)
                                e.pack(fill=BOTH, expand=YES)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                now=datetime.datetime.now()

                                exp_month_var=StringVar()
                                exp_year_var=StringVar()
                                exp_category_var=StringVar()
                                exp_amount_var=StringVar()

                                exp_month_var.set(month_dict[now.month])
                                exp_year_var.set(str(now.year))
                                exp_amount_var.set("₹")

                                month_list=[]
                                for i in month_dict:
                                    month_list.append(month_dict[i])

                                exp_month_label=Label(page_frame, background="#ffedf3", text="Month:", font=("Haettenschweiler", 25), foreground="#811c98")
                                exp_month_label.place(relx=0.03, rely=0.03)
                                arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                exp_month_menu=OptionMenu(page_frame, exp_month_var, *month_list)
                                exp_month_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), borderwidth=0)
                                exp_month_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                exp_month_menu.place(relx=0.082, rely=0.03, relwidth=0.115, relheight=0.05)
                                exp_month_menu.image=arrow

                                exp_year_label=Label(page_frame, background="#ffedf3", text="Year:", font=("Haettenschweiler", 25), foreground="#811c98")
                                exp_year_label.place(relx=0.235, rely=0.03)
                                exp_year_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=exp_year_var)
                                exp_year_entry.place(relx=0.28, rely=0.03, relwidth=0.075, relheight=0.045)

                                exp_category_label=Label(page_frame, background="#ffedf3", text="Category:", font=("Haettenschweiler", 25), foreground="#811c98")
                                exp_category_label.place(relx=0.03, rely=0.1)
                                exp_category_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=exp_category_var)
                                exp_category_entry.place(relx=0.1, rely=0.1, relwidth=0.255, relheight=0.045)

                                exp_year_label=Label(page_frame, background="#ffedf3", text="Amount:", font=("Haettenschweiler", 25), foreground="#811c98")
                                exp_year_label.place(relx=0.03, rely=0.17)
                                exp_year_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=exp_amount_var)
                                exp_year_entry.place(relx=0.09, rely=0.17, relwidth=0.1, relheight=0.045)

                                exp_head_label=Label(page_frame, background="#ffedf3", text=f"{exp_month_var.get()}, {exp_year_var.get()}", font=("Haettenschweiler", 40), foreground="#811c98")
                                exp_head_label.place(relx=0.535, rely=0.075)

                                s_bar=Scrollbar(page_frame)
                                s_bar.place(relx=0.9751, rely=0.175, relwidth=0.015, relheight=0.785)

                                global exp_view_text
                                exp_view_text=Text(page_frame, background="#ffedf3", foreground="#811c98", font=("Anton", 20), wrap=WORD, yscrollcommand=s_bar.set)
                                cursor.execute(f"select Category, Amount from expenses where Month='{exp_month_var.get()}' and Year='{exp_year_var.get()}'")
                                exp_data=cursor.fetchall()

                                if len(exp_data)!=0:
                                    total=0
                                    for i in exp_data:
                                        amt=i[1][1:]
                                        total+=int(amt)
                                        data=f"Category: {i[0]}\nAmount: {i[1]}\n\n"
                                        exp_view_text.insert(END, data)
                                    exp_view_text.insert(END, f"Total: ₹{total}")
                                else:
                                    exp_view_text.insert(END, "No Expenses for this Month!")
                                
                                exp_view_text.config(state="disabled")
                                
                                exp_view_text.place(relx=0.525, rely=0.175, relheight=0.785, relwidth=0.45)

                                exp_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                def add_exp():
                                    global exp_view_text
                                    if exp_year_var.get()!="" and exp_category_var.get()!="" and exp_amount_var.get()!="₹" and exp_amount_var.get()!="":
                                        cursor.execute(f"insert into expenses values ('{exp_month_var.get()}', '{exp_year_var.get()}', '{exp_category_var.get()}', '{exp_amount_var.get()}')")
                                        db_connection.commit()
                                        call_func()
                                        messagebox.showinfo("Action Successful", "Expenditure Entered Successfully!")
                                        exp_head_label.config(text=f"{exp_month_var.get()}, {exp_year_var.get()}")
                                        exp_view_text.destroy()
                                        exp_view_text=Text(page_frame, background="#ffedf3", foreground="#811c98", font=("Anton", 20), wrap=WORD, yscrollcommand=s_bar.set)
                                        cursor.execute(f"select Category, Amount from expenses where Month='{exp_month_var.get()}' and Year='{exp_year_var.get()}'")
                                        exp_data=cursor.fetchall()
                                        if len(exp_data)!=0:
                                            total=0
                                            for i in exp_data:
                                                amt=i[1][1:]
                                                total+=int(amt)
                                                data=f"Category: {i[0]}\nAmount: {i[1]}\n\n"
                                                exp_view_text.insert(END, data)
                                            exp_view_text.insert(END, f"Total: ₹{total}")
                                        else:
                                            exp_view_text.insert(END, "No Expenses for this Month!")
                                        exp_view_text.config(state="disabled")
                                        exp_view_text.place(relx=0.525, rely=0.175, relheight=0.785, relwidth=0.45)
                                        exp_month_var.set(month_dict[now.month])
                                        exp_year_var.set(str(now.year))
                                        exp_category_var.set("")
                                        exp_amount_var.set("₹")
                                    else:
                                        exp_conditional_label.config(text="Please Enter all Essential Details!", foreground="Red")
                                        exp_conditional_label.place(relx=0.1405, rely=0.87)

                                exp_add_button=Button(page_frame, text="Add Expenditure", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", command=add_exp)
                                exp_add_button.place(relx=0.185, rely=0.8, relheight=0.06)

                            def view_expenses():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                view_year_var=StringVar()
                                view_month_var=StringVar()

                                year_list=["Select-"]
                                view_year_var.set("Select-")

                                month_list=["Select-"]
                                view_month_var.set("Select-")

                                cursor.execute("Select distinct Year from expenses")
                                yl=cursor.fetchall()
                                for i in yl:
                                    for j in i:
                                        year_list.append(j)
                                
                                def month_find():
                                    if view_year_var.get()!="Select-":
                                        cursor.execute(f"select distinct Month from expenses where Year='{view_year_var.get()}'")
                                        ml=cursor.fetchall()
                                        for i in ml:
                                            for j in i:
                                                if j not in month_list:
                                                    month_list.append(j)
                                        exp_month_label=Label(page_frame, background="#ffedf3", text="Month:", font=("Haettenschweiler", 25), foreground="#811c98")
                                        exp_month_label.place(relx=0.21, rely=0.03)
                                        arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                        exp_month_menu=OptionMenu(page_frame, view_month_var, *month_list)
                                        exp_month_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), borderwidth=0)
                                        exp_month_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                        exp_month_menu.place(relx=0.26, rely=0.03, relwidth=0.115, relheight=0.05)
                                        exp_month_menu.image=arrow
                                    abc.after(1000, month_find)

                                exp_year_label=Label(page_frame, background="#ffedf3", text="Year:", font=("Haettenschweiler", 25), foreground="#811c98")
                                exp_year_label.place(relx=0.03, rely=0.03)
                                arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                exp_year_menu=OptionMenu(page_frame, view_year_var, *year_list)
                                exp_year_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), borderwidth=0)
                                exp_year_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                exp_year_menu.place(relx=0.07, rely=0.03, relwidth=0.1, relheight=0.05)
                                exp_year_menu.image=arrow

                                abc=Label(page_frame)
                                month_find()

                                def exp_search():
                                    if view_month_var.get()!="Select-" and view_year_var.get()!="Select-":
                                        s_bar=Scrollbar(page_frame)
                                        s_bar.place(relx=0.9505, rely=0.15, relwidth=0.015, relheight=0.78)

                                        exp_view_text=Text(page_frame, background="#ffedf3", foreground="#811c98", font=("Anton", 20), wrap=WORD, yscrollcommand=s_bar.set)
                                        cursor.execute(f"select Category, Amount from expenses where Month='{view_month_var.get()}' and Year='{view_year_var.get()}'")
                                        exp_data=cursor.fetchall()

                                        if len(exp_data)!=0:
                                            total=0
                                            for i in exp_data:
                                                amt=i[1]
                                                total+=int(amt[1:])
                                                data=f"\tCategory: {i[0]}\n\tAmount: {i[1]}\n\n"
                                                exp_view_text.insert(END, data)
                                            exp_view_text.insert(END, f"\tTotal: ₹{total}")
                                        else:
                                            exp_view_text.insert(END, "\tNo Expenses for this Month!")
                                        
                                        exp_view_text.config(state="disabled")
                                        exp_view_text.place(relx=0.03, rely=0.15, relheight=0.78, relwidth=0.92)
                                    else:
                                        exp_conditional_label.config(text="Please Enter all Essential Details!", foreground="Red")
                                        exp_conditional_label.place(relx=0.405, rely=0.5)
                                
                                exp_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=exp_search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.415, rely=0.0275, relheight=0.052, relwidth=0.075)

                            def allot_room():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                r_name_var=StringVar()
                                r_mob_var=StringVar()
                                r_room_var=StringVar()
                                r_bed_var=StringVar()

                                r_room_var.set("Select-")
                                r_bed_var.set("Select-")

                                r_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                r_name_label.place(relx=0.03, rely=0.03)
                                r_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=r_name_var)
                                r_name_entry.place(relx=0.075, rely=0.03, relwidth=0.12, relheight=0.045)

                                r_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                r_mob_label.place(relx=0.23, rely=0.03)
                                r_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=r_mob_var)
                                r_mob_entry.place(relx=0.335, rely=0.03, relwidth=0.12, relheight=0.045)

                                room_no=[]
                                for i in room_dict:
                                    room_no.append(i)
                                
                                for i in room_no:
                                    cursor.execute(f"select * from rooms where Room_No='{i}'")
                                    bed_check=cursor.fetchall()
                                    if len(bed_check)==len(room_dict[i]):
                                        room_no.remove(i)
                                
                                room_no.insert(0, "Select-")

                                def bed_count():
                                    if r_room_var.get()!="Select-":
                                        room=int(r_room_var.get())
                                        total_beds=room_dict[room]
                                        cursor.execute(f"select * from rooms where Room_No='{r_room_var.get()}'")
                                        occ_beds=cursor.fetchall()
                                        if len(occ_beds)!=0:
                                            for i in occ_beds:
                                                if i[3] in total_beds:
                                                    total_beds.remove(i[3])
                                        
                                        if "Select-" not in total_beds:
                                            total_beds.insert(0, "Select-")
                                        
                                        r_bed_label=Label(page_frame, background="#ffedf3", text="Bed Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                        r_bed_label.place(relx=0.64, rely=0.03)
                                        arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                        r_bed_menu=OptionMenu(page_frame, r_bed_var, *total_beds)
                                        r_bed_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), borderwidth=0)
                                        r_bed_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                        r_bed_menu.place(relx=0.725, rely=0.03, relwidth=0.085, relheight=0.05)
                                        r_bed_menu.image=arrow

                                    cd_label.after(1000, bed_count)
                                
                                r_room_label=Label(page_frame, background="#ffedf3", text="Room:", font=("Haettenschweiler", 25), foreground="#811c98")
                                r_room_label.place(relx=0.48, rely=0.03)
                                arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                r_room_menu=OptionMenu(page_frame, r_room_var, *room_no)
                                r_room_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), borderwidth=0)
                                r_room_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                r_room_menu.place(relx=0.525, rely=0.03, relwidth=0.085, relheight=0.05)
                                r_room_menu.image=arrow

                                cd_label=Label(page_frame)
                                bed_count()

                                def allot_btn():

                                    conditional_label.config(text="", foreground="Red")
                                    conditional_label.place(rely=0.87, relx=0.35)

                                    if r_name_var.get()!="" and r_mob_var.get()!="" and r_room_var.get()!="Select-" and r_bed_var.get()!="Select-":
                                        for i in room_info:
                                            if i[0]==r_name_var.get() and i[1]==r_mob_var.get():
                                                conditional_label.config(text="Room Already Alloted!", foreground="Red")
                                                conditional_label.place(rely=0.87, relx=0.4175)
                                                break
                                        else:
                                            for i in student_info:
                                                if i[0]==r_name_var.get() and i[2]==r_mob_var.get():
                                                    cursor.execute(f"insert into rooms values ('{r_name_var.get()}', '{r_mob_var.get()}', '{r_room_var.get()}', '{r_bed_var.get()}')")
                                                    db_connection.commit()
                                                    call_func()
                                                    messagebox.showinfo("Action Succesful", "Room Alloted Successfully!")
                                                    r_name_var.set("")
                                                    r_mob_var.set("")
                                                    r_room_var.set("Select-")
                                                    r_bed_var.set("Select-")
                                                    break
                                            else:
                                                conditional_label.config(text="Student Data does not Exist!", foreground="Red")
                                                conditional_label.place(rely=0.87, relx=0.395)
                                    else:
                                        conditional_label.config(text="Please Enter All Essential Details!", foreground="Red")
                                        conditional_label.place(rely=0.87, relx=0.38)
                                
                                conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                r_all_button=Button(page_frame, text="Allot Room", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", command=allot_btn)
                                r_all_button.place(relx=0.45, rely=0.8, relheight=0.06)

                            def search_room():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(main_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                fee_search_var=StringVar()
                                fee_search_var.set("")

                                fee_search_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_search_var)
                                fee_search_entry.place(relx=0.03, rely=0.03, relwidth=0.7, relheight=0.045)

                                search_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                def fee_search():
                                    search_conditional_label.configure(text="", foreground="Red")
                                    search_conditional_label.place(relx=0.45, rely=0.5)
                                    data_list=[]
                                    add=1
                                    if fee_search_var.get()=="":
                                        data_list=room_info
                                    else:
                                        for i in room_info:
                                            for j in i:
                                                if j==fee_search_var.get() or fee_search_var.get() in j or j==fee_search_var.get().lower() or fee_search_var.get().lower() in j or j==fee_search_var.get().upper() or fee_search_var.get().upper() in j or j==fee_search_var.get().title() or fee_search_var.get().title() in j:
                                                    for k in data_list:
                                                        if k!=i:
                                                            add=1
                                                        else:
                                                            add=0
                                                    if add==1:
                                                        data_list.append(i)

                                    if len(data_list)==0:
                                        search_conditional_label.configure(text="No Match Found!", foreground="Red")
                                        search_conditional_label.place(relx=0.45, rely=0.5)
                                    else:
                                        cols=("Name", "Mobile Number", "Room Number", "Bed")

                                        search_result=ttk.Treeview(page_frame, columns=cols, show="headings")
                                        search_result.heading("Name", text="Name")
                                        search_result.heading("Mobile Number", text="Mobile Number")
                                        search_result.heading("Room Number", text="Room Number")
                                        search_result.heading("Bed", text="Bed")

                                        for i in data_list:
                                            search_result.insert("", END, values=i)

                                        y_scroll=Scrollbar(page_frame, command=search_result.yview)

                                        search_result.config(yscrollcommand=y_scroll.set)

                                        search_result.place(relx=0.03, rely=0.15, relheight=0.825, relwidth=0.94)
                                        y_scroll.place(relx=0.971, rely=0.15, relheight=0.825, relwidth=0.01)

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=fee_search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.74, rely=0.0275, relheight=0.052, relwidth=0.075)

                            MENU=Menu(main_root, background="#ffedf3", foreground="#811c98")
                            mainmenu=Menu(MENU, tearoff=False, background="#ffedf3", foreground="#811c98")
                            MENU.add_cascade(label="Main Menu", menu=mainmenu, background="#ffedf3", foreground="#811c98")

                            mainmenu.add_command(label="Home", background="#ffedf3", foreground="#811c98", command=home)

                            mainmenu.add_command(label="Add New User", background="#ffedf3", foreground="#811c98", command=new_user)

                            sub_menu_data=Menu(mainmenu, tearoff=False, background="#ffedf3", foreground="#811c98")
                            sub_menu_data.add_command(label="Add Data", background="#ffedf3", foreground="#811c98", command=add_data)
                            sub_menu_data.add_command(label="Delete/Edit Data", background="#ffedf3", foreground="#811c98", command=delete_edit_data)
                            sub_menu_data.add_command(label="Search Data", background="#ffedf3", foreground="#811c98", command=search_stu_data)
                            mainmenu.add_cascade(label="Data Management", background="#ffedf3", foreground="#811c98", menu=sub_menu_data)

                            expense_sub_menu=Menu(mainmenu, tearoff=False, background="#ffedf3", foreground="#811c98")
                            expense_sub_menu.add_command(label="Add Expenditure", background="#ffedf3", foreground="#811c98", command=add_expenses)
                            expense_sub_menu.add_command(label="View Expenditure", background="#ffedf3", foreground="#811c98", command=view_expenses)
                            mainmenu.add_cascade(label="Expenses", background="#ffedf3", foreground="#811c98", menu=expense_sub_menu)

                            sub_menu=Menu(mainmenu, tearoff=False, background="#ffedf3", foreground="#811c98")
                            sub_menu.add_command(label="Add Fee Data", background="#ffedf3", foreground="#811c98", command=fee_add_data)
                            sub_menu.add_command(label="Search Fee Data", background="#ffedf3", foreground="#811c98", command=fee_search_data)
                            mainmenu.add_cascade(label="Fee Management", background="#ffedf3", foreground="#811c98", menu=sub_menu)

                            room_sub_menu=Menu(mainmenu, tearoff=False, background="#ffedf3", foreground="#811c98")
                            room_sub_menu.add_command(label="Allot Room", background="#ffedf3", foreground="#811c98", command=allot_room)
                            room_sub_menu.add_command(label="View Room Details", background="#ffedf3", foreground="#811c98", command=search_room)
                            mainmenu.add_cascade(label="Room Management", background="#ffedf3", foreground="#811c98", menu=room_sub_menu)

                            mainmenu.add_separator()

                            mainmenu.add_command(label="Log Out", background="#ffedf3", foreground="#811c98", command=log_out)

                            mainmenu.add_command(label="Exit", background="#ffedf3", foreground="#811c98", command=exit)

                            main_root.config(menu=MENU)

                            home()

                            main_root.mainloop()

                            break
                        
                        else:

                            restricted_root=Tk()
                            restricted_root.title("Dream Catcher Girl's Hostel")
                            restricted_root.state("zoomed")
                            restricted_root.iconbitmap("Images/Logo_3.ico")
                            restricted_root.configure(background="#ffedf3")

                            month_dict={1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
                            room_dict={301:["A", "B", "C"], 302:["A", "B", "C"], 303:["A", "B", "C"], 304:["A", "B", "C"], 305:["A", "B", "C"], 306:["A", "B", "C"], 307:["A", "B", "C", "D"],
                            401:["A", "B", "C"], 402:["A", "B"], 403:["A", "B"], 404:["A", "B"], 405:["A", "B", "C", "D"], 406:["A", "B", "C", "D"], 407:["A", "B", "C"], 408:["A", "B", "C"],
                            409:["A", "B", "C"], 410:["A", "B", "C"], 411:["A", "B"], 412:["A", "B"], 413:["A", "B"], 414:["A", "B"], 415:["A", "B", "C"], 416:["A", "B", "C"], 417:["A", "B", "C"],
                            418:["A", "B", "C"], 419:["A", "B", "C"], 420:["A", "B", "C"], 501:["A", "B", "C"], 502:["A", "B"], 503:["A", "B"], 504:["A", "B"], 505:["A", "B", "C", "D"], 
                            506:["A", "B", "C", "D"], 507:["A", "B", "C"], 508:["A", "B", "C"], 509:["A", "B", "C"], 510:["A", "B", "C"], 511:["A", "B"], 512:["A", "B"], 513:["A", "B"],
                            514:["A", "B"], 515:["A", "B", "C"], 516:["A", "B", "C"], 517:["A", "B", "C"], 518:["A", "B", "C"], 519:["A", "B", "C"], 520:["A", "B", "C"], 601:["A", "B", "C"],
                            602:["A", "B"], 603:["A", "B"], 604:["A", "B"], 605:["A", "B", "C", "D"], 606:["A", "B", "C", "D"], 607:["A", "B", "C"], 608:["A", "B", "C"], 609:["A", "B", "C"],
                            610:["A", "B", "C"], 611:["A", "B"], 612:["A", "B"], 613:["A", "B"], 614:["A", "B"], 615:["A", "B", "C"], 616:["A", "B", "C"], 617:["A", "B", "C"], 618:["A", "B", "C"],
                            619:["A", "B", "C"], 620:["A", "B", "C"]}

                            def call_func():
                                global student_info
                                global fee_info
                                global fee_data_set
                                global expense_info
                                global total_fee_info
                                global room_info

                                cursor.execute("select * from student_info")
                                student_info=cursor.fetchall()
                                cursor.execute("select * from fee_info")
                                fee_info=cursor.fetchall()
                                cursor.execute("select * from fee_stats")
                                fee_data_set=cursor.fetchall()
                                cursor.execute("select * from expenses")
                                expense_info=cursor.fetchall()
                                cursor.execute("select * from monthly_total_fee")
                                total_fee_info=cursor.fetchall()
                                cursor.execute("select * from rooms")
                                room_info=cursor.fetchall()

                            call_func()

                            def home():
                                global page_frame
                                try:
                                    page_frame.destroy()
                                except:
                                    pass

                                page_frame=Frame(restricted_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Main_BG.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(page_frame)
                                e.pack(fill=BOTH, expand=YES)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.525, rely=0.065, relheight=0.4, relwidth=0.285)

                                def TIME():
                                    string = strftime('%H:%M:%S')
                                    time_label.config(text = string)
                                    time_label.after(1000, TIME)

                                time_label=Label(page_frame, background="#ffedf3", font=("Anton", 25), foreground="#811c98")
                                time_label.place(relx=0.8675, rely=0.0335, relheight=0.05)
                                TIME()

                                def Date():
                                    now=datetime.datetime.now()
                                    date_label.config(text=str(now.day)+"/"+str(now.month)+"/"+str(now.year))
                                    date_label.after(1000, Date)

                                date_label=Label(page_frame, background="#ffedf3", font=("Anton", 25), foreground="#811c98")
                                date_label.place(relx=0.8675, rely=0.08, relheight=0.05)
                                Date()

                                week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

                                def Day():
                                    now=datetime.datetime.now()
                                    week_num=datetime.date(now.year, now.month, now.day).weekday()
                                    DAY=week_days[week_num]
                                    day_label.config(text=DAY)
                                    day_label.after(1000, Day)

                                day_label=Label(page_frame, background="#ffedf3", font=("Anton", 25), foreground="#811c98")
                                day_label.place(relx=0.8675, rely=0.1275, relheight=0.05)
                                Day()

                                now=datetime.datetime.now()

                                n_s_bar=Scrollbar(page_frame)
                                n_s_bar.place(relx=0.4625, rely=0.06, relwidth=0.015, relheight=0.4)

                                n_view_text=Text(page_frame, background="#ffedf3", foreground="#811c98", font=("Anton", 20), wrap=WORD, yscrollcommand=n_s_bar.set)

                                n_list=[]

                                for i in student_info:
                                    cursor.execute(f"select * from fee_stats where Name='{i[0]}' and Mobile_No='{i[2]}' and Month='{month_dict[now.month]}' and Year='{now.year}'")
                                    n_data=cursor.fetchall()
                                    if len(n_data)==0:
                                        n_list.append(f"{i[0]} hasn't paid the fee for {month_dict[now.month]}, {now.year}.")
                                
                                for i in student_info:
                                    cursor.execute(f"select * from rooms where Name='{i[0]}' and Mobile_No='{i[2]}'")
                                    n_data=cursor.fetchall()
                                    if len(n_data)==0:
                                        n_list.append(f"{i[0]} hasn't been alloted a room.")


                                if len(n_list)!=0:
                                    for i in n_list:
                                        n_view_text.insert(END, f"{i}\n")
                                else:
                                    n_view_text.insert(END, "No Notifications to show!")
                                
                                n_view_text.config(state="disabled")
                                
                                n_view_text.place(relx=0.0375, rely=0.06, relheight=0.4, relwidth=0.425)

                                global num
                                num=1
                                def photo_func():
                                    global num
                                    if num > 5:
                                        num=1
                                    elif num <= 5:
                                        h_photo_label=Label(page_frame, background="#ffedf3")
                                        class Example(Frame):
                                            def __init__(self, master, *pargs):
                                                Frame.__init__(self, master, *pargs)

                                                self.image = Image.open(f"Images/{num}.png")
                                                self.img_copy= self.image.copy()

                                                self.background_image = ImageTk.PhotoImage(self.image)

                                                self.background = Label(self, image=self.background_image)
                                                self.background.pack(fill=BOTH, expand=YES)
                                                self.background.bind('<Configure>', self._resize_image)

                                            def _resize_image(self,event):

                                                new_width = event.width
                                                new_height = event.height

                                                self.image = self.img_copy.resize((new_width, new_height))

                                                self.background_image = ImageTk.PhotoImage(self.image)
                                                self.background.configure(image =  self.background_image)

                                        e = Example(h_photo_label)
                                        e.pack(fill=BOTH, expand=YES)
                                        h_photo_label.place(relx=0.595, rely=0.54, relheight=0.4, relwidth=0.3)
                                        num+=1

                                    condt_label.after(10000, photo_func)
                                
                                condt_label=Label(page_frame)
                                photo_func()

                                new_room_dict=room_dict

                                room_no=[]
                                for i in room_dict:
                                    room_no.append(i)
                                
                                for i in room_no:
                                    cursor.execute(f"select * from rooms where Room_No='{i}'")
                                    bed_check=cursor.fetchall()
                                    if len(bed_check)==len(room_dict[i]):
                                        room_no.remove(i)
                                    else:
                                        for j in bed_check:
                                            new_room_dict[i].remove(j[3])
                                
                                emp_rooms={}
                                for i in room_no:
                                    emp_rooms[i]=new_room_dict[i]

                                r_s_bar=Scrollbar(page_frame)
                                r_s_bar.place(relx=0.4625, rely=0.54, relwidth=0.015, relheight=0.4)

                                r_view_text=Text(page_frame, background="#ffedf3", foreground="#811c98", font=("Anton", 20), wrap=WORD, yscrollcommand=r_s_bar.set)

                                if len(emp_rooms)!=0:
                                    for i in emp_rooms:
                                        r_view_text.insert(END, f"{i} : {len(emp_rooms[i])} beds vacant\n")
                                else:
                                    r_view_text.insert(END, "All rooms are fully occupied!")
                                
                                r_view_text.config(state="disabled")

                                r_view_text.place(relx=0.0375, rely=0.54, relheight=0.4, relwidth=0.425)

                            def exit():
                                restricted_root.destroy()

                            def log_out():
                                restricted_root.destroy()
                                main_function()

                            def add_data():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(restricted_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.85, rely=0.01, relheight=0.15, relwidth=0.1)

                                stu_name=StringVar()
                                dob_var=StringVar()
                                mob_no=StringVar()
                                menu_var_blood=StringVar()
                                address_var=StringVar()
                                edu_var=StringVar()
                                insti_var=StringVar()
                                med_var=StringVar()
                                father_name_var=StringVar()
                                father_mob_no=StringVar()
                                father_occ_var=StringVar()
                                father_off_var=StringVar()
                                mother_name_var=StringVar()
                                mother_mob_no=StringVar()
                                mother_occ_var=StringVar()
                                mother_off_var=StringVar()
                                lg_name_var=StringVar()
                                lg_mob_no=StringVar()
                                lg_occ_var=StringVar()
                                lg_add_var=StringVar()
                                entry_date_var=StringVar()

                                now=datetime.datetime.now()
                                entry_date_var.set(str(now.day)+"/"+str(now.month)+"/"+str(now.year)+", "+strftime('%H:%M:%S'))

                                menu_var_blood.set("Select-")

                                s_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_name_label.place(relx=0.03, rely=0.03)
                                s_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=stu_name)
                                s_name_entry.place(relx=0.075, rely=0.03, relwidth=0.12, relheight=0.045)

                                s_dob_label=Label(page_frame, background="#ffedf3", text="Date of Birth:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_dob_label.place(relx=0.23, rely=0.03)
                                s_dob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=dob_var)
                                s_dob_entry.place(relx=0.325, rely=0.03, relwidth=0.12, relheight=0.045)

                                s_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mob_label.place(relx=0.48, rely=0.03)
                                s_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mob_no)
                                s_mob_entry.place(relx=0.585, rely=0.03, relwidth=0.12, relheight=0.045)

                                s_add_label=Label(page_frame, background="#ffedf3", text="Permanent Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_add_label.place(relx=0.03, rely=0.1)
                                s_add_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=address_var)
                                s_add_entry.place(relx=0.175, rely=0.1, relwidth=0.5, relheight=0.045)

                                s_blood_label=Label(page_frame, background="#ffedf3", text="Blood Group:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_blood_label.place(relx=0.735, rely=0.24)
                                blood_list=["Select-", "A+ve", "B+ve", "O+ve", "AB+ve", "A-ve", "B-ve", "O-ve", "AB-ve"]
                                arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                s_blood_menu=OptionMenu(page_frame, menu_var_blood, *blood_list)
                                s_blood_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                s_blood_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                s_blood_menu.place(relx=0.825, rely=0.24, relwidth=0.085, relheight=0.045)
                                s_blood_menu.image=arrow

                                s_edu_label=Label(page_frame, background="#ffedf3", text="Educational Qualification:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_edu_label.place(relx=0.03, rely=0.17)
                                s_edu_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=edu_var)
                                s_edu_entry.place(relx=0.2, rely=0.17, relwidth=0.2, relheight=0.045)

                                s_insti_label=Label(page_frame, background="#ffedf3", text="Name and Address of Institution/Work Place:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_insti_label.place(relx=0.433, rely=0.17)
                                s_insti_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=insti_var)
                                s_insti_entry.place(relx=0.739, rely=0.17, relwidth=0.2, relheight=0.045)

                                s_med_label=Label(page_frame, background="#ffedf3", text="Medical Condition ( if any ):", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_med_label.place(relx=0.03, rely=0.24)
                                s_med_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=med_var)
                                s_med_entry.place(relx=0.21, rely=0.24, relwidth=0.5, relheight=0.045)

                                s_father_name_label=Label(page_frame, background="#ffedf3", text="Father's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_father_name_label.place(relx=0.03, rely=0.31)
                                s_father_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_name_var)
                                s_father_name_entry.place(relx=0.135, rely=0.31, relwidth=0.12, relheight=0.045)

                                s_father_mob_label=Label(page_frame, background="#ffedf3", text="Father's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_father_mob_label.place(relx=0.285, rely=0.31)
                                s_father_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_mob_no)
                                s_father_mob_entry.place(relx=0.45, rely=0.31, relwidth=0.12, relheight=0.045)

                                s_father_occ_label=Label(page_frame, background="#ffedf3", text="Father's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_father_occ_label.place(relx=0.6028, rely=0.31)
                                s_father_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_occ_var)
                                s_father_occ_entry.place(relx=0.745, rely=0.31, relwidth=0.12, relheight=0.045)

                                s_father_off_label=Label(page_frame, background="#ffedf3", text="Father's Office Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_father_off_label.place(relx=0.03, rely=0.38)
                                s_father_off_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_off_var)
                                s_father_off_entry.place(relx=0.2, rely=0.38, relwidth=0.5, relheight=0.045)

                                s_mother_name_label=Label(page_frame, background="#ffedf3", text="Mother's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mother_name_label.place(relx=0.03, rely=0.45)
                                s_mother_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_name_var)
                                s_mother_name_entry.place(relx=0.143, rely=0.45, relwidth=0.12, relheight=0.045)

                                s_mother_mob_label=Label(page_frame, background="#ffedf3", text="Mother's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mother_mob_label.place(relx=0.2925, rely=0.45)
                                s_mother_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_mob_no)
                                s_mother_mob_entry.place(relx=0.4675, rely=0.45, relwidth=0.12, relheight=0.045)

                                s_mother_occ_label=Label(page_frame, background="#ffedf3", text="Mother's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mother_occ_label.place(relx=0.6203, rely=0.45)
                                s_mother_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_occ_var)
                                s_mother_occ_entry.place(relx=0.77, rely=0.45, relwidth=0.12, relheight=0.045)

                                s_mother_off_label=Label(page_frame, background="#ffedf3", text="Mother's Office Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_mother_off_label.place(relx=0.03, rely=0.52)
                                s_mother_off_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_off_var)
                                s_mother_off_entry.place(relx=0.205, rely=0.52, relwidth=0.5, relheight=0.045)

                                s_lg_name_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_lg_name_label.place(relx=0.03, rely=0.59)
                                s_lg_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_name_var)
                                s_lg_name_entry.place(relx=0.185, rely=0.59, relwidth=0.12, relheight=0.045)

                                s_lg_mob_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_lg_mob_label.place(relx=0.3425, rely=0.59)
                                s_lg_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_mob_no)
                                s_lg_mob_entry.place(relx=0.5575, rely=0.59, relwidth=0.12, relheight=0.045)

                                s_lg_occ_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_lg_occ_label.place(relx=0.705, rely=0.59)
                                s_lg_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_occ_var)
                                s_lg_occ_entry.place(relx=0.8975, rely=0.59, relwidth=0.09, relheight=0.045)

                                s_lg_add_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_lg_add_label.place(relx=0.03, rely=0.66)
                                s_lg_add_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_add_var)
                                s_lg_add_entry.place(relx=0.205, rely=0.66, relwidth=0.5, relheight=0.045)

                                s_entry_label=Label(page_frame, background="#ffedf3", text="Entry Date:", font=("Haettenschweiler", 25), foreground="#811c98")
                                s_entry_label.place(relx=0.03, rely=0.73)
                                s_entry_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=entry_date_var)
                                s_entry_entry.place(relx=0.11, rely=0.73, relwidth=0.15, relheight=0.045)

                                def add_data_button():
                                    if stu_name.get()!="" and dob_var.get()!="" and mob_no.get()!="" and menu_var_blood.get()!="Select-" and address_var.get()!="" and edu_var.get()!="" and insti_var.get()!="" and father_name_var.get()!="" and father_mob_no.get()!="" and father_occ_var.get()!="" and mother_name_var.get()!="" and mother_mob_no.get()!="" and mother_occ_var.get()!="" and entry_date_var.get()!="":

                                        for i in student_info:
                                            if i[0]==stu_name.get() and i[1]==dob_var.get() and i[2]==mob_no.get():
                                                main_conditional_label.configure(text="Data Set Alreaady Exists!", foreground="Red")
                                                main_conditional_label.place(relx=0.425, rely=0.87)
                                                break
                                        
                                        else:
                                            main_conditional_label.configure(text="", foreground="Red")
                                            main_conditional_label.place(relx=0.425, rely=0.87)
                                        
                                            try:
                                                name=stu_name.get()
                                                dob=dob_var.get()
                                                mobile=mob_no.get()
                                                addr=address_var.get()
                                                edu=edu_var.get()
                                                insti=insti_var.get()
                                                blood=menu_var_blood.get()
                                                med=med_var.get()
                                                f_name=father_name_var.get()
                                                f_mob=father_mob_no.get()
                                                f_occ=father_occ_var.get()
                                                f_off=father_off_var.get()
                                                m_name=mother_name_var.get()
                                                m_mob=mother_mob_no.get()
                                                m_occ=mother_occ_var.get()
                                                m_off=mother_off_var.get()
                                                lg_name=lg_name_var.get()
                                                lg_mob=lg_mob_no.get()
                                                lg_add=lg_add_var.get()
                                                lg_occ=lg_occ_var.get()
                                                entry_d=entry_date_var.get()

                                                global page_frame
                                                page_frame.destroy()

                                                page_frame=Frame(restricted_root, background="#ffedf3")
                                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                                main_photo_label=Label(page_frame, background="#ffedf3")
                                                class Example(Frame):
                                                    def __init__(self, master, *pargs):
                                                        Frame.__init__(self, master, *pargs)

                                                        self.image = Image.open("Images/Logo_2.png")
                                                        self.img_copy= self.image.copy()

                                                        self.background_image = ImageTk.PhotoImage(self.image)

                                                        self.background = Label(self, image=self.background_image)
                                                        self.background.pack(fill=BOTH, expand=YES)
                                                        self.background.bind('<Configure>', self._resize_image)

                                                    def _resize_image(self,event):

                                                        new_width = event.width
                                                        new_height = event.height

                                                        self.image = self.img_copy.resize((new_width, new_height))

                                                        self.background_image = ImageTk.PhotoImage(self.image)
                                                        self.background.configure(image =  self.background_image)

                                                e = Example(main_photo_label)
                                                e.pack(fill=BOTH, expand=YES)
                                                main_photo_label.place(relx=0.85, rely=0.01, relheight=0.15, relwidth=0.1)

                                                name_var=StringVar()
                                                mob_no_var=StringVar()
                                                reg_fee_var=StringVar()
                                                caution_var=StringVar()
                                                monthly_fee_var=StringVar()

                                                name_var.set(name)
                                                mob_no_var.set(mobile)
                                                reg_fee_var.set("₹")
                                                caution_var.set("₹")
                                                monthly_fee_var.set("₹")

                                                f_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_name_label.place(relx=0.03, rely=0.03)
                                                f_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=name_var, state="disabled")
                                                f_name_entry.place(relx=0.075, rely=0.03, relwidth=0.12, relheight=0.045)

                                                f_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_mob_label.place(relx=0.23, rely=0.03)
                                                f_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mob_no_var, state="disabled")
                                                f_mob_entry.place(relx=0.335, rely=0.03, relwidth=0.12, relheight=0.045)

                                                f_reg_label=Label(page_frame, background="#ffedf3", text="Registration Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_reg_label.place(relx=0.03, rely=0.1)
                                                f_reg_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=reg_fee_var)
                                                f_reg_entry.place(relx=0.15, rely=0.1, relwidth=0.12, relheight=0.045)

                                                f_caution_label=Label(page_frame, background="#ffedf3", text="Caution Money:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_caution_label.place(relx=0.3, rely=0.1)
                                                f_caution_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=caution_var)
                                                f_caution_entry.place(relx=0.405, rely=0.1, relwidth=0.12, relheight=0.045)

                                                f_monthly_label=Label(page_frame, background="#ffedf3", text="Monthly Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                f_monthly_label.place(relx=0.562, rely=0.1)
                                                f_monthly_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=monthly_fee_var)
                                                f_monthly_entry.place(relx=0.65, rely=0.1, relwidth=0.12, relheight=0.045)

                                                def fee_button():
                                                    if reg_fee_var.get()!="" and reg_fee_var.get()!="₹" and caution_var.get()!="" and caution_var.get()!="₹" and monthly_fee_var.get()!="" and monthly_fee_var.get()!="₹":
                                                        cursor.execute(f"insert into student_info values ('{name}', '{dob}', '{mobile}', '{addr}', '{edu}', '{insti}', '{blood}', '{med}', '{f_name}', '{f_mob}', '{f_occ}', '{f_off}', '{m_name}', '{m_mob}', '{m_occ}', '{m_off}', '{lg_name}', '{lg_mob}', '{lg_add}', '{lg_occ}', '{entry_d}')")
                                                        cursor.execute(f"insert into fee_info values ('{name_var.get()}', '{mob_no_var.get()}', '{reg_fee_var.get()}', '{caution_var.get()}', '{monthly_fee_var.get()}')")
                                                        db_connection.commit()
                                                        
                                                        date_list=entry_d.split(", ")
                                                        date_list_1=date_list[0].split("/")
                                                        m_number=date_list_1[1]
                                                        y=date_list_1[2]
                                                        m=month_dict[int(m_number)]

                                                        exist=0
                                                        for i in total_fee_info:
                                                            if i[0]==m and i[1]==y:
                                                                exist=1
                                                            else:
                                                                exist=0
                                                        
                                                        if exist==0:
                                                            cursor.execute(f"insert into monthly_total_fee values ('{month_dict[now.month]}', '{str(now.year)}', '₹{str(int(reg_fee_var.get()[1:])+int(caution_var.get()[1:])+int(monthly_fee_var.get()[1:]))}')")
                                                            db_connection.commit()
                                                        else:
                                                            cursor.execute(f"update monthly_total_fee set Total_Fee='₹{str(int(reg_fee_var.get()[1:])+int(caution_var.get()[1:])+int(monthly_fee_var.get()[1:]))}' where Month='{m}' and Year='{y}'")
                                                            db_connection.commit()
                                                        messagebox.showinfo("Action Successful", "Data Entry Successful!")
                                                        call_func()
                                                        add_data()
                                                    else:
                                                        f_conditional_label.configure(text="Please Enter all Essential Details!", foreground="Red")
                                                        f_conditional_label.place(relx=0.4, rely=0.87)
                                                
                                                f_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                                f_add_button=Button(page_frame, text="Add Data", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", command=fee_button)
                                                f_add_button.place(relx=0.475, rely=0.8, relheight=0.06)

                                            except:
                                                main_conditional_label.configure(text="Please Enter Valid Data!", foreground="Red")
                                                main_conditional_label.place(relx=0.4, rely=0.87)

                                    else:
                                        main_conditional_label.configure(text="Please Enter all Essential Details!", foreground="Red")
                                        main_conditional_label.place(relx=0.4, rely=0.87)

                                add_button=Button(page_frame, text="Add Data", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", command=add_data_button)
                                add_button.place(relx=0.475, rely=0.8, relheight=0.06)

                                main_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                            def delete_edit_data():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(restricted_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                search_var=StringVar()
                                search_var.set(None)

                                search_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=search_var)
                                search_entry.place(relx=0.03, rely=0.03, relwidth=0.7, relheight=0.045)

                                def search():

                                    global flag
                                    flag=0

                                    for i in student_info:
                                        for j in i:
                                            if j==search_var.get():

                                                flag=1

                                                cursor.execute(f"select * from fee_info where Name='{i[0]}' and Mobile_No='{i[2]}'")
                                                fee_list=cursor.fetchall()

                                                search_conditional_label.configure(text="")
                                                search_conditional_label.place(relx=0.45, rely=0.5)

                                                stu_name=StringVar()
                                                dob_var=StringVar()
                                                mob_no=StringVar()
                                                menu_var_blood=StringVar()
                                                address_var=StringVar()
                                                edu_var=StringVar()
                                                insti_var=StringVar()
                                                med_var=StringVar()
                                                father_name_var=StringVar()
                                                father_mob_no=StringVar()
                                                father_occ_var=StringVar()
                                                father_off_var=StringVar()
                                                mother_name_var=StringVar()
                                                mother_mob_no=StringVar()
                                                mother_occ_var=StringVar()
                                                mother_off_var=StringVar()
                                                lg_name_var=StringVar()
                                                lg_mob_no=StringVar()
                                                lg_occ_var=StringVar()
                                                lg_add_var=StringVar()
                                                entry_date_var=StringVar()
                                                s_reg_fee_var=StringVar()
                                                s_caution_var=StringVar()
                                                s_monthly_fee_var=StringVar()

                                                stu_name.set(i[0])
                                                dob_var.set(i[1])
                                                mob_no.set(i[2])
                                                menu_var_blood.set(i[6])
                                                address_var.set(i[3])
                                                edu_var.set(i[4])
                                                insti_var.set(i[5])
                                                med_var.set(i[7])
                                                father_name_var.set(i[8])
                                                father_mob_no.set(i[9])
                                                father_occ_var.set(i[10])
                                                father_off_var.set(i[11])
                                                mother_name_var.set(i[12])
                                                mother_mob_no.set(i[13])
                                                mother_occ_var.set(i[14])
                                                mother_off_var.set(i[15])
                                                lg_name_var.set(i[16])
                                                lg_mob_no.set(i[17])
                                                lg_occ_var.set(i[18])
                                                lg_add_var.set(i[19])
                                                entry_date_var.set(i[20])
                                                s_reg_fee_var.set(fee_list[0][2])
                                                s_caution_var.set(fee_list[0][3])
                                                s_monthly_fee_var.set(fee_list[0][4])

                                                s_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_name_label.place(relx=0.03, rely=0.1)
                                                s_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=stu_name)
                                                s_name_entry.place(relx=0.075, rely=0.1, relwidth=0.12, relheight=0.045)

                                                s_dob_label=Label(page_frame, background="#ffedf3", text="Date of Birth:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_dob_label.place(relx=0.23, rely=0.1)
                                                s_dob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=dob_var)
                                                s_dob_entry.place(relx=0.325, rely=0.1, relwidth=0.12, relheight=0.045)

                                                s_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mob_label.place(relx=0.48, rely=0.1)
                                                s_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mob_no)
                                                s_mob_entry.place(relx=0.585, rely=0.1, relwidth=0.12, relheight=0.045)

                                                s_add_label=Label(page_frame, background="#ffedf3", text="Permanent Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_add_label.place(relx=0.03, rely=0.17)
                                                s_add_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=address_var)
                                                s_add_entry.place(relx=0.175, rely=0.17, relwidth=0.5, relheight=0.045)

                                                s_blood_label=Label(page_frame, background="#ffedf3", text="Blood Group:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_blood_label.place(relx=0.735, rely=0.31)
                                                blood_list=["Select-", "A+ve", "B+ve", "O+ve", "AB+ve", "A-ve", "B-ve", "O-ve", "AB-ve"]
                                                arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                                s_blood_menu=OptionMenu(page_frame, menu_var_blood, *blood_list)
                                                s_blood_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                                s_blood_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                                s_blood_menu.place(relx=0.825, rely=0.31, relwidth=0.085, relheight=0.045)
                                                s_blood_menu.image=arrow

                                                s_edu_label=Label(page_frame, background="#ffedf3", text="Educational Qualification:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_edu_label.place(relx=0.03, rely=0.24)
                                                s_edu_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=edu_var)
                                                s_edu_entry.place(relx=0.2, rely=0.24, relwidth=0.2, relheight=0.045)

                                                s_insti_label=Label(page_frame, background="#ffedf3", text="Name and Address of Institution/Work Place:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_insti_label.place(relx=0.433, rely=0.24)
                                                s_insti_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=insti_var)
                                                s_insti_entry.place(relx=0.739, rely=0.24, relwidth=0.2, relheight=0.045)

                                                s_med_label=Label(page_frame, background="#ffedf3", text="Medical Condition ( if any ):", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_med_label.place(relx=0.03, rely=0.31)
                                                s_med_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=med_var)
                                                s_med_entry.place(relx=0.21, rely=0.31, relwidth=0.5, relheight=0.045)

                                                s_father_name_label=Label(page_frame, background="#ffedf3", text="Father's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_father_name_label.place(relx=0.03, rely=0.38)
                                                s_father_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_name_var)
                                                s_father_name_entry.place(relx=0.135, rely=0.38, relwidth=0.12, relheight=0.045)

                                                s_father_mob_label=Label(page_frame, background="#ffedf3", text="Father's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_father_mob_label.place(relx=0.285, rely=0.38)
                                                s_father_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_mob_no)
                                                s_father_mob_entry.place(relx=0.45, rely=0.38, relwidth=0.12, relheight=0.045)

                                                s_father_occ_label=Label(page_frame, background="#ffedf3", text="Father's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_father_occ_label.place(relx=0.6028, rely=0.38)
                                                s_father_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_occ_var)
                                                s_father_occ_entry.place(relx=0.745, rely=0.38, relwidth=0.12, relheight=0.045)

                                                s_father_off_label=Label(page_frame, background="#ffedf3", text="Father's Office Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_father_off_label.place(relx=0.03, rely=0.45)
                                                s_father_off_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=father_off_var)
                                                s_father_off_entry.place(relx=0.2, rely=0.45, relwidth=0.5, relheight=0.045)

                                                s_mother_name_label=Label(page_frame, background="#ffedf3", text="Mother's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mother_name_label.place(relx=0.03, rely=0.52)
                                                s_mother_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_name_var)
                                                s_mother_name_entry.place(relx=0.143, rely=0.52, relwidth=0.12, relheight=0.045)

                                                s_mother_mob_label=Label(page_frame, background="#ffedf3", text="Mother's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mother_mob_label.place(relx=0.2925, rely=0.52)
                                                s_mother_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_mob_no)
                                                s_mother_mob_entry.place(relx=0.4675, rely=0.52, relwidth=0.12, relheight=0.045)

                                                s_mother_occ_label=Label(page_frame, background="#ffedf3", text="Mother's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mother_occ_label.place(relx=0.6203, rely=0.52)
                                                s_mother_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_occ_var)
                                                s_mother_occ_entry.place(relx=0.77, rely=0.52, relwidth=0.12, relheight=0.045)

                                                s_mother_off_label=Label(page_frame, background="#ffedf3", text="Mother's Office Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_mother_off_label.place(relx=0.03, rely=0.59)
                                                s_mother_off_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=mother_off_var)
                                                s_mother_off_entry.place(relx=0.205, rely=0.59, relwidth=0.5, relheight=0.045)

                                                s_lg_name_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_lg_name_label.place(relx=0.03, rely=0.66)
                                                s_lg_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_name_var)
                                                s_lg_name_entry.place(relx=0.185, rely=0.66, relwidth=0.12, relheight=0.045)

                                                s_lg_mob_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_lg_mob_label.place(relx=0.3425, rely=0.66)
                                                s_lg_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_mob_no)
                                                s_lg_mob_entry.place(relx=0.5575, rely=0.66, relwidth=0.12, relheight=0.045)

                                                s_lg_occ_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Occupation:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_lg_occ_label.place(relx=0.705, rely=0.66)
                                                s_lg_occ_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_occ_var)
                                                s_lg_occ_entry.place(relx=0.8975, rely=0.66, relwidth=0.09, relheight=0.045)

                                                s_lg_add_label=Label(page_frame, background="#ffedf3", text="Local Guardian's Address:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_lg_add_label.place(relx=0.03, rely=0.73)
                                                s_lg_add_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=lg_add_var)
                                                s_lg_add_entry.place(relx=0.205, rely=0.73, relwidth=0.5, relheight=0.045)

                                                s_entry_label=Label(page_frame, background="#ffedf3", text="Entry Date:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_entry_label.place(relx=0.03, rely=0.8)
                                                s_entry_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=entry_date_var)
                                                s_entry_entry.place(relx=0.11, rely=0.8, relwidth=0.15, relheight=0.045)

                                                s_reg_label=Label(page_frame, background="#ffedf3", text="Registration Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_reg_label.place(relx=0.2875, rely=0.8)
                                                s_reg_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=s_reg_fee_var)
                                                s_reg_entry.place(relx=0.405, rely=0.8, relwidth=0.075, relheight=0.045)

                                                s_caution_label=Label(page_frame, background="#ffedf3", text="Caution Money:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_caution_label.place(relx=0.505, rely=0.8)
                                                s_caution_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=s_caution_var)
                                                s_caution_entry.place(relx=0.61, rely=0.8, relwidth=0.075, relheight=0.045)

                                                s_monthly_label=Label(page_frame, background="#ffedf3", text="Monthly Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                                s_monthly_label.place(relx=0.71, rely=0.8)
                                                s_monthly_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=s_monthly_fee_var)
                                                s_monthly_entry.place(relx=0.8, rely=0.8, relwidth=0.075, relheight=0.045)

                                                def delete_data():
                                                    cursor.execute(f"delete from student_info where Name='{stu_name.get()}' and DOB='{dob_var.get()}' and Mobile_No='{mob_no.get()}'")
                                                    cursor.execute(f"delete from fee_info where Name='{stu_name.get()}' and Mobile_No='{mob_no.get()}'")
                                                    db_connection.commit()

                                                    for i in room_info:
                                                        if i[0]==stu_name.get() and i[1]==mob_no.get():
                                                            cursor.execute(f"delete from rooms where Name='{stu_name.get()}' and Mobile_No='{mob_no.get()}'")
                                                            db_connection.commit()

                                                    now=datetime.datetime.now()

                                                    ins=0
                                                    for i in expense_info:
                                                        if i[0]==month_dict[now.month] and i[1]==str(now.year) and i[2]=="Caution Money Refund":
                                                            ins=1
                                                            break
                                                        else:
                                                            ins=0

                                                    if ins==0:
                                                        cursor.execute(f"insert into expenses values ('{month_dict[now.month]}', '{str(now.year)}', 'Caution Money Refund', '{s_caution_var.get()}')")
                                                        db_connection.commit()
                                                    else:
                                                        for i in expense_info:
                                                            if i[0]==month_dict[now.month] and i[1]==str(now.year) and i[2]=="Caution Money Refund":
                                                                Ref=int(i[3][1:])
                                                                cursor.execute(f"update expenses set Amount='{str(Ref+int(s_caution_var.get()[1:]))}' where Month='{month_dict[now.month]}' and Year='{str(now.year)}' and Category='Caution Money Refund'")
                                                                db_connection.commit()

                                                    call_func()
                                                    messagebox.showinfo("Action Successful", "Data Deleted Successfully!")
                                                    delete_edit_data()
                                                
                                                def edit_data():
                                                    cursor.execute(f"update student_info set Name='{stu_name.get()}', DOB='{dob_var.get()}', Mobile_No='{mob_no.get()}', Permanent_Address='{address_var.get()}', Educational_Qualification='{edu_var.get()}', Educational_Institution_or_Working_Place='{insti_var.get()}', Blood_Group='{menu_var_blood.get()}', Medical_Condition='{med_var.get()}', Father_Name='{father_name_var.get()}', Father_Mob_No='{father_mob_no.get()}',  Father_Occupation='{father_occ_var.get()}', Father_Office='{father_off_var.get()}', Mother_Name='{mother_name_var.get()}', Mother_Mob_No='{mother_mob_no.get()}', Mother_Occupation='{mother_occ_var.get()}', Mother_Office='{mother_off_var.get()}', L_G_Name='{lg_name_var.get()}', L_G_Mob_No='{lg_mob_no.get()}', L_G_Address='{lg_add_var.get()}', L_G_Occupation='{lg_occ_var.get()}', Entry_Date='{entry_date_var.get()}' where Name='{i[0]}' and DOB='{i[1]}' and Mobile_No='{i[2]}'")
                                                    db_connection.commit()
                                                    cursor.execute(f"update fee_info set Name='{stu_name.get()}', Mobile_No='{mob_no.get()}', Registration_Fee='{s_reg_fee_var.get()}', Caution_Money='{s_caution_var.get()}', Monthly_Fee='{s_monthly_fee_var.get()}' where Name='{fee_list[0][0]}' and Mobile_No='{fee_list[0][1]}'")
                                                    db_connection.commit()
                                                    call_func()
                                                    messagebox.showinfo("Action Successful", "Data Edited Successfully!")
                                                    delete_edit_data()

                                                edit_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), text="Edit Data", command=edit_data)
                                                edit_button.place(relx=0.4, rely=0.9, relheight=0.045)

                                                delete_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), text="Delete Data", command=delete_data)
                                                delete_button.place(relx=0.55, rely=0.9, relheight=0.045)

                                                break
                                    
                                    if flag==0:
                                        search_conditional_label.configure(text="No Match Found!", foreground="Red")
                                        search_conditional_label.place(relx=0.45, rely=0.5)

                                search_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.74, rely=0.03, relheight=0.052, relwidth=0.075)

                            def search_stu_data():

                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(restricted_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                fee_search_var=StringVar()

                                fee_search_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_search_var)
                                fee_search_entry.place(relx=0.03, rely=0.03, relwidth=0.7, relheight=0.045)

                                search_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                def fee_search():
                                    search_conditional_label.configure(text="", foreground="Red")
                                    search_conditional_label.place(relx=0.45, rely=0.5)
                                    
                                    cursor.execute("select * from student_info natural join fee_info")
                                    data_list_initial=cursor.fetchall()
                                    data_list=[]
                                    add=1
                                    if fee_search_var.get()=="":
                                        data_list=data_list_initial
                                    else:
                                        for i in data_list_initial:
                                            for j in i:
                                                if j==fee_search_var.get() or fee_search_var.get() in j or j==fee_search_var.get().lower() or fee_search_var.get().lower() in j or j==fee_search_var.get().upper() or fee_search_var.get().upper() in j or j==fee_search_var.get().title() or fee_search_var.get().title() in j:
                                                    for k in data_list:
                                                        if k!=i:
                                                            add=1
                                                        else:
                                                            add=0
                                                    if add==1:
                                                        data_list.append(i)
                                    
                                    if len(data_list)==0:
                                        search_conditional_label.configure(text="No Match Found!", foreground="Red")
                                        search_conditional_label.place(relx=0.45, rely=0.5)
                                    else:
                                        cols=("Name", "Mobile Number", "Date of Birth", "Permanent Address", "Educational Qualification", "Educational Institution/Office", "Blood Group", "Medical Condition", "Father's Name", "Father's Mobile Number", "Father's Occupation", "Father's Office", "Mother's Name", "Mother's Mobile Number", "Mother's Occupation", "Mother's Office", "Local Guardian's Name", "Local Guardian's Mobile Number", "Local Guardian's Address", "Local Guardian's Occupation", "Entry Date", "Registration Fee", "Caution Money", "Monthly Fee")

                                        search_result=ttk.Treeview(page_frame, columns=cols, show="headings")
                                        for i in cols:
                                            search_result.heading(i, text=i)

                                        for i in data_list:
                                            search_result.insert("", END, values=i)

                                        y_scroll=Scrollbar(page_frame, command=search_result.yview)

                                        x_scroll=Scrollbar(page_frame, command=search_result.xview, orient="horizontal")

                                        search_result.config(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

                                        search_result.place(relx=0.03, rely=0.15, relheight=0.8, relwidth=0.94)
                                        y_scroll.place(relx=0.971, rely=0.15, relheight=0.8, relwidth=0.01)
                                        x_scroll.place(relx=0.03, rely=0.951, relheight=0.01, relwidth=0.94)

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=fee_search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.74, rely=0.0275, relheight=0.052, relwidth=0.075)

                            def fee_add_data():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(restricted_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.85, rely=0.01, relheight=0.15, relwidth=0.1)

                                fee_name_var=StringVar()
                                fee_mob_no_var=StringVar()
                                fee_month_var=StringVar()
                                fee_year_var=StringVar()
                                fee_monthly_fee_var=StringVar()
                                fee_date_var=StringVar()

                                now=datetime.datetime.now()

                                global flag_2
                                flag_2=0

                                def check_func():
                                    global flag_2
                                    if flag_2==0:
                                        for i in fee_info:
                                            if i[0]==fee_name_var.get() and i[1]==fee_mob_no_var.get():
                                                fee_monthly_fee_var.set(i[4])
                                                fee_date_var.set(str(now.day)+"/"+str(now.month)+"/"+str(now.year))
                                                fee_year_var.set(str(now.year))
                                                fee_month_var.set(month_dict[now.month])
                                                fee_monthly_entry.configure(state="disabled")
                                                flag_2=1
                                                break
                                        fee_conditional_label.after(1000, check_func)

                                fee_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_name_label.place(relx=0.03, rely=0.03)
                                fee_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_name_var)
                                fee_name_entry.place(relx=0.075, rely=0.03, relwidth=0.12, relheight=0.045)

                                fee_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_mob_label.place(relx=0.23, rely=0.03)
                                fee_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_mob_no_var)
                                fee_mob_entry.place(relx=0.335, rely=0.03, relwidth=0.12, relheight=0.045)

                                fee_month_label=Label(page_frame, background="#ffedf3", text="Month:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_month_label.place(relx=0.03, rely=0.1)
                                fee_month_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_month_var)
                                fee_month_entry.place(relx=0.08, rely=0.1, relwidth=0.1, relheight=0.045)

                                fee_year_label=Label(page_frame, background="#ffedf3", text="Year:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_year_label.place(relx=0.21, rely=0.1)
                                fee_year_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_year_var)
                                fee_year_entry.place(relx=0.25, rely=0.1, relwidth=0.075, relheight=0.045)

                                fee_monthly_label=Label(page_frame, background="#ffedf3", text="Monthly Fee:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_monthly_label.place(relx=0.3575, rely=0.1)
                                fee_monthly_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_monthly_fee_var)
                                fee_monthly_entry.place(relx=0.445, rely=0.1, relwidth=0.075, relheight=0.045)

                                fee_date_label=Label(page_frame, background="#ffedf3", text="Paid On:", font=("Haettenschweiler", 25), foreground="#811c98")
                                fee_date_label.place(relx=0.03, rely=0.17)
                                fee_date_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_date_var)
                                fee_date_entry.place(relx=0.085, rely=0.17, relwidth=0.1, relheight=0.045)

                                def fee_status_button():
                                    fee_set=[]
                                    for i in fee_data_set:
                                        if i[0]==fee_name_var.get() and i[1]==fee_mob_no_var.get():
                                            fee_set.append(i)

                                    for i in fee_info:
                                        if i[0]==fee_name_var.get() and i[1]==fee_mob_no_var.get():
                                            if fee_name_var.get()!="" and fee_mob_no_var.get()!="" and fee_month_var.get()!="" and fee_year_var.get()!="" and fee_date_var.get()!="":
                                                if (fee_name_var.get(), fee_mob_no_var.get(), fee_month_var.get(), fee_year_var.get(), fee_date_var.get()) not in fee_set:
                                                    cursor.execute(f"insert into fee_stats values ('{fee_name_var.get()}', '{fee_mob_no_var.get()}', '{fee_month_var.get()}', '{fee_year_var.get()}', '{fee_date_var.get()}')")
                                                    db_connection.commit()
                                                    for i in total_fee_info:
                                                        if i[0]==fee_month_var.get() and i[1]==fee_year_var.get():
                                                            cursor.execute(f"update monthly_total_fee set Total_Fee='₹{str(int(i[2][1:])+int(fee_monthly_fee_var.get()[1:]))}' where Month='{fee_month_var.get()}' and Year='{fee_year_var.get()}'")
                                                            db_connection.commit()
                                                            messagebox.showinfo("Action Successful", "Data Entry Successful!")
                                                            call_func()
                                                            fee_add_data()
                                                            break
                                                    else:
                                                        cursor.execute(f"insert into monthly_total_fee values ('{fee_month_var.get()}', '{fee_year_var.get()}', '{fee_monthly_fee_var.get()}')")
                                                        db_connection.commit()
                                                        messagebox.showinfo("Action Successful", "Data Entry Successful!")
                                                        call_func()
                                                        fee_add_data()
                                                        break
                                                else:
                                                    fee_conditional_label.configure(text="Data Already Exists!", foreground="Red")
                                                    fee_conditional_label.place(relx=0.44, rely=0.87)
                                                    break
                                            else:
                                                fee_conditional_label.configure(text="Please Enter all Essential Details!", foreground="Red")
                                                fee_conditional_label.place(relx=0.4, rely=0.87)
                                                break
                                    else:
                                        fee_conditional_label.configure(text="Student Not Found!", foreground="Red")
                                        fee_conditional_label.place(relx=0.45, rely=0.87)
                                                
                                fee_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))
                                check_func()

                                f_add_button=Button(page_frame, text="Add Data", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3",command=fee_status_button)
                                f_add_button.place(relx=0.475, rely=0.8, relheight=0.06)

                            def fee_search_data():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(restricted_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                fee_search_var=StringVar()
                                fee_search_var.set("")

                                fee_search_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_search_var)
                                fee_search_entry.place(relx=0.03, rely=0.03, relwidth=0.7, relheight=0.045)

                                search_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                def fee_search():
                                    search_conditional_label.configure(text="", foreground="Red")
                                    search_conditional_label.place(relx=0.45, rely=0.5)
                                    cursor.execute("select Name, Mobile_No, Month, Year, Monthly_Fee, Paid_On from fee_stats natural join fee_info")
                                    data_list_initial=cursor.fetchall()
                                    data_list=[]
                                    add=1
                                    if fee_search_var.get()=="":
                                        data_list=data_list_initial
                                    else:
                                        for i in data_list_initial:
                                            for j in i:
                                                if j==fee_search_var.get() or fee_search_var.get() in j or j==fee_search_var.get().lower() or fee_search_var.get().lower() in j or j==fee_search_var.get().upper() or fee_search_var.get().upper() in j or j==fee_search_var.get().title() or fee_search_var.get().title() in j:
                                                    for k in data_list:
                                                        if k!=i:
                                                            add=1
                                                        else:
                                                            add=0
                                                    if add==1:
                                                        data_list.append(i)
                                    
                                    if len(data_list)==0:
                                        search_conditional_label.configure(text="No Match Found!", foreground="Red")
                                        search_conditional_label.place(relx=0.45, rely=0.5)
                                    else:
                                        cols=("Name", "Mobile Number", "Month", "Year", "Monthly Fee", "Paid On")

                                        search_result=ttk.Treeview(page_frame, columns=cols, show="headings")
                                        search_result.heading("Name", text="Name")
                                        search_result.heading("Mobile Number", text="Mobile Number")
                                        search_result.heading("Month", text="Month")
                                        search_result.heading("Year", text="Year")
                                        search_result.heading("Monthly Fee", text="Monthly Fee")
                                        search_result.heading("Paid On", text="Paid On")

                                        for i in data_list:
                                            search_result.insert("", END, values=i)

                                        y_scroll=Scrollbar(page_frame, command=search_result.yview)

                                        search_result.config(yscrollcommand=y_scroll.set)

                                        search_result.place(relx=0.03, rely=0.15, relheight=0.825, relwidth=0.94)
                                        y_scroll.place(relx=0.971, rely=0.15, relheight=0.825, relwidth=0.01)

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=fee_search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.74, rely=0.0275, relheight=0.052, relwidth=0.075)

                            def allot_room():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(restricted_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                r_name_var=StringVar()
                                r_mob_var=StringVar()
                                r_room_var=StringVar()
                                r_bed_var=StringVar()

                                r_room_var.set("Select-")
                                r_bed_var.set("Select-")

                                r_name_label=Label(page_frame, background="#ffedf3", text="Name:", font=("Haettenschweiler", 25), foreground="#811c98")
                                r_name_label.place(relx=0.03, rely=0.03)
                                r_name_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=r_name_var)
                                r_name_entry.place(relx=0.075, rely=0.03, relwidth=0.12, relheight=0.045)

                                r_mob_label=Label(page_frame, background="#ffedf3", text="Mobile Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                r_mob_label.place(relx=0.23, rely=0.03)
                                r_mob_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=r_mob_var)
                                r_mob_entry.place(relx=0.335, rely=0.03, relwidth=0.12, relheight=0.045)

                                room_no=[]
                                for i in room_dict:
                                    room_no.append(i)
                                
                                for i in room_no:
                                    cursor.execute(f"select * from rooms where Room_No='{i}'")
                                    bed_check=cursor.fetchall()
                                    if len(bed_check)==len(room_dict[i]):
                                        room_no.remove(i)
                                
                                room_no.insert(0, "Select-")

                                def bed_count():
                                    if r_room_var.get()!="Select-":
                                        room=int(r_room_var.get())
                                        total_beds=room_dict[room]
                                        cursor.execute(f"select * from rooms where Room_No='{r_room_var.get()}'")
                                        occ_beds=cursor.fetchall()
                                        if len(occ_beds)!=0:
                                            for i in occ_beds:
                                                if i[3] in total_beds:
                                                    total_beds.remove(i[3])
                                        
                                        if "Select-" not in total_beds:
                                            total_beds.insert(0, "Select-")
                                        
                                        r_bed_label=Label(page_frame, background="#ffedf3", text="Bed Number:", font=("Haettenschweiler", 25), foreground="#811c98")
                                        r_bed_label.place(relx=0.64, rely=0.03)
                                        arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                        r_bed_menu=OptionMenu(page_frame, r_bed_var, *total_beds)
                                        r_bed_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), borderwidth=0)
                                        r_bed_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                        r_bed_menu.place(relx=0.725, rely=0.03, relwidth=0.085, relheight=0.05)
                                        r_bed_menu.image=arrow

                                    cd_label.after(1000, bed_count)
                                
                                r_room_label=Label(page_frame, background="#ffedf3", text="Room:", font=("Haettenschweiler", 25), foreground="#811c98")
                                r_room_label.place(relx=0.48, rely=0.03)
                                arrow = PhotoImage(file='Images/Drop_Down_Arrow.png')
                                r_room_menu=OptionMenu(page_frame, r_room_var, *room_no)
                                r_room_menu.config(compound="right", indicatoron=0, image=arrow, bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25), borderwidth=0)
                                r_room_menu["menu"].config(bg="#ffedf3", fg="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 25))
                                r_room_menu.place(relx=0.525, rely=0.03, relwidth=0.085, relheight=0.05)
                                r_room_menu.image=arrow

                                cd_label=Label(page_frame)
                                bed_count()

                                def allot_btn():

                                    conditional_label.config(text="", foreground="Red")
                                    conditional_label.place(rely=0.87, relx=0.35)

                                    if r_name_var.get()!="" and r_mob_var.get()!="" and r_room_var.get()!="Select-" and r_bed_var.get()!="Select-":
                                        for i in room_info:
                                            if i[0]==r_name_var.get() and i[1]==r_mob_var.get():
                                                conditional_label.config(text="Room Already Alloted!", foreground="Red")
                                                conditional_label.place(rely=0.87, relx=0.4175)
                                                break
                                        else:
                                            for i in student_info:
                                                if i[0]==r_name_var.get() and i[2]==r_mob_var.get():
                                                    cursor.execute(f"insert into rooms values ('{r_name_var.get()}', '{r_mob_var.get()}', '{r_room_var.get()}', '{r_bed_var.get()}')")
                                                    db_connection.commit()
                                                    call_func()
                                                    messagebox.showinfo("Action Succesful", "Room Alloted Successfully!")
                                                    r_name_var.set("")
                                                    r_mob_var.set("")
                                                    r_room_var.set("Select-")
                                                    r_bed_var.set("Select-")
                                                    break
                                            else:
                                                conditional_label.config(text="Student Data does not Exist!", foreground="Red")
                                                conditional_label.place(rely=0.87, relx=0.395)
                                    else:
                                        conditional_label.config(text="Please Enter All Essential Details!", foreground="Red")
                                        conditional_label.place(rely=0.87, relx=0.38)
                                
                                conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                r_all_button=Button(page_frame, text="Allot Room", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", command=allot_btn)
                                r_all_button.place(relx=0.45, rely=0.8, relheight=0.06)

                            def search_room():
                                global page_frame
                                page_frame.destroy()

                                page_frame=Frame(restricted_root, background="#ffedf3")
                                page_frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

                                main_photo_label=Label(page_frame, background="#ffedf3")
                                class Example(Frame):
                                    def __init__(self, master, *pargs):
                                        Frame.__init__(self, master, *pargs)

                                        self.image = Image.open("Images/Logo_2.png")
                                        self.img_copy= self.image.copy()

                                        self.background_image = ImageTk.PhotoImage(self.image)

                                        self.background = Label(self, image=self.background_image)
                                        self.background.pack(fill=BOTH, expand=YES)
                                        self.background.bind('<Configure>', self._resize_image)

                                    def _resize_image(self,event):

                                        new_width = event.width
                                        new_height = event.height

                                        self.image = self.img_copy.resize((new_width, new_height))

                                        self.background_image = ImageTk.PhotoImage(self.image)
                                        self.background.configure(image =  self.background_image)

                                e = Example(main_photo_label)
                                e.pack(fill=BOTH, expand=YES)
                                main_photo_label.place(relx=0.875, rely=0.01, relheight=0.15, relwidth=0.105)

                                fee_search_var=StringVar()
                                fee_search_var.set("")

                                fee_search_entry=Entry(page_frame, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", textvariable=fee_search_var)
                                fee_search_entry.place(relx=0.03, rely=0.03, relwidth=0.7, relheight=0.045)

                                search_conditional_label=Label(page_frame, background="#ffedf3", font=("Haettenschweiler", 25))

                                def fee_search():
                                    search_conditional_label.configure(text="", foreground="Red")
                                    search_conditional_label.place(relx=0.45, rely=0.5)
                                    data_list=[]
                                    add=1
                                    if fee_search_var.get()=="":
                                        data_list=room_info
                                    else:
                                        for i in room_info:
                                            for j in i:
                                                if j==fee_search_var.get() or fee_search_var.get() in j or j==fee_search_var.get().lower() or fee_search_var.get().lower() in j or j==fee_search_var.get().upper() or fee_search_var.get().upper() in j or j==fee_search_var.get().title() or fee_search_var.get().title() in j:
                                                    for k in data_list:
                                                        if k!=i:
                                                            add=1
                                                        else:
                                                            add=0
                                                    if add==1:
                                                        data_list.append(i)

                                    if len(data_list)==0:
                                        search_conditional_label.configure(text="No Match Found!", foreground="Red")
                                        search_conditional_label.place(relx=0.45, rely=0.5)
                                    else:
                                        cols=("Name", "Mobile Number", "Room Number", "Bed")

                                        search_result=ttk.Treeview(page_frame, columns=cols, show="headings")
                                        search_result.heading("Name", text="Name")
                                        search_result.heading("Mobile Number", text="Mobile Number")
                                        search_result.heading("Room Number", text="Room Number")
                                        search_result.heading("Bed", text="Bed")

                                        for i in data_list:
                                            search_result.insert("", END, values=i)

                                        y_scroll=Scrollbar(page_frame, command=search_result.yview)

                                        search_result.config(yscrollcommand=y_scroll.set)

                                        search_result.place(relx=0.03, rely=0.15, relheight=0.825, relwidth=0.94)
                                        y_scroll.place(relx=0.971, rely=0.15, relheight=0.825, relwidth=0.01)

                                img=PhotoImage(file="Images/Search_Logo.png")
                                search_photo_button=Button(page_frame, background="#ffedf3", foreground="#811c98", activebackground="#811c98", activeforeground="#ffedf3", font=("Haettenschweiler", 20), image=img, text="Search", compound=RIGHT, command=fee_search)
                                search_photo_button.image=img
                                search_photo_button.place(relx=0.74, rely=0.0275, relheight=0.052, relwidth=0.075)

                            MENU=Menu(restricted_root, background="#ffedf3", foreground="#811c98")
                            mainmenu=Menu(MENU, tearoff=False, background="#ffedf3", foreground="#811c98")
                            MENU.add_cascade(label="Main Menu", menu=mainmenu, background="#ffedf3", foreground="#811c98")

                            mainmenu.add_command(label="Home", background="#ffedf3", foreground="#811c98", command=home)

                            sub_menu_data=Menu(mainmenu, tearoff=False, background="#ffedf3", foreground="#811c98")
                            sub_menu_data.add_command(label="Add Data", background="#ffedf3", foreground="#811c98", command=add_data)
                            sub_menu_data.add_command(label="Delete/Edit Data", background="#ffedf3", foreground="#811c98", command=delete_edit_data)
                            sub_menu_data.add_command(label="Search Data", background="#ffedf3", foreground="#811c98", command=search_stu_data)
                            mainmenu.add_cascade(label="Data Management", background="#ffedf3", foreground="#811c98", menu=sub_menu_data)

                            sub_menu=Menu(mainmenu, tearoff=False, background="#ffedf3", foreground="#811c98")
                            sub_menu.add_command(label="Add Fee Data", background="#ffedf3", foreground="#811c98", command=fee_add_data)
                            sub_menu.add_command(label="Search Fee Data", background="#ffedf3", foreground="#811c98", command=fee_search_data)
                            mainmenu.add_cascade(label="Fee Management", background="#ffedf3", foreground="#811c98", menu=sub_menu)

                            room_sub_menu=Menu(mainmenu, tearoff=False, background="#ffedf3", foreground="#811c98")
                            room_sub_menu.add_command(label="Allot Room", background="#ffedf3", foreground="#811c98", command=allot_room)
                            room_sub_menu.add_command(label="View Room Details", background="#ffedf3", foreground="#811c98", command=search_room)
                            mainmenu.add_cascade(label="Room Management", background="#ffedf3", foreground="#811c98", menu=room_sub_menu)

                            mainmenu.add_separator()

                            mainmenu.add_command(label="Log Out", background="#ffedf3", foreground="#811c98", command=log_out)

                            mainmenu.add_command(label="Exit", background="#ffedf3", foreground="#811c98", command=exit)

                            restricted_root.config(menu=MENU)

                            home()

                            restricted_root.mainloop()

                            break

                else:
                    login_condition_label.configure(text="Access Denied!", foreground="Red")

            photo_label=Label(root_login, background="#ffedf3")
            class Example(Frame):
                def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)

                    self.image = Image.open("Images/Logo_2.png")
                    self.img_copy= self.image.copy()

                    self.background_image = ImageTk.PhotoImage(self.image)

                    self.background = Label(self, image=self.background_image)
                    self.background.pack(fill=BOTH, expand=YES)
                    self.background.bind('<Configure>', self._resize_image)

                def _resize_image(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image = self.img_copy.resize((new_width, new_height))

                    self.background_image = ImageTk.PhotoImage(self.image)
                    self.background.configure(image =  self.background_image)

            e = Example(photo_label)
            e.pack(fill=BOTH, expand=YES)
            photo_label.place(relx=0.375, rely=0.05, relheight=0.4, relwidth=0.285)

            user_label=Label(root_login, background="#ffedf3", text="Username:", font=("Haettenschweiler", 25), foreground="#811c98")
            user_label.place(relx=0.39, rely=0.5)
            user_entry=Entry(root_login, textvariable=user_var, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", width=20)
            user_entry.place(relx=0.465, rely=0.5, relheight=0.045)
            pass_label=Label(root_login, background="#ffedf3", text="Password:", font=("Haettenschweiler", 25), foreground="#811c98")
            pass_label.place(relx=0.39, rely=0.55)
            pass_entry=Entry(root_login, textvariable=pass_var, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", width=20, show="*")
            pass_entry.place(relx=0.465, rely=0.55, relheight=0.045)

            login_button=Button(root_login, text="Login", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", command=login_function, activebackground="#811c98", activeforeground="#ffedf3")
            login_button.place(relx=0.4925, rely=0.65, relheight=0.06)

            login_condition_label=Label(root_login, background="#ffedf3", font=("Haettenschweiler", 25))
            login_condition_label.place(relx=0.457, rely=0.75)

            root_login.mainloop()

    main_function()

try:
    file=open("Password.dat", "rb")
    pswd=pickle.load(file)

    global db_connection
    db_connection=mysql.connector.connect(host="localhost", user="root", password=pswd)
    cursor=db_connection.cursor()
    db_func()
    
except:
    root_db=Tk()
    root_db.title("Dream Catcher Girl's Hostel")
    root_db.state("zoomed")
    root_db.iconbitmap("Logo_3.ico")
    root_db.configure(background="#ffedf3")

    db_photo_label=Label(root_db, background="#ffedf3")
    class Example(Frame):
                def __init__(self, master, *pargs):
                    Frame.__init__(self, master, *pargs)

                    self.image = Image.open("Images/Logo_2.png")
                    self.img_copy= self.image.copy()

                    self.background_image = ImageTk.PhotoImage(self.image)

                    self.background = Label(self, image=self.background_image)
                    self.background.pack(fill=BOTH, expand=YES)
                    self.background.bind('<Configure>', self._resize_image)

                def _resize_image(self,event):

                    new_width = event.width
                    new_height = event.height

                    self.image = self.img_copy.resize((new_width, new_height))

                    self.background_image = ImageTk.PhotoImage(self.image)
                    self.background.configure(image =  self.background_image)

    e = Example(db_photo_label)
    e.pack(fill=BOTH, expand=YES)
    db_photo_label.place(relx=0.375, rely=0.05, relheight=0.4, relwidth=0.285)

    password=StringVar()

    db_label=Label(root_db, background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", text="Database Password:")
    db_label.place(relx=0.38, rely=0.519)
    database_password=Entry(root_db, textvariable=password, background="#ffedf3", font=("Anton", 20), foreground="#811c98", insertbackground="#811c98", show="*")
    database_password.place(relheight=0.043, relwidth=0.12, relx=0.52, rely=0.519)

    def button_command():
        pswd=password.get()
        file=open("Password.dat", "wb")
        pickle.dump(pswd, file)
        file.close()
        root_db.destroy()

        global db_connection
        global cursor
        db_connection=mysql.connector.connect(host="localhost", user="root", password=pswd)
        cursor=db_connection.cursor()
        db_func()

    ok_button=Button(root_db, text="OK", background="#ffedf3", font=("Haettenschweiler", 25), foreground="#811c98", command=button_command)
    ok_button.place(relheight=0.045, relwidth=0.06, relx=0.48, rely=0.68)

    root_db.mainloop()

db_connection.close()