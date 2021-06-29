from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class ResetPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Reset password window")
        self.root.geometry("1536x864+0+0")
        self.root.resizable(False, False)
        self.root.config(bg="#E8E8E8")
        self.f1 = Frame(self.root, bd=4, relief=GROOVE, bg="#E8E8E8").place(x=500, y=100, width=560, height=550)

        titleLabel = Label(self.f1, text="Forget Password", font=("times new roman", 25, "bold"), fg="#D208A3",
                           bg="#E8E8E8")
        titleLabel.place(x=630, y=170)

        questionLabel = Label(self.f1, text="Security Question ",
                              font=("times new roman", 18, ""), bg="#E8E8E8")
        questionLabel.place(x=640, y=240)

        self.varComboBox = StringVar()
        comboBox = ttk.Combobox(self.root, textvariable=self.varComboBox,
                                font=("times new roman", 14, ""), justify=CENTER, state="readonly")
        comboBox["values"] = ("Select", "Who was your first class Teacher ?",
                              "What is your first pet name ?",
                              "What was your birth place ?")
        comboBox.current(0)
        comboBox.place(x=640, y=280, width=240, height=30)

        ansLabel = Label(self.root, text="Answer", font=("times new roman", 18, ""), bg="#E8E8E8")
        ansLabel.place(x=640, y=320)

        self.varAns = StringVar()
        textAns = Entry(self.root, textvariable=self.varAns,
                        font=("times new roman", 18, ""), bd=2, relief=GROOVE)
        textAns.place(x=640, y=360, width=240, height=30)

        passwordLabel = Label(self.root, text="New Password ", font=("times new roman", 18, ""), bg="#E8E8E8")
        passwordLabel.place(x=640, y=400)

        self.varNewPassword = StringVar()
        textPassword = Entry(self.root, show="*", textvariable=self.varNewPassword,
                             font=("times new roman", 16, ""), bd=2, relief=GROOVE)
        textPassword.place(x=640, y=440, width=240, height=30)

        confirmPassword = Label(self.root, text="Confirm Password", font=("times new roman", 16, ""), bg="#E8E8E8")
        confirmPassword.place(x=640, y=480)

        self.varConfirmPassword = StringVar()
        textConfirmPassword = Entry(self.root, textvariable=self.varConfirmPassword,
                                    font=("times new roman", 16, ""), bd=2, relief=GROOVE)
        textConfirmPassword.place(x=640, y=520, width=240, height=30)

        self.resetPassImage = PhotoImage(file="Images/resetpassBut.png")

        resetPassButton = Button(self.root, image=self.resetPassImage, bd=0, activebackground="#E8E8E8",
                                 bg="#E8E8E8", cursor="hand2", command=self.resetPass)
        resetPassButton.place(x=640, y=570)

    def clear(self):
        self.varComboBox.set("Select")
        self.varAns.set("")
        self.varNewPassword.set("")
        self.varConfirmPassword.set("")

    def resetPass(self):
        if self.varComboBox.get() == "" or self.varAns.get() == "":
            messagebox.showerror("Error", "Please Select Security question / Enter Answer")
        else:
            myDb = mysql.connector.connect(host="localhost", user="root",
                                           passwd="sachin@0987", database="School_Management_System")
            myCursor = myDb.cursor()
            myCursor.execute("SELECT * FROM admin WHERE security_question = '%s'and answer = '%s'" %
                             (self.varComboBox.get(), self.varAns.get()))
            result = myCursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "Please enter the correct answer", parent=self.root)
            else:
                myCursor.execute("UPDATE admin SET user_password = %s WHERE  answer = %s",
                                 (self.varNewPassword.get(), self.varAns.get()))
                myDb.commit()
                myDb.close()
                messagebox.showinfo("Success", "Password updated successfully !")
                self.clear()


win = Tk()
resetPassObj = ResetPassword(win)
win.mainloop()
