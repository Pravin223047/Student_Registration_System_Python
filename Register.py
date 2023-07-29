from tkinter import *
from tkinter import messagebox
import mysql.connector

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

root=Tk()
root.title("New User Registration")
root.geometry("1250x700+310+150")
root.config(bg=background)
root.resizable(False,False)


image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="Images/Register.png")
Label(frame,image=backgroundimage).pack()

adminaccess = Entry(frame,width=15,fg="#000",border=0,bg="#e8ecf7",font=('Arial Bold',20),show="*")
adminaccess.focus()
adminaccess.place(x=550,y=280)

def user_enter(e):
    user.delete(0,'end')
def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'UserID')
    

user = Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',20))
user.insert(0,'UserID')
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x=500,y=380)

def password_enter(e):
    code.delete(0,'end')
def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
    

code = Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',20))
code.insert(0,'Password')
code.bind("<FocusIn>",password_enter)
code.bind("<FocusOut>",password_leave)
code.place(x=500,y=470)

button_mode=True

def hide():
    global button_mode
    if button_mode:
        
        eyeButton.config(image=closeeye,activebackground="white")
        code.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground="white")
        code.config(show="")
        button_mode=True

def register():
    username=user.get()
    password=code.get()
    admincode=adminaccess.get()
    if admincode=="2754":
        

        if(username=="" or username=="UserID") or (password=="" or password=="Password"):
            messagebox.showerror("Entry error","Type username or password!!!")
        else:
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',password='pmkc223047pmk')
                mycursor=mydb.cursor()
                print("Connected to Database!!")
            except:
                messagebox.showerror("Connection","Database connection not stablish!!!")
                return

            try:
                command="create database StudentRegistration"
                mycursor.execute(command)

                command="use StudentRegistration"
                mycursor.execute(command)

                command="create table login(user int auto_increment key not null, Username varchar(100), Password varchar(100))"
                mycursor.execute(command)
            except:
                mycursor.execute("use StudentRegistration")
                mydb=mysql.connector.connect(host='localhost',user='root',password='pmkc223047pmk',database="StudentRegistration")
                mycursor=mydb.cursor()

                command="insert into login(Username,Password) values(%s,%s)"
                mycursor.execute(command,(username,password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Register","New user added Sucessfully!!")
                

        
    else:
        messagebox.showinfo("Invalid","Please enter correct admin code!!!") 
def login():
    root.destroy()
    import Login
    
openeye=PhotoImage(file="Images/openeye.png")
closeeye=PhotoImage(file="Images/close eye.png")
eyeButton=Button(root,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=780,y=470)

regis_button=Button(root,text="ADD NEW USER",bg="#455c88",fg="white",width=13,height=1,font=("arial",16,'bold'),bd=0,command=register)
regis_button.place(x=530,y=600)

backbuttonimage=PhotoImage(file="Images/backbutton.png")
Backbutton=Button(root,image=backbuttonimage,fg="#deeefb",command=login)
Backbutton.place(x=20,y=15)


































































root.mainloop()
