from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os

class Registration_System:
    def __init__(self,root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fafafa')


        #============All Variables===============
        self.var_cid=StringVar()
        self.var_username=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()

        #============Registration Frame===============
        reg_frame=Frame(self.root,bd=5,relief=RIDGE,bg='white')
        reg_frame.place(x=450,y=90,width=350,height=400)

        #============Title===============
        title=Label(reg_frame,text='Registration Form',font=('Elephant',20,'bold'),bg='white').place(x=0,y=30,relwidth=1)

        #============Label and Text Entry===============
        lbl_username=Label(reg_frame,text='Username:',font=('times new roman',12),bg='white').place(x=20,y=100)
        lbl_email=Label(reg_frame,text='Email:',font=('times new roman',12),bg='white').place(x=20,y=150)
        lbl_password=Label(reg_frame,text='Password:',font=('times new roman',12),bg='white').place(x=20,y=200)

        txt_username=Entry(reg_frame,font=('times new roman',12),textvariable=self.var_username,bg='lightyellow').place(x=100,y=105)
        txt_email=Entry(reg_frame,font=('times new roman',12),textvariable=self.var_email,bg='lightyellow').place(x=100,y=150)
        txt_password=Entry(reg_frame,font=('times new roman',12),show=('*'),textvariable=self.var_password,bg='lightyellow').place(x=100,y=200)

        #============Button===============
        btn_register=Button(reg_frame,text='Register',font=('times new roman',15,'bold'),command=self.registration,bg="green",fg='white',cursor='hand2').place(x=100,y=250,width=100,height=30)


#=========================================================================================
    def registration(self):
        #===========Connect the Database==================
        con=sqlite3.connect(database=r'customerinfo.db')
        cur=con.cursor()
        #=================================================
        try:
            print(self.var_cid,self.var_username,self.var_email,self.var_password)
            if self.var_username.get()=="" or self.var_email.get()=='' or self.var_password.get()=='':
                messagebox.showerror('Error','Fields cannot be empty',parent=self.root)
            else:
                cur.execute("Select * from customer where username=?",(self.var_username.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','This Username already assigned, try different',parent=self.root)
                else:
                    cur.execute('Insert into customer (username,email,pass) values(?,?,?)',(   
                                                    self.var_username.get(),
                                                    self.var_email.get(),
                                                    self.var_password.get(),

                    ))
                    con.commit()
                    messagebox.showinfo('Success','User Resistration Successfully',parent=self.root)
                    self.login()


        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)

#=================Call another python file=================
    def login(self):
        self.root.destroy()
        os.system('Python login.py')



root=Tk()   
obj=Registration_System(root)
root.mainloop()