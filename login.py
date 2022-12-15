from tkinter import*
from PIL import ImageTk
from tkinter import messagebox

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
        self.var_username=StringVar()
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
        btn_forget=Button(login_frame,text='Forget Password?',font=('times new roman',15,'bold'),bd=0,bg="white",fg='blue',cursor='hand2',activebackground='white',activeforeground='blue').place(x=90,y=330)

        #============Sign Up===============

        signup_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        signup_frame.place(x=650,y=495,width=350,height=80)
        lbl_signup=Label(signup_frame,text="Don't have an account?",font=('times new roman',13,'bold'),bg='white').place(x=50,y=20)
        btn_signup=Button(signup_frame,text='Sign Up?',font=('times new roman',15,'bold'),bd=0,bg="white",fg='blue',cursor='hand2',activebackground='white',activeforeground='blue').place(x=220,y=15)

        #============Animation Image===============
        # image_frame=Frame(self.root,relief=RIDGE,bg='white')
        # image_frame.place(x=399,y=246,width=102,height=205)


        self.im1=ImageTk.PhotoImage(file='images/im1.png')
        self.im2=ImageTk.PhotoImage(file='images/im2.png')
        self.im3=ImageTk.PhotoImage(file='images/im3.png')

        self.lbl_change_image=Label(self.root,bg='white')
        self.lbl_change_image.place(x=399,y=246,width=102,height=205)

        self.animate()

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im

        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
         

    def login(self):
        if self.var_username.get()=='' or self.var_password.get()=='':
            messagebox.showerror('Error','User name and Passowrd, both filds are required.')
        elif self.var_username.get()!='nasim' or self.var_password.get()!='1234':
            messagebox.showerror('Error','User name or Password incorrect.')
        else:
            messagebox.showinfo('Information',f'Welcome {self.var_username.get()}')
 
root=Tk()   
obj=Login_System(root)
root.mainloop()
        