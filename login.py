from tkinter import *
from PIL import ImageTk
from tkinter import messagebox, ttk
import mysql.connector


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login  System")
        self.root.geometry("1536x864+0+0")
        self.root.resizable(False, False)
        # ================================== background image ==========================================================

        self.bgImage = ImageTk.PhotoImage(file="Images/login_bg1.jpg")
        labelBackground = Label(self.root, image=self.bgImage)
        labelBackground.place(x=0, y=0, relwidth=1, relheight=1)

        # ================================== Login Main Frame ==========================================================

        self.frame1 = Frame(self.root, bg="#E8E8E8", bd=2, relief=GROOVE).place(x=410, y=60, width=560, height=550)

        labelHeading = Label(self.frame1, text="Admin Login System", bg="#E8E8E8", fg="#0070DF",
                             font=("Times new roman", 25, "bold"))
        labelHeading.place(x=520, y=95)

        self.userIcon = PhotoImage(file="Images/user.png")
        userPngLabel = Label(self.frame1, image=self.userIcon, bd=0, bg="#E8E8E8")
        userPngLabel.place(x=600, y=155)

        self.userName = PhotoImage(file="Images/username1.png")
        labelUsername = Label(self.frame1, text="Username", bg="#E8E8E8", font=("arial", 15, ""),
                              image=self.userName, compound=LEFT)
        labelUsername.place(x=510, y=265)

        self.varTextUsername = StringVar()
        txtUsername = Entry(self.frame1, textvariable=self.varTextUsername,
                            font=("arial", 15, ""), bd=2, relief=GROOVE)
        txtUsername.place(x=510, y=305, width=340, height=40)

        self.password = PhotoImage(file="Images/password1.png")
        labelPassword = Label(self.frame1, text="Password", bg="#E8E8E8", font=("arial", 15, ""),
                              image=self.password, compound=LEFT)
        labelPassword.place(x=510, y=365)

        self.varTextPassword = StringVar()
        txtPassword = Entry(self.frame1, textvariable=self.varTextPassword,
                            font=("arial", 15, ""), bd=2, relief=GROOVE, show="*")
        txtPassword.place(x=510, y=395, width=340, height=40)

        # ================================== Buttons ===================================================================

        self.buttonImage = PhotoImage(file="Images/button.png")

        forgetPassword = Button(self.frame1, text="Forget Password?", font=("times new roman", 14, "bold"),
                                bd=0, bg="#E8E8E8", fg="#df00df", cursor="hand2",
                                activebackground="#E8E8E8", activeforeground="green",
                                command=self.forgetPasswordFun)
        forgetPassword.place(x=680, y=455)

        loginButton = Button(self.frame1, image=self.buttonImage, bd=0, activebackground="#E8E8E8",
                             bg="#E8E8E8", cursor="hand2", command=self.funLogin)
        loginButton.place(x=570, y=505)
# ====================================== Forget password function =============================================
    def forgetPasswordFun(self):
        if self.varTextUsername.get() == "":
            messagebox.showerror("Error ", "Please enter Email address to reset password !", parent=self.root)
        else:
            myDb = mysql.connector.connect(host="localhost", user="root", passwd="sachin@0987",
                                           database="School_Management_System")
            myCursor = myDb.cursor()
            myCursor.execute("SELECT * FROM admin WHERE email = '%s'" % self.varTextUsername.get())
            result = myCursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "No Such Admin Exist , Please Enter Correct Email Address")
            else:
                self.root.destroy()
                import reset_password

    # ====================================== Login function =============================================

    def funLogin(self):
        if self.varTextUsername.get() == "" or self.varTextPassword.get() == "":
            messagebox.showerror("Error", "All Fields are Required ", parent=self.root)
        else:
            try:
                myDb = mysql.connector.connect(host="localhost", user="root", passwd="sachin@0987",
                                               database="School_Management_System")
                myCursor = myDb.cursor()
                sql = "SELECT * FROM admin WHERE email = '%s' and user_password = '%s'"
                val = (self.varTextUsername.get(), self.varTextPassword.get())
                myCursor.execute(sql % val)
                res = myCursor.fetchone()
                if res is None:
                    messagebox.showerror("Error", "Invalid Username and Password ", parent=self.root)
                else:
                    myDb.commit()
                    myDb.close()
                    messagebox.showinfo("Success", "Login Successful !")
                    self.root.destroy()
                    import App
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error Occurred due to {str(es)}", parent=self.root)

# ====================================== window switching =============================================




win = Tk()
loginObj1 = Login(win)
win.mainloop()
