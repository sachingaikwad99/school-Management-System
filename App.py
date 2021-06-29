from tkinter import *
from PIL import ImageTk
from tkinter import messagebox, ttk
import mysql.connector
import time


class App:
    def __init__(self, root):
        global total, total2, total3, total4

        self.root = root
        self.root.title('School Management System')
        self.root.geometry('1536x864+0+0')
        self.root.resizable(False, False)
        self.root.config(bg="#CAD1D9")

        # ======================================Title frames ===================================================
        titleFrame = Frame(self.root, bd=3, relief=GROOVE, bg="#CAD1D9")
        titleFrame.place(x=10, y=5, width=1515, height=100)

        self.titleImage = PhotoImage(file='Images\\main_logo.png')

        imageLabel = Label(titleFrame, image=self.titleImage)
        imageLabel.pack(padx=40, side=LEFT)

        titleLabel = Label(titleFrame, text='UNIVERSAL PRIMARY SCHOOL, UMARKHED.', font=('times new roman', 30, 'bold'),
                           fg='#dd0000', bg="#CAD1D9", bd=2, padx=0, pady=25)
        titleLabel.pack()

        # ------------------------ date time  label ---------------------------------------------------------------
        self.date = time.strftime('%d/%m/%Y')
        self.time = time.strftime('%H:%M:%S')

        dateTimeLabel = Label(self.root, font=('times new roman', 15, 'bold'), bg='#CAD1D9')
        dateTimeLabel.place(x=160, y=35)

        dateTimeLabel.config(text=f"Date: {self.date}\nTime : {self.time}", )
        # ======================================Menu  frames ===================================================
        menuFrame = LabelFrame(self.root, text='Manage', bd=3, relief=GROOVE, font=('times new roman', 15, 'bold'),
                               fg='#dd0000', bg="#CAD1D9")
        menuFrame.place(x=10, y=105, width=1515, height=80)
        # ================================ Buttons =============================================================
        studentButton = Button(menuFrame, text="Student", font=("times new roman", 15, "bold"), padx=20, pady=10,
                               cursor="hand2", command=self.student)
        studentButton.place(x=50, y=5, width=200, height=40)

        teacherButton = Button(menuFrame, text="Teacher", font=("times new roman", 15, "bold"), padx=20, pady=10,
                               cursor="hand2", command=self.teacher)
        teacherButton.place(x=250, y=5, width=200, height=40)

        subjectButton = Button(menuFrame, text="Subject", font=("times new roman", 15, "bold"), padx=20, pady=10,
                               cursor="hand2", command=self.subject)
        subjectButton.place(x=450, y=5, width=200, height=40)

        classesButton = Button(menuFrame, text="Classes", font=("times new roman", 15, "bold"), padx=20, pady=10,
                               cursor="hand2", command=self.classes)
        classesButton.place(x=650, y=5, width=200, height=40)

        resultButton = Button(menuFrame, text="Results", font=("times new roman", 15, "bold"), padx=20, pady=10,
                              cursor="hand2", command=self.result)
        resultButton.place(x=850, y=5, width=200, height=40)

        clubsButton = Button(menuFrame, text="Clubs", font=("times new roman", 15, "bold"), padx=20, pady=10,
                             cursor="hand2", command=self.clubs)
        clubsButton.place(x=1050, y=5, width=200, height=40)

        logoutButton = Button(menuFrame, text="Log Out", font=("times new roman", 15, "bold"), padx=20, pady=10,
                              cursor="hand2", command=self.exit)
        logoutButton.place(x=1250, y=5, width=200, height=40)

        # ======================================Dashboard frames ===================================================
        dashBoardFrame = LabelFrame(self.root, text='Dashboard', bd=3, relief=GROOVE,
                                    font=('times new roman', 15, 'bold'), fg='#dd0000', bg="#CAD1D9")
        dashBoardFrame.place(x=10, y=190, width=1515, height=580)
        # =========  fetching data and display on dashboard ========================================================
        # fetch data from tables and show on dashboard
        import mysql.connector
        import mysql.connector
        myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                       database='School_Management_System')
        myCursor = myDb.cursor()
        myCursor.execute("SELECT COUNT(student_rollno) FROM student")
        studentTotal = myCursor.fetchone()
        for value1 in studentTotal:
            total = value1
        myCursor.execute("SELECT COUNT(teacher_id) FROM teacher")
        teacherTotal = myCursor.fetchone()
        for value2 in teacherTotal:
            total2 = value2
        myCursor.execute("SELECT COUNT(subject_id) FROM subjects")
        subjectTotal = myCursor.fetchone()
        for value3 in subjectTotal:
            total3 = value3
        myCursor.execute("SELECT COUNT(class_id) FROM class")
        classesTotal = myCursor.fetchone()
        for value4 in classesTotal:
            total4 = value4
        myDb.commit()

        self.bgImage = ImageTk.PhotoImage(file="Images//dashboard_img.jpg")
        bgImageLabel = Label(dashBoardFrame, image=self.bgImage)
        bgImageLabel.place(x=0, y=0, relwidth=1, relheight=1)

        # ------------------------- total & student label -------------------------------------------------------------
        self.studentImage = ImageTk.PhotoImage(file="Images//student.png")
        titleStudentLabel = Label(dashBoardFrame, text='Student', font=('times new roman', 20, 'bold'), bd=3,
                                  bg='#1EA362', relief=GROOVE, padx=60, pady=10, image=self.studentImage, compound=LEFT)
        titleStudentLabel.place(x=50, y=50)

        studentTotalLabel = Label(dashBoardFrame, font=('times new roman', 20, 'bold'), bd=3, bg='#1EA362',
                                  relief=GROOVE)
        studentTotalLabel.place(x=50, y=120, width=325, height=100)
        studentTotalLabel.config(text=f'Total : {total}')
        # --------------------total & teacher label---------------------------------------------------------------------
        self.teacherImage = ImageTk.PhotoImage(file="Images//teacher.png")
        titleTeacherLabel = Label(dashBoardFrame, text='Teacher', font=('times new roman', 20, 'bold'), bd=3,
                                  bg="#DD5347", relief=GROOVE, padx=60, pady=10, image=self.teacherImage, compound=LEFT)
        titleTeacherLabel.place(x=420, y=50)

        teacherTotalLabel = Label(dashBoardFrame, font=('times new roman', 20, 'bold'), bd=3, bg="#DD5347",
                                  relief=GROOVE)
        teacherTotalLabel.place(x=420, y=120, width=330, height=100)
        teacherTotalLabel.config(text=f'Total : {total2}')
        # --------------------total & subject label---------------------------------------------------------------------

        self.subjectImage = ImageTk.PhotoImage(file="Images//subject.png")
        titleSubjectLabel = Label(dashBoardFrame, text='Subject', font=('times new roman', 20, 'bold'), bd=3,
                                  bg="#B460E6", relief=GROOVE, padx=60, pady=10, image=self.subjectImage, compound=LEFT)
        titleSubjectLabel.place(x=800, y=50)

        subjectTotalLabel = Label(dashBoardFrame, font=('times new roman', 20, 'bold'), bd=3, bg="#B460E6",
                                  relief=GROOVE)
        subjectTotalLabel.place(x=800, y=120, width=322, height=100)
        subjectTotalLabel.config(text=f'Total : {total3}')
        # --------------------total & classes label---------------------------------------------------------------------

        self.classesImage = ImageTk.PhotoImage(file="Images//classes.png")
        titleClassesLabel = Label(dashBoardFrame, text='Classes', font=('times new roman', 20, 'bold'), bd=3,
                                  bg="#4B8BF4", relief=GROOVE, padx=60, pady=10, image=self.classesImage, compound=LEFT)
        titleClassesLabel.place(x=50, y=250)

        classesTotalLabel = Label(dashBoardFrame, font=('times new roman', 20, 'bold'), bd=3, bg="#4B8BF4",
                                  relief=GROOVE)
        classesTotalLabel.place(x=50, y=320, width=322, height=100)
        classesTotalLabel.config(text=f'Total : {total4}')
        # --------------------total & clubs label---------------------------------------------------------------------

        self.clubImage = ImageTk.PhotoImage(file="Images//clubs.png")
        titleClubLabel = Label(dashBoardFrame, text='Clubs', font=('times new roman', 20, 'bold'), bd=3,
                               bg="#FFCD42", relief=GROOVE, padx=68, pady=10, image=self.clubImage, compound=LEFT)
        titleClubLabel.place(x=420, y=250)

        clubTotalLabel = Label(dashBoardFrame, font=('times new roman', 20, 'bold'), bd=3, bg="#FFCD42",
                               relief=GROOVE)
        clubTotalLabel.place(x=420, y=320, width=330, height=100)
        clubTotalLabel.config(text=f'Total : {0}')

        # --------------------total & clubs label---------------------------------------------------------------------
        self.resultImage = ImageTk.PhotoImage(file="Images//results.png")
        titleResultLabel = Label(dashBoardFrame, text='Results', font=('times new roman', 20, 'bold'), bd=3,
                                 bg="#D13762", relief=GROOVE, padx=63, pady=10, image=self.resultImage, compound=LEFT)
        titleResultLabel.place(x=800, y=250)

        resultOverAllLabel = Label(dashBoardFrame, font=('times new roman', 20, 'bold'), bd=3, bg="#D13762",
                                   relief=GROOVE)
        resultOverAllLabel.place(x=800, y=320, width=330, height=100)
        resultOverAllLabel.config(text=f'OverAll : {94}')


# ======================================footer frames ===================================================
        footerFrame = Frame(self.root, bd=3, relief=GROOVE, bg='#CAD1D9')
        footerFrame.place(x=10, y=780, width=1515, height=50)

        footerInfoLabel = Label(footerFrame, text="Developed by Sachin\n All right reserved.",
                                font=("times new roman", 12, 'bold'),  bg="#CAD1D9")
        footerInfoLabel.place(x=700, y=0)
# ===============================  All methods ===========================================================

    def student(self):
        top = Toplevel()

        # -----------------------Clear all Field ----------------------------------------------------------------------

        def clear():
            varRollNumber.set('')
            varName.set('')
            varClass.set('')
            varGender.set('Select')
            varMobileNo.set('')
            varDob.set('')
            textAddress.delete('1.0', END)

        # ----------------- clear recently search field ----------------------------------------------------------------

        def reset():
            varSearch.set("Select")
            varValue.set('')

        # ---------------------- Data insertion into table -------------------------------------------------------------
        def addData():

            if varRollNumber.get() == '' or varName.get() == '' or varClass.get() == '' or varGender.get() == 'Select' \
                    or varMobileNo.get() == '' or varDob.get() == '' or textAddress.get("1.0", END) == '':
                messagebox.showerror('Error', 'All Fields are Required', parent=top)
            else:
                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()
                sql = 'INSERT INTO student(student_rollno, student_name, student_class, student_gender, ' \
                      'student_mobileno, student_dob, student_address) VALUES (%s, %s, %s, %s, %s, %s, %s)'

                val = (varRollNumber.get(), varName.get(), varClass.get(), varGender.get(), varMobileNo.get(),
                       varDob.get(), textAddress.get("1.0", END))
                myCursor.execute(sql, val)
                myDb.commit()
                messagebox.showinfo('Success', "Data Inserted Successfully !", parent=top)
                clear()
# --------------------------------Backend data  deletion from student table -------------------------------------------

        def deleteData():
            if varRollNumber.get() == '':
                messagebox.showerror('Error', 'Please enter the Roll Number to Delete data', parent=top)
            else:
                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()
                sql = "DELETE  FROM student WHERE student_rollno = '%s'"
                val = varRollNumber.get()
                myCursor.execute(sql % val)
                myDb.commit()
                messagebox.showinfo("Success", "Student's Data Deleted Successfully !", parent=top)
                clear()

        # --------------------------------Backend  data show from student table ----------------------------------------

        def showAll():
            import mysql.connector
            myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                           database='School_Management_System')
            myCursor = myDb.cursor()
            treeView.delete(*treeView.get_children())
            myCursor.execute("SELECT * FROM student")
            rows = myCursor.fetchall()
            for r in rows:
                treeView.insert('', 'end', values=r)
            myDb.commit()

        # --------------------------------backend  data  search from student table -------------------------------------
        def searchStudent():

            if varSearch.get() == 'Select' and varValue.get() == '':
                messagebox.showerror("Error", "Please Enter valid Data to Search !", parent=top)
            else:

                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()

                myCursor.execute("SELECT * FROM student WHERE student_rollno = '%s' or student_name ='%s'" %
                                 (varValue.get(), varValue.get()))
                rows1 = myCursor.fetchall()
                if not rows1:
                    messagebox.showerror("Not Found", "No such record or Student  Found", parent=top)
                    reset()

                else:
                    for r1 in rows1:
                        treeView.delete(*treeView.get_children())
                        treeView.insert("", "end", values=r1)

                    myDb.commit()
                    reset()

        top.config(bg='#E8E8E8')
        top.title('Student Management')
        top.geometry('1510x650+10+125')
        top.resizable(False, False)
        top.grab_set()
        top.focus()

        studentFrame = Frame(top, bd=3, relief=GROOVE, bg='#E8E8E8')
        studentFrame.place(x=100, y=10, width=500, height=620)

        searchFrame = Frame(top, bd=3, relief=GROOVE, bg='#E8E8E8')
        searchFrame.place(x=620, y=10, width=765, height=620)

        rollNumberLabel = Label(studentFrame, text='Roll No.', font=('times new roman', 18, ''), bg='#E8E8E8')
        rollNumberLabel.grid(row=0, column=0, padx=50, pady=30)

        varRollNumber = StringVar()
        textRollNUmber = Entry(studentFrame, textvariable=varRollNumber, font=('times new roman', 18), width=22, bd=3,
                               relief=GROOVE)
        textRollNUmber.grid(row=0, column=1, padx=10, pady=5)

        nameLabel = Label(studentFrame, text='Name', font=('times new roman', 18, ''), bg='#E8E8E8')
        nameLabel.grid(row=1, column=0, padx=50, pady=15)

        varName = StringVar()
        textName = Entry(studentFrame, textvariable=varName, font=('times new roman', 18), width=22, bd=3,
                         relief=GROOVE)
        textName.grid(row=1, column=1, padx=10, pady=15)

        classLabel = Label(studentFrame, text='Class', font=('times new roman', 18, ''), bg='#E8E8E8')
        classLabel.grid(row=2, column=0, padx=50, pady=15)

        varClass = StringVar()
        textClass = Entry(studentFrame, textvariable=varClass, font=('times new roman', 18), width=22, bd=3,
                          relief=GROOVE)
        textClass.grid(row=2, column=1, padx=10, pady=15)

        genderLabel = Label(studentFrame, text='Gender', font=('times new roman', 18, ''), bg='#E8E8E8')
        genderLabel.grid(row=3, column=0, padx=50, pady=15)

        varGender = StringVar()
        textGender = ttk.Combobox(studentFrame, textvariable=varGender, font=('times new roman', 18),
                                  width=20, justify=CENTER, state='readonly')
        textGender['values'] = ('Select', 'Male', 'Female', 'Other')
        textGender.current(0)
        textGender.grid(row=3, column=1, padx=10, pady=15)

        mobileNoLabel = Label(studentFrame, text='Mobile No.', font=('times new roman', 18, ''), bg='#E8E8E8')
        mobileNoLabel.grid(row=4, column=0, padx=40, pady=15)

        varMobileNo = StringVar()
        textMobileNo = Entry(studentFrame, textvariable=varMobileNo, font=('times new roman', 18), width=22, bd=3,
                             relief=GROOVE)
        textMobileNo.grid(row=4, column=1, padx=10, pady=15)

        dobLabel = Label(studentFrame, text='DOB', font=('times new roman', 18, ''), bg='#E8E8E8')
        dobLabel.grid(row=5, column=0, padx=50, pady=15)

        varDob = StringVar()
        textDob = Entry(studentFrame, textvariable=varDob, font=('times new roman', 18), width=22, bd=3,
                        relief=GROOVE)
        textDob.grid(row=5, column=1, padx=10, pady=15)

        addressLabel = Label(studentFrame, text='Address', font=('times new roman', 18, ''), bg='#E8E8E8')
        addressLabel.grid(row=6, column=0, padx=50, pady=15)

        textAddress = Text(studentFrame, font=('times new roman', 18, ''), bd=3, relief=GROOVE)
        textAddress.place(x=205, y=430, width=270, height=80)

        addButton = Button(studentFrame, text='Add', font=('times new roman', 18, ''), padx=60, pady=5, bg='blue',
                           fg='white', activebackground='blue', activeforeground='white', cursor='hand2',
                           command=addData)
        addButton.place(x=80, y=540)

        deleteButton = Button(studentFrame, text='Delete', font=('times new roman', 18, ''), padx=50, pady=5,
                              bg='blue', fg='white', activebackground='blue', activeforeground='white', cursor='hand2',
                              command=deleteData)
        deleteButton.place(x=280, y=540)

        # ---------------------------------------- search label, entry and button --------------------------------------

        searchLabel = Label(searchFrame, text='Search by', font=('times new roman', 18, ''), bg='#E8E8E8')
        searchLabel.place(x=30, y=20)

        varSearch = StringVar()
        textSearch = ttk.Combobox(searchFrame, textvariable=varSearch, font=('times new roman', 16),
                                  width=15, justify=CENTER, state='readonly')
        textSearch['values'] = ('Select', 'Roll no.', 'Name')
        textSearch.current(0)
        textSearch.place(x=150, y=20)

        varValue = StringVar()
        textValue = Entry(searchFrame, textvariable=varValue, font=('times new roman', 16), width=18, bd=3,
                          relief=GROOVE)
        textValue.place(x=360, y=20)

        searchImage = PhotoImage(file='Images\\search1.png')
        searchButton = Button(searchFrame, font=('times new roman', 15, 'bold'), padx=20, pady=0, cursor='hand2', bd=0,
                              bg='#E8E8E8', image=searchImage, activebackground='#E8E8E8', command=searchStudent)
        searchButton.place(x=580, y=10)

        showAllButton = Button(searchFrame, text='Show All', font=('times new roman', 15, 'bold'), bg='blue',
                               fg='white',
                               padx=12, pady=0,
                               activebackground='blue', activeforeground='white', cursor='hand2', command=showAll)
        showAllButton.place(x=640, y=15)

        # ---------------------- sub frames for search window ----------------------------------------------------------
        tableFrame = LabelFrame(searchFrame, bd=3, relief=GROOVE)
        tableFrame.place(x=0, y=70, width=760, height=545)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading', font=('times new roman', 15, 'bold'))
        style.configure('Treeview', font=('Calibri', 14, ''), rowheight=25)

        xScrollbar = Scrollbar(tableFrame, orient=HORIZONTAL)
        xScrollbar.pack(side=BOTTOM, fill=X)

        yScrollbar = Scrollbar(tableFrame, orient=VERTICAL)
        yScrollbar.pack(side=RIGHT, fill=Y)

        treeView = ttk.Treeview(tableFrame, xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)
        treeView.pack(expand=YES, fill=BOTH)

        xScrollbar.config(command=treeView.xview)
        yScrollbar.config(command=treeView.yview)

        treeView['column'] = (1, 2, 3, 4, 5, 6, 7)

        treeView.heading(1, text='Roll No.')
        treeView.heading(2, text='Name.')
        treeView.heading(3, text='Class')
        treeView.heading(4, text='Gender')
        treeView.heading(5, text='Mobile No.')
        treeView.heading(6, text='DOB.')
        treeView.heading(7, text='Address')
        treeView['show'] = 'headings'
        top.mainloop()
# =============================  To manage the teacher window ==========================================================


    def teacher(self):
        top1 = Toplevel()

        # -----------------------Clear all Field -----------------------------------------------------------------------

        def clear():
            varTeacherId.set('')
            varName.set('')
            varMobileNo.set('')
            varGender.set('Select')
            varQualification.set('')
            varEmail.set('')
            textAddress.delete('1.0', END)

        # ----------------- clear recently search field ----------------------------------------------------------------

        def reset():
            varSearch.set("Select")
            varValue.set('')

        # ---------------------- Data insertion into teacher  table ----------------------------------------------------
        def addData():

            if varTeacherId.get() == '' or varName.get() == '' or varMobileNo.get() == '' or varGender.get() == 'Select'\
                    or varQualification.get() == '' or varEmail.get() == '' or textAddress.get("1.0", END) == '':
                messagebox.showerror('Error', 'All Fields are Required', parent=top1)
            else:
                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()
                sql = 'INSERT INTO teacher (teacher_id, teacher_name, teacher_mobileNo, teacher_gender, ' \
                      'teacher_qualification, teacher_email, teacher_address) VALUES (%s, %s, %s, %s, %s, %s, %s)'

                val = (varTeacherId.get(), varName.get(), varMobileNo.get(), varGender.get(), varQualification.get(),
                       varEmail.get(), textAddress.get("1.0", END))
                myCursor.execute(sql, val)
                myDb.commit()
                messagebox.showinfo('Success', "Data Inserted Successfully !", parent=top1)
                clear()
# --------------------------------  data  deletion from teacher table ------------------------------------------------

        def deleteData():
            if varTeacherId.get() == '':
                messagebox.showerror('Error', 'Please enter the Teacher ID to delete data', parent=top1)
            else:
                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()
                sql = "DELETE  FROM teacher WHERE teacher_id = '%s'"
                val = varTeacherId.get()
                myCursor.execute(sql % val)
                myDb.commit()
                messagebox.showinfo("Success", "Teacher's Data Deleted Successfully !", parent=top1)
                clear()

# --------------------------------  data show from Teacher table ------------------------------------------------

        def showAll():
            import mysql.connector
            myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                           database='School_Management_System')
            myCursor = myDb.cursor()
            treeView.delete(*treeView.get_children())
            myCursor.execute("SELECT * FROM teacher")
            rows = myCursor.fetchall()
            for r in rows:
                treeView.insert('', 'end', values=r)
            myDb.commit()

# --------------------------------  data  search from teacher table --------------------------------------------

        def searchTeacher():

            if varSearch.get() == 'Select' and varValue.get() == '':
                messagebox.showerror("Error", "Please Enter valid Data to Search !", parent=top1)
            else:

                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()

                myCursor.execute("SELECT * FROM teacher WHERE teacher_id = '%s' or teacher_name ='%s'" %
                                 (varValue.get(), varValue.get()))
                rows1 = myCursor.fetchall()
                if not rows1:
                    messagebox.showerror("Not Found", "No such record or Student  Found", parent=top1)
                    reset()

                else:
                    for r1 in rows1:
                        treeView.delete(*treeView.get_children())
                        treeView.insert("", "end", values=r1)

                    myDb.commit()
                    reset()

        top1.title('Teacher Management')
        top1.geometry('1510x650+10+125')
        top1.resizable(False, False)
        top1.grab_set()
        top1.focus()
        teacherFrame = Frame(top1, bd=3, relief=GROOVE, bg='#E8E8E8')
        teacherFrame.place(x=100, y=10, width=500, height=620)

        searchFrame = Frame(top1, bd=3, relief=GROOVE, bg='#E8E8E8')
        searchFrame.place(x=620, y=10, width=765, height=620)

        teacherIdLabel = Label(teacherFrame, text='Teacher Id', font=('times new roman', 15, ''), bg='#E8E8E8')
        teacherIdLabel.grid(row=0, column=0, padx=50, pady=30)

        varTeacherId = StringVar()
        textTeacherId = Entry(teacherFrame, textvariable=varTeacherId, font=('times new roman', 18), width=22, bd=3,
                              relief=GROOVE)
        textTeacherId.grid(row=0, column=1, padx=10, pady=5)

        nameLabel = Label(teacherFrame, text='Name', font=('times new roman', 18, ''), bg='#E8E8E8')
        nameLabel.grid(row=1, column=0, padx=40, pady=15)

        varName = StringVar()
        textName = Entry(teacherFrame, textvariable=varName, font=('times new roman', 18), width=22, bd=3,
                         relief=GROOVE)
        textName.grid(row=1, column=1, padx=10, pady=15)

        MobileNoLabel = Label(teacherFrame, text='Mobile', font=('times new roman', 18, ''), bg='#E8E8E8')
        MobileNoLabel.grid(row=2, column=0, padx=50, pady=15)

        varMobileNo = StringVar()
        textClass = Entry(teacherFrame, textvariable=varMobileNo, font=('times new roman', 18), width=22, bd=3,
                          relief=GROOVE)
        textClass.grid(row=2, column=1, padx=10, pady=15)

        genderLabel = Label(teacherFrame, text='Gender', font=('times new roman', 18, ''), bg='#E8E8E8')
        genderLabel.grid(row=3, column=0, padx=50, pady=15)

        varGender = StringVar()
        textGender = ttk.Combobox(teacherFrame, textvariable=varGender, font=('times new roman', 18),
                                  width=20, justify=CENTER, state='readonly')
        textGender['values'] = ('Select', 'Male', 'Female', 'Other')
        textGender.current(0)
        textGender.grid(row=3, column=1, padx=10, pady=15)

        qualificationLabel = Label(teacherFrame, text='Qualification', font=('times new roman', 18, ''), bg='#E8E8E8')
        qualificationLabel.grid(row=4, column=0, padx=30, pady=15)

        varQualification = StringVar()
        textQualification = Entry(teacherFrame, textvariable=varQualification, font=('times new roman', 18), width=22,
                                  bd=3,
                                  relief=GROOVE)
        textQualification.grid(row=4, column=1, padx=10, pady=15)

        emailLabel = Label(teacherFrame, text='Email', font=('times new roman', 18, ''), bg='#E8E8E8')
        emailLabel.grid(row=5, column=0, padx=50, pady=15)

        varEmail = StringVar()
        textEmail = Entry(teacherFrame, textvariable=varEmail, font=('times new roman', 18), width=22, bd=3,
                          relief=GROOVE)
        textEmail.grid(row=5, column=1, padx=10, pady=15)

        addressLabel = Label(teacherFrame, text='Address', font=('times new roman', 18, ''), bg='#E8E8E8')
        addressLabel.grid(row=6, column=0, padx=50, pady=15)

        textAddress = Text(teacherFrame, font=('times new roman', 18, ''), bd=3, relief=GROOVE)
        textAddress.place(x=205, y=430, width=270, height=80)

        addButton = Button(teacherFrame, text='Add', font=('times new roman', 18, ''), padx=60, pady=5, bg='blue',
                           fg='white', activebackground='blue', activeforeground='white', cursor='hand2',
                           command=addData)
        addButton.place(x=80, y=540)

        deleteButton = Button(teacherFrame, text='Delete', font=('times new roman', 18, ''), padx=50, pady=5,
                              bg='blue', fg='white', activebackground='blue', activeforeground='white', cursor='hand2',
                              command=deleteData)
        deleteButton.place(x=280, y=540)
# ---------------------------------------- search label, entry and button ----------------------------------------------

        searchLabel = Label(searchFrame, text='Search by', font=('times new roman', 18, ''), bg='#E8E8E8')
        searchLabel.place(x=30, y=20)

        varSearch = StringVar()
        textSearch = ttk.Combobox(searchFrame, textvariable=varSearch, font=('times new roman', 16),
                                  width=15, justify=CENTER, state='readonly')
        textSearch['values'] = ('Select', 'Teacher ID', 'Name')
        textSearch.current(0)
        textSearch.place(x=150, y=20)

        varValue = StringVar()
        textValue = Entry(searchFrame, textvariable=varValue, font=('times new roman', 16), width=18, bd=3,
                          relief=GROOVE)
        textValue.place(x=360, y=20)

        searchImage = PhotoImage(file='Images\\search1.png')
        searchButton = Button(searchFrame, font=('times new roman', 15, 'bold'), padx=20, pady=0, cursor='hand2', bd=0,
                              bg='#E8E8E8', image=searchImage, activebackground='#E8E8E8', command=searchTeacher)
        searchButton.place(x=580, y=10)

        showAllButton = Button(searchFrame, text='Show All', font=('times new roman', 15, 'bold'), bg='blue',
                               fg='white',
                               padx=12, pady=0,
                               activebackground='blue', activeforeground='white', cursor='hand2', command=showAll)
        showAllButton.place(x=640, y=15)

        # ---------------------- sub frames for search window ---------------------------------------------------------
        tableFrame = LabelFrame(searchFrame, bd=3, relief=GROOVE)
        tableFrame.place(x=0, y=70, width=760, height=545)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading', font=('times new roman', 15, 'bold'))
        style.configure('Treeview', font=('Calibri', 15, ''), rowheight=25)

        xScrollbar = Scrollbar(tableFrame, orient=HORIZONTAL)
        xScrollbar.pack(side=BOTTOM, fill=X)

        yScrollbar = Scrollbar(tableFrame, orient=VERTICAL)
        yScrollbar.pack(side=RIGHT, fill=Y)

        treeView = ttk.Treeview(tableFrame, xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)
        treeView.pack(expand=YES, fill=BOTH)

        xScrollbar.config(command=treeView.xview)
        yScrollbar.config(command=treeView.yview)

        treeView['column'] = (1, 2, 3, 4, 5, 6, 7)
        treeView.heading(1, text='Teacher Id.')
        treeView.heading(2, text='Name.')
        treeView.heading(3, text='Mobile No.')
        treeView.heading(4, text='Gender')
        treeView.heading(5, text='Qualification')
        treeView.heading(6, text='Email')
        treeView.heading(7, text='Address')
        treeView['show'] = 'headings'
        top1.mainloop()

# ========= Subject management ========================================================================================

    def subject(self):
        top3 = Toplevel()

# ---------------------- Clear All Fields -----------------------------------------------------------------------------
        def clear():
            varSubjectId.set('')
            varSubjectName.set('')
            varClassId.set('')

# ----------------- clear recently search field ---------------------------------------------------------------------

        def reset():
            varSearch.set("Select")
            varValue.set('')

# ---------------------- Data insertion into subject  table ------------------------------------------------------------
        def addData():
            try:

                if varSubjectId.get() == '' or varSubjectName.get() == '' or varClassId.get() == '':
                    messagebox.showerror('Error', 'All Fields are Required', parent=top3)
                else:
                    import mysql.connector
                    myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                                   database='School_Management_System')
                    myCursor = myDb.cursor()
                    sql = 'INSERT INTO subjects (subject_id, subject_name, class_id) VALUES (%s, %s, %s)'

                    val = (varSubjectId.get(), varSubjectName.get(), varClassId.get())
                    myCursor.execute(sql, val)
                    myDb.commit()
                    messagebox.showinfo('Success', "Data Inserted Successfully !", parent=top3)
                    clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due wrong Class Id {es}", parent=top3)
                clear()

                clear()

# --------------------------------  data  deletion from  Subjects table ------------------------------------------------

        def deleteData():
            if varSubjectId.get() == '':
                messagebox.showerror('Error', 'Please enter the Subject ID to delete data', parent=top3)
            else:
                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()
                sql = "DELETE  FROM subjects WHERE subject_id = '%s'"
                val = varSubjectId.get()
                myCursor.execute(sql % val)
                myDb.commit()
                messagebox.showinfo("Success", "Subjects's Data Deleted Successfully !", parent=top3)
                clear()

# --------------------------------  data show from subjects table ------------------------------------------------

        def showAll():
            import mysql.connector
            myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                           database='School_Management_System')
            myCursor = myDb.cursor()
            treeView.delete(*treeView.get_children())
            myCursor.execute("SELECT * FROM subjects")
            rows = myCursor.fetchall()
            for r in rows:
                treeView.insert('', 'end', values=r)
            myDb.commit()

# --------------------------------  data  search from subjects table ------------------------------------------------

        def searchClasses():

            if varSearch.get() == 'Select' and varValue.get() == '':
                messagebox.showerror("Error", "Please Enter valid Data to Search !", parent=top3)
            else:

                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()

                myCursor.execute("SELECT * FROM class WHERE class_id = '%s' or class_name ='%s'" %
                                 (varValue.get(), varValue.get()))
                rows1 = myCursor.fetchall()
                if not rows1:
                    messagebox.showerror("Not Found", "No such record or Student  Found", parent=top3)
                    reset()

                else:
                    for r1 in rows1:
                        treeView.delete(*treeView.get_children())
                        treeView.insert("", "end", values=r1)

                    myDb.commit()
                    reset()

        top3.title('Subject Management')
        top3.geometry('1510x650+10+125')
        top3.resizable(False, False)
        top3.grab_set()
        top3.focus()

        subjectFrame = Frame(top3, bd=3, relief=GROOVE, bg='#E8E8E8')
        subjectFrame.place(x=100, y=10, width=500, height=620)

        searchFrame = Frame(top3, bd=3, relief=GROOVE, bg='#E8E8E8')
        searchFrame.place(x=620, y=10, width=765, height=620)

        subjectIdLabel = Label(subjectFrame, text='Subject  Id', font=('times new roman', 15, ''), bg='#E8E8E8')
        subjectIdLabel.grid(row=0, column=0, padx=10, pady=30)

        varSubjectId = StringVar()
        textSubjectId = Entry(subjectFrame, textvariable=varSubjectId, font=('times new roman', 18), width=22, bd=3,
                              relief=GROOVE)
        textSubjectId.grid(row=1, column=0, padx=80, pady=0)

        subjectNameLabel = Label(subjectFrame, text='Subject  Name', font=('times new roman', 15, ''), bg='#E8E8E8')
        subjectNameLabel.grid(row=2, column=0, padx=10, pady=20)

        varSubjectName = StringVar()
        textSubjectName = Entry(subjectFrame, textvariable=varSubjectName, font=('times new roman', 18), width=22, bd=3,
                                relief=GROOVE)
        textSubjectName.grid(row=3, column=0, padx=80, pady=0)

        classIdLabel = Label(subjectFrame, text='Class  Id', font=('times new roman', 15, ''), bg='#E8E8E8')
        classIdLabel.grid(row=4, column=0, padx=10, pady=20)

        varClassId = StringVar()
        textClassId = Entry(subjectFrame, textvariable=varClassId, font=('times new roman', 18), width=22, bd=3,
                            relief=GROOVE)
        textClassId.grid(row=5, column=0, padx=80, pady=0)

        addButton = Button(subjectFrame, text='Add', font=('times new roman', 18, 'bold'), padx=40, bg='green',
                           fg='white', activebackground='green', foreground='white', activeforeground='white',
                           cursor='hand2', command=addData)
        addButton.place(x=50, y=380)

        deleteButton = Button(subjectFrame, text='Delete', font=('times new roman', 18, 'bold'), padx=40, bg='green',
                              fg='white', activebackground='green', activeforeground='white', foreground='white',
                              cursor='hand2', command=deleteData)
        deleteButton.place(x=220, y=380)

# ---------------------------------------- search label, entry and button ----------------------------------------------

        searchLabel = Label(searchFrame, text='Search by', font=('times new roman', 18, ''), bg='#E8E8E8')
        searchLabel.place(x=30, y=20)

        varSearch = StringVar()
        textSearch = ttk.Combobox(searchFrame, textvariable=varSearch, font=('times new roman', 16),
                                  width=15, justify=CENTER, state='readonly')
        textSearch['values'] = ('Select', 'Subject ID', 'Subject Name')
        textSearch.current(0)
        textSearch.place(x=150, y=20)

        varValue = StringVar()
        textValue = Entry(searchFrame, textvariable=varValue, font=('times new roman', 16), width=18, bd=3,
                          relief=GROOVE)
        textValue.place(x=360, y=20)

        searchImage = PhotoImage(file='Images\\search1.png')
        searchButton = Button(searchFrame, font=('times new roman', 15, 'bold'), padx=20, pady=0, cursor='hand2', bd=0,
                              bg='#E8E8E8', image=searchImage, activebackground='#E8E8E8', command=searchClasses)
        searchButton.place(x=580, y=10)

        showAllButton = Button(searchFrame, text='Show All', font=('times new roman', 15, 'bold'), bg='blue',
                               fg='white',
                               padx=12, pady=0,
                               activebackground='blue', activeforeground='white', cursor='hand2', command=showAll)
        showAllButton.place(x=640, y=15)

# ------------------------  Search sub frames window  ------------------------------------------------------------------

        tableFrame = LabelFrame(searchFrame, bd=3, relief=GROOVE)
        tableFrame.place(x=0, y=70, width=760, height=545)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading', font=('times new roman', 15, 'bold'))
        style.configure('Treeview', font=('Calibri', 15, ''), rowheight=25)

        xScrollbar = Scrollbar(tableFrame, orient=HORIZONTAL)
        xScrollbar.pack(side=BOTTOM, fill=X)

        yScrollbar = Scrollbar(tableFrame, orient=VERTICAL)
        yScrollbar.pack(side=RIGHT, fill=Y)

        treeView = ttk.Treeview(tableFrame, xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)
        treeView.pack(expand=YES, fill=BOTH)

        xScrollbar.config(command=treeView.xview)
        yScrollbar.config(command=treeView.yview)

        treeView['column'] = (1, 2, 3)
        treeView.heading(1, text='Subject Id.')
        treeView.heading(2, text=' Subject Name.')
        treeView.heading(3, text='Class Id.')
        treeView['show'] = 'headings'

        top3.mainloop()

# ==================================== Classes management front end Backend ===========================================
    
    def classes(self):
        top2 = Toplevel()

        # ---------------------- Clear All Fields ----------------------------------------------------------------------
        def clear():
            varClassId.set('')
            varClassName.set('')
            varDateOfjJoin.set('')

# ----------------- clear recently search field ---------------------------------------------------------------------

        def reset():
            varSearch.set("Select")
            varValue.set('')

# ---------------------- Data insertion into Classes table ------------------------------------------------------------
        def addData():

            if varClassId.get() == '' or varClassName.get() == '' or varDateOfjJoin.get() == '':
                messagebox.showerror('Error', 'All Fields are Required', parent=top2)
            else:
                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()
                sql = 'INSERT INTO class (class_id, class_name, date_of_join) VALUES (%s, %s, %s)'

                val = (varClassId.get(), varClassName.get(), varDateOfjJoin.get())
                myCursor.execute(sql, val)
                myDb.commit()
                messagebox.showinfo('Success', "Data Inserted Successfully !", parent=top2)
                clear()

# --------------------------------  data  deletion from  Classes table ------------------------------------------------

        def deleteData():
            if varClassId.get() == '':
                messagebox.showerror('Error', 'Please enter the Teacher ID to delete data', parent=top2)
            else:
                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()
                sql = "DELETE  FROM class WHERE class_id = '%s'"
                val = varClassId.get()
                myCursor.execute(sql % val)
                myDb.commit()
                messagebox.showinfo("Success", "Class Data Deleted Successfully !", parent=top2)
                clear()

# --------------------------------  data show from Teacher table ------------------------------------------------
        def showAll():
            import mysql.connector
            myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                           database='School_Management_System')
            myCursor = myDb.cursor()
            treeView.delete(*treeView.get_children())
            myCursor.execute("SELECT * FROM class")
            rows = myCursor.fetchall()
            for r in rows:
                treeView.insert('', 'end', values=r)
            myDb.commit()

# --------------------------------  data  search from teacher table ------------------------------------------------

        def searchClasses():

            if varSearch.get() == 'Select' and varValue.get() == '':
                messagebox.showerror("Error", "Please Enter valid Data to Search !", parent=top2)
            else:

                import mysql.connector
                myDb = mysql.connector.connect(host='localhost', user='root', passwd='sachin@0987',
                                               database='School_Management_System')
                myCursor = myDb.cursor()

                myCursor.execute("SELECT * FROM class WHERE class_id = '%s' or class_name ='%s'" %
                                 (varValue.get(), varValue.get()))
                rows1 = myCursor.fetchall()
                if not rows1:
                    messagebox.showerror("Not Found", "No such record or Student  Found", parent=top2)
                    reset()

                else:
                    for r1 in rows1:
                        treeView.delete(*treeView.get_children())
                        treeView.insert("", "end", values=r1)

                    myDb.commit()
                    reset()

        top2.title('Classes Management')
        top2.geometry('1510x650+10+125')
        top2.resizable(False, False)
        top2.grab_set()
        top2.focus()

        classFrame = Frame(top2, bd=3, relief=GROOVE, bg='#E8E8E8')
        classFrame.place(x=100, y=10, width=500, height=620)

        searchFrame = Frame(top2, bd=3, relief=GROOVE, bg='#E8E8E8')
        searchFrame.place(x=620, y=10, width=765, height=620)

        classIdLabel = Label(classFrame, text='Class  Id', font=('times new roman', 15, ''), bg='#E8E8E8')
        classIdLabel.grid(row=0, column=0, padx=10, pady=30)

        varClassId = StringVar()
        textClassId = Entry(classFrame, textvariable=varClassId, font=('times new roman', 18), width=22, bd=3,
                            relief=GROOVE)
        textClassId.grid(row=1, column=0, padx=80, pady=0)

        classNameLabel = Label(classFrame, text='Class  Name', font=('times new roman', 15, ''), bg='#E8E8E8')
        classNameLabel.grid(row=2, column=0, padx=10, pady=20)

        varClassName = StringVar()
        textClassName = Entry(classFrame, textvariable=varClassName, font=('times new roman', 18), width=22, bd=3,
                              relief=GROOVE)
        textClassName.grid(row=3, column=0, padx=80, pady=0)

        dateOfJoinLabel = Label(classFrame, text='Date of Start', font=('times new roman', 15, ''), bg='#E8E8E8')
        dateOfJoinLabel.grid(row=4, column=0, padx=10, pady=20)

        varDateOfjJoin = StringVar()
        textDateOfJoin = Entry(classFrame, textvariable=varDateOfjJoin, font=('times new roman', 18), width=22, bd=3,
                               relief=GROOVE)
        textDateOfJoin.grid(row=5, column=0, padx=80, pady=0)

        addButton = Button(classFrame, text='Add', font=('times new roman', 18, 'bold'), padx=40, bg='green',
                           fg='white', activebackground='green', foreground='white', activeforeground='white',
                           cursor='hand2', command=addData)
        addButton.place(x=50, y=380)

        deleteButton = Button(classFrame, text='Delete', font=('times new roman', 18, 'bold'), padx=40, bg='green',
                              fg='white', activebackground='green', activeforeground='white', foreground='white',
                              cursor='hand2', command=deleteData)
        deleteButton.place(x=220, y=380)

# ---------------------------------------- search label, entry and button ----------------------------------------------

        searchLabel = Label(searchFrame, text='Search by', font=('times new roman', 18, ''), bg='#E8E8E8')
        searchLabel.place(x=30, y=20)

        varSearch = StringVar()
        textSearch = ttk.Combobox(searchFrame, textvariable=varSearch, font=('times new roman', 16),
                                  width=15, justify=CENTER, state='readonly')
        textSearch['values'] = ('Select', ' Class ID', 'Class Name')
        textSearch.current(0)
        textSearch.place(x=150, y=20)

        varValue = StringVar()
        textValue = Entry(searchFrame, textvariable=varValue, font=('times new roman', 16), width=18, bd=3,
                          relief=GROOVE)
        textValue.place(x=360, y=20)

        searchImage = PhotoImage(file='Images\\search1.png')
        searchButton = Button(searchFrame, font=('times new roman', 15, 'bold'), padx=20, pady=0, cursor='hand2', bd=0,
                              bg='#E8E8E8', image=searchImage, activebackground='#E8E8E8', command=searchClasses)
        searchButton.place(x=580, y=10)

        showAllButton = Button(searchFrame, text='Show All', font=('times new roman', 15, 'bold'), bg='blue',
                               fg='white',
                               padx=12, pady=0,
                               activebackground='blue', activeforeground='white', cursor='hand2', command=showAll)
        showAllButton.place(x=640, y=15)

# ---------------------- sub frames for search window ---------------------------------------------------------

        tableFrame = LabelFrame(searchFrame, bd=3, relief=GROOVE)
        tableFrame.place(x=0, y=70, width=760, height=545)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading', font=('times new roman', 15, 'bold'))
        style.configure('Treeview', font=('Calibri', 15, ''), rowheight=25)

        xScrollbar = Scrollbar(tableFrame, orient=HORIZONTAL)
        xScrollbar.pack(side=BOTTOM, fill=X)

        yScrollbar = Scrollbar(tableFrame, orient=VERTICAL)
        yScrollbar.pack(side=RIGHT, fill=Y)

        treeView = ttk.Treeview(tableFrame, xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)
        treeView.pack(expand=YES, fill=BOTH)

        xScrollbar.config(command=treeView.xview)
        yScrollbar.config(command=treeView.yview)

        treeView['column'] = (1, 2, 3)
        treeView.heading(1, text='Class Id.')
        treeView.heading(2, text=' Class Name.')
        treeView.heading(3, text='Date of Start.')

        treeView['show'] = 'headings'
        top2.mainloop()
# ================================== Method for exit =====================================

    def exit(self):
        answer = messagebox.askyesno("Exit", "Do you really  want to exit ?")
        if answer is True:
            self.root.destroy()
            import login

    def clubs(self):
        messagebox.showinfo("Clubs", "Presently No clubs are active !", parent=self.root)

    def result(self):
        messagebox.showinfo("Result", "Database not updated yet !", parent=self.root)





win = Tk()
obj = App(win)
win.mainloop()
