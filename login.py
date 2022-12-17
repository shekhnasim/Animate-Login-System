from tkinter import*
from PIL import ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title('Login System')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fafafa')

        #===============images============
        self.phone_image=ImageTk.PhotoImage(file='images/image1.png')
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0,bg='#fafafa').place(x=300,y=100,width=300,height=500)

        #============Login===============
        self.var_cid=StringVar()
        self.var_username=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        login_frame.place(x=650,y=90,width=350,height=400)

        title=Label(login_frame,text='Ligin System',font=('Elephant',30,'bold'),bg='white').place(x=0,y=30,relwidth=1)

        lbl_username=Label(login_frame,text='Username:',font=('times new roman',12),bg='white').place(x=50,y=100)
        txt_username=Entry(login_frame,font=('times new roman',12),textvariable=self.var_username,bg='lightyellow').place(x=50,y=130)

        lbl_password=Label(login_frame,text='Password:',font=('times new roman',12),bg='white').place(x=50,y=180)
        txt_password=Entry(login_frame,font=('times new roman',12),show=('*'),textvariable=self.var_password,bg='lightyellow').place(x=50,y=210)

        btn_login=Button(login_frame,text='Login',command=self.login,font=('times new roman',15,'bold'),bg="green",fg='white',cursor='hand2').place(x=90,y=250,width=100,height=30)

        hr=Label(login_frame,bg='lightgray').place(x=40,y=300,width=260,height=5)
        or_=Label(login_frame,bg='white',text=('OR')).place(x=160,y=290)
        btn_forget=Button(login_frame,text='Forget Password?',command=self.forget_password,font=('times new roman',15,'bold'),bd=0,bg="white",fg='blue',cursor='hand2',activebackground='white',activeforeground='blue').place(x=90,y=330)

        #============Sign Up===============

        signup_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        signup_frame.place(x=650,y=495,width=350,height=80)
        lbl_signup=Label(signup_frame,text="Don't have an account?",font=('times new roman',13,'bold'),bg='white').place(x=50,y=20)
        btn_signup=Button(signup_frame,text='Sign Up?',command=self.registration,font=('times new roman',15,'bold'),bd=0,bg="white",fg='blue',cursor='hand2',activebackground='white',activeforeground='blue').place(x=220,y=15)

        #============Animation Image===============
        # image_frame=Frame(self.root,relief=RIDGE,bg='white')
        # image_frame.place(x=399,y=246,width=102,height=205)


        self.im1=ImageTk.PhotoImage(file='images/im1.png')
        self.im2=ImageTk.PhotoImage(file='images/im2.png')
        self.im3=ImageTk.PhotoImage(file='images/im3.png')

        self.lbl_change_image=Label(self.root,bg='white')
        self.lbl_change_image.place(x=399,y=246,width=102,height=205)

        self.animate()

        #-----------Customer Details----------
        c_frame = Frame(self.root,bd=3,relief=RIDGE)
        c_frame.place(x=50,y=500,height=100)


        scrolly = Scrollbar(c_frame,orient=VERTICAL)
        scrollx = Scrollbar(c_frame,orient=HORIZONTAL)

        self.CustomerTable = ttk.Treeview(c_frame,columns=('cid','username','email','pass'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)
        
        self.CustomerTable.heading('cid',text='C ID') 
        self.CustomerTable.heading('username',text='Username')
        self.CustomerTable.heading('email',text='Email')
        self.CustomerTable.heading('pass',text='Password')

        self.CustomerTable['show']='headings' #To remove the blank left column

        self.CustomerTable.column('cid',width=60) 
        self.CustomerTable.column('username',width=100)
        self.CustomerTable.column('email',width=100)
        self.CustomerTable.column('pass',width=60)


        self.CustomerTable.pack(fill=BOTH,expand=1)
        #self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    


    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im

        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
         

    def login(self):
        con=sqlite3.connect(database=r'customerinfo.db')
        cur=con.cursor()
        try: 
            if self.var_username.get()=='' or self.var_password.get()=='':
                messagebox.showerror('Error','User name and Passowrd, both filds are required.')

            else:
                print('I am here')
                cur.execute("Select * from customer where username=?",(self.var_username.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror('Error','User does not exist')

                elif self.var_username.get()==row[1] and self.var_password.get()==row[3]:
                    messagebox.showinfo('Information',f'Welcome {self.var_username.get()}')

                else:
                    messagebox.showerror('Error','User name or Password is incorrect')
        
        except Exception as ex:
            
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'customerinfo.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from customer")
            rows=cur.fetchall()
            self.CustomerTable.delete(*self.CustomerTable.get_children())
            for row in rows:
                self.CustomerTable.insert('',END,values=row,)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)

    def get_data(self,ev):
        f=self.CustomerTable.focus()
        content=(self.CustomerTable.item(f))
        row=content['values']
        #print(row)
        self.var_cid.set(row[0])
        self.var_username.set(row[1])
        self.var_email.set(row[2])
        self.var_password.set(row[3])

    def forget_password(self):
        messagebox.showinfo('Success','OTP sent to your email address to reset your password')

#=================Call another python file=================
    def registration(self):
        self.root.destroy()
        os.system('Python registration.py')


root=Tk()   
obj=Login_System(root)
root.mainloop()
        