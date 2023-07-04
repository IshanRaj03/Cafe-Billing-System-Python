from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import csv
import random

    
windows=Tk()
windows.geometry("1400x800+0+0")
windows.title("Billing System")


def stud():
    studwindow=Toplevel()
    studwindow.geometry("900x600+250+45")
    studwindow.title("Login Form")
    lst=[]
    
    
    def login():
        if entry1.get()=="" and entry2.get()=="":
            messagebox.showerror("Error","Please Fill Name and Student ID ")
            
            
        else:
            login=False
            while login==False:
                data=[]
                with open("D:\\IP Project\\Student Data.csv","r")as f:
                    reader=csv.reader(f)
                    for row in reader:
                        data.append(row)
            
                    a=entry1.get()
                    b=entry2.get()
            
                    col0=[x[0] for x in data]
                    col1=[x[1] for x in data]
            
                    if a in col0:
                        for k in range (0,len(col0)):
                            if col0[k]==a and col1[k]==b:
                                    login=True
                                    studwindow.destroy()
                                    
                                    top=Toplevel()
                                    top.geometry("1400x800+0+0")
                                    
                                    bg=Image.open('D:\\IP Project\\billing bg.jpg')
                                    bg_place=ImageTk.PhotoImage(bg)
                                    bg_img=Label(top,image=bg_place)
                                    bg_img.place(x=0,y=0)
                                    
                                    frame=Frame(top,bg="light yellow",highlightbackground="orange",highlightthickness=5)
                                    frame.place(x=150,y=70,width=1100,height=600)
                                    
                                    x=random.randint(10908,500876)
                                    
                                    D=IntVar()
                                    C=IntVar()
                                    S=IntVar()
                                    B=IntVar()


                                    D.set("0")
                                    C.set("0")
                                    S.set("0")
                                    B.set("0")
                                    
                                    def proceed():
                                        a=Toplevel()
                                        a.geometry("1000x600+0+0")
                                        a.title("Billing")
                                        
                                        bg=Image.open('D:\\IP Project\\receipt bg.jpg')
                                        bg_place=ImageTk.PhotoImage(bg)
                                        bg_img=Label(a,image=bg_place)
                                        bg_img.place(x=0,y=0)
                                        
                                        
                                        
                                        
                                        frame=Frame(a,bg="light green",highlightbackground="black",highlightthickness=5)
                                        frame.place(x=100,y=70,width=800,height=450)
                                        
                                        bg=Image.open('D:\\IP Project\\thank you.png')
                                        bg_place=ImageTk.PhotoImage(bg)
                                        bg_img=Label(a,image=bg_place,bg="light green")
                                        bg_img.place(x=520,y=170)
                                        
                                        
                                        Drinks=D.get()
                                        Coffee=C.get()
                                        Sandwitch=S.get()
                                        Burger=B.get()
                                        
                                        
                                        totalquantity=int(Drinks+Coffee+Sandwitch+Burger)
                                        price=int((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))
                                        discount=25
                                        tax=10
                                        grandtotal=int(((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))-((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))*0.25
                                                       +((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))*0.1)
                                        
                                        
                                        TotalQuantity=Label(a,text=totalquantity,bg="light green", font=("",25)).place(x=400,y=160)
                                        TotalPrice=Label(a,text=(price,"₹"),bg="light green", font=("",25)).place(x=400,y=210)
                                        Discount=Label(a,text=(discount,"%"),bg="light green", font=("",25)).place(x=400,y=260)
                                        Tax=Label(a,text=(tax,"%"),bg="light green", font=("",25)).place(x=400,y=310)
                                        
                                        GrandTotal=Label(a,text=(grandtotal,"₹"),font=("",25),padx=80).place(x=430,y=410)
                                        
                                        
                                        Heading=Label(a,text=("Receipt"),font=("Trebuchet MS",40,"bold"),bg="green",padx=50).place(x=330,y=40)
                                        Qua=Label(a,text="Total Quantity",bg="light green", font=("tisa",25),).place(x=130,y=160)
                                        Cost=Label(a, text="Total Cost",bg="light green", font=("tisa",25)).place(x=130,y=210)
                                        Discount=Label(a,text="Discount",bg="light green", font=("tisa",25)).place(x=130,y=260)
                                        Tax=Label(a, text="Tax",bg="light green", font=("tisa",25)).place(x=130,y=310)
                                        Grand=Label(a, text="Grand Total :",bg="light green", font=("tisa",25,"bold"),padx=17).place(x=130,y=410)
                                        
                                        a.mainloop()
                                        
                                        
                                    def reset():
                                        D.set("0")
                                        C.set("0")
                                        S.set("0")
                                        B.set("0")
    
                                        totalquantity=0
                                        price=0
                                        grandtotal=0 
                                        
                                        
                                        
                                    heading=Label(top,text="Choose your Daymaker",bg="orange",font=("Trebuchet MS",50,"bold"))
                                    heading.place(x=310,y=35)
                                        
                                        
                                    
                                    # Choosing the quantity of Items
                                    Orderno=Label(top,text="Order No:", font=("tisa",25,"bold"),bg="light yellow",padx=10).place(x=190,y=200)
                                    Order=Label(top,text=x, font=("tisa", 25),bg="light yellow",padx=10).place(x=370,y=200)
                                    Items=Label(top, text="Items",bg="light yellow", font=("Lucida Handwriting",30)).place(x=200,y=300)
                                    Quantity=Label(top, text="Quantity",bg="light yellow", font=("Lucida Handwriting", 30)).place(x=470,y=300)
                                    Drinks=Label(top, text="Drinks",bg="light yellow", font=("tisa",25),padx=31.5).place(x=170,y=400)
                                    Coffee=Label(top, text="Coffee",bg="light yellow", font=("tisa",25),padx=30.5).place(x=170,y=450)
                                    Sanwitch=Label(top, text="Sandwitch",bg="light yellow", font=("tisa",25),padx=4).place(x=195,y=500)
                                    Burgers=Label(top, text="Burger",bg="light yellow", font=("tisa",25),padx=30).place(x=170,y=550)
        
                                    #Choosing Quantity
                                    Drinks=Entry(top, font=("tisa",20),bg="light yellow",textvariable=D).place(x=420, y=400)
                                    Coffee=Entry(top,font=("tisa",20),bg="light yellow",textvariable=C).place(x=420, y=450)
                                    Sandwitch=Entry(top,font=("tisa",20),bg="light yellow",textvariable=S).place(x=420, y=500)
                                    Burgers=Entry(top,font=("tisa",20),bg="light yellow",textvariable=B).place(x=420, y=550)
                                    
                                    
                                    # Price list
                                    price=Label(top,text="Price List",bg="light yellow",font=("Lucida Handwriting",25,"bold"),height=1,padx=40).place(x=830, y=160)
                                    drinks=Label(top,text="Drinks        50₹",bg="light yellow", font=("tisa",25),padx=10).place(x=820, y=220)
                                    coffee=Label(top,text="Coffee        70₹",bg="light yellow", font=("tisa",25),padx=10).place(x=820, y=270)
                                    sandwitch=Label(top,text="Sandwitch   60₹",bg="light yellow", font=("tisa",25),padx=5).place(x=820, y=320)
                                    burgers=Label(top,text="Burgers      80₹",bg="light yellow", font=("tisa",25),padx=8.5).place(x=820, y=370)
    
                                    Next=Button(top, text="Proceed",bg="orange", font=("Trebuchet MS",25,"bold italic"),command=proceed).place(x=770,y=570)
                                    RESET=Button(top,text="Reset",bg="orange", font=("Trebuchet MS",25,"bold italic"),command=reset).place(x=970,y=570)
                                    
                                        
                   
            
                                    top.mainloop()
                                    
                                   
                                    
                    else:
                        messagebox.showerror("Error","Please enter correct Name and Student ID \n If New Please Sign in..")
                        break
                        
                        
    
    def signin():
        studwindow.destroy()
        window=Toplevel()
        window.geometry("900x600+250+45")
        window.title("Sign In Form")
        
        bg=Image.open('D:\\IP Project\\signin bg.jpg')
        bg_place=ImageTk.PhotoImage(bg)
        bg_img=Label(window,image=bg_place)
        bg_img.place(x=0,y=0)
    
        frame=Frame(window,bg="orange",highlightbackground="black",highlightthickness=5).place(x=150,y=70,width=600,height=400)
        
        bg2=Image.open('D:\\IP Project\\hello.jpg')
        bg_place2=ImageTk.PhotoImage(bg2)
        bg_img2=Label(window,image=bg_place2,bg="black")
        bg_img2.place(x=580,y=170)
        
        
        
        
        def emptyerror():
            
            if entry1.get()=="" and entry2.get()=='':
                messagebox.showerror("Error","Please Fill Student ID ")
            else:
                a=False
                
                
            while a==False:
                
                data=[]
                with open("D:\\IP Project\\Student Data.csv","r")as f:
                    reader=csv.reader(f)
                    for row in reader:
                        data.append(row)
                        
                        
                    a=entry1.get()
                    b=entry2.get()
            
                    col0=[x[0] for x in data]
                    col1=[x[1] for x in data]
            
                    if a in col0:
                        for k in range (0,len(col0)):
                            if col0[k]==a and col1[k]==b:
                                    login=True
                                    messagebox.showerror("Error","Account Already Exist \nPlease Login")
                                    window.destroy()
                                    break
                
                    else:
                        with open("D:\\IP Project\\Student Data.csv","a",newline='') as f:
                            Writer=csv.writer(f)
                            lst=[entry1.get(),entry2.get()]
                            Writer.writerow(lst)
                            messagebox.showinfo("SAVED","The Data Is Succesfully Saved")
                            window.destroy()
                            break

                
        
        
        
        
        
        
        heading=Label(window,text="Sign In Here",fg="white",bg='black',bd=10,font=("Trebuchet MS",40,"bold"))     
        heading.place(x=285,y=30)
        
        Login=Label(window,text="Username",fg="Black",bg="orange",bd=10,font=("tisa",25,"italic"))
        Login.place(x=210,y=170)
    
        entry1=Entry(window,width=25,bg="orange",bd=0.5,font=("tisa",15,"italic"))
        entry1.place(x=220,y=222,height=30)
        
        Login=Label(window,text="Student ID",fg="Black",bg="orange",bd=10,font=("tisa",25,"italic"))
        Login.place(x=210,y=260)
    
        entry2=Entry(window,width=25,bg="orange",bd=0.5,font=("tisa",15,"italic"))
        entry2.place(x=220,y=320,height=30)
        
        
        signup_button=Button(window,text="SIGN UP",font=("Trebuchet MS",17,"bold"),fg="white",bg="black",bd=0,padx=80,pady=10,cursor="hand2",command=emptyerror)
        signup_button.place(x=320,y=430)
        
        window.mainloop()
        
    
    
        
    
    
    
    
    
    
    loginbg1=Image.open('D:\\IP Project\\login bg.jpg')
    loginbg_place1=ImageTk.PhotoImage(loginbg1)
    loginbg_img1=Label(studwindow,image=loginbg_place1).place(x=0,y=0)
    
    
    frame=Frame(studwindow,bg="pink",highlightbackground="orange",highlightthickness=5).place(x=150,y=70,width=600,height=400)
    
    loginbg2=Image.open('D:\\IP Project\\welcome.jpg')
    loginbg_place2=ImageTk.PhotoImage(loginbg2)
    loginbg_img2=Label(studwindow,image=loginbg_place2,bg="orange").place(x=580,y=160)
    
     
    
    
    heading=Label(studwindow,text="Login Here",fg="Black",bg='orange',bd=10,font=("Trebuchet MS",40,"bold"))     
    heading.place(x=305,y=50)

    Login=Label(studwindow,text="Username",fg="black",bg="pink",bd=10,font=("tisa",25,"italic"))
    Login.place(x=230,y=180)
    
    entry1=Entry(studwindow,width=25,bg="pink",bd=0.5,font=("tisa",15,"italic"))
    entry1.place(x=240,y=235,height=30)
    
    Login=Label(studwindow,text="Student ID",fg="Black",bg="pink",bd=10,font=("tisa",25,"italic"))
    Login.place(x=230,y=270)
    
    entry2=Entry(studwindow,width=25,bg="pink",bd=0.5,font=("tisa",15,"italic"))
    entry2.place(x=240,y=330,height=33)
    
    login_button=Button(studwindow,text="LOGIN",font=("Trebuchet MS",17,"bold"),bd=0,bg="orange",padx=55,pady=10,cursor="hand2",command=login).place(x=200,y=430)
    
    signup_button=Button(studwindow,text="New Student? SIGN UP",bg="orange",font=("Trebuchet MS",17,"bold"),bd=0,padx=20,pady=10,cursor="hand2",command=signin).place(x=440,y=430)
    
        
    studwindow.mainloop()
    
    
def prof():    
    profwindow=Toplevel()
    profwindow.geometry("900x600+250+45")
    profwindow.title("Login Form")
    
    
    def login():
        if entry1.get()=="" and entry2.get()=="":
         messagebox.showerror("Error","Please Fill Name and Professor ID ")
         
        else:
            login=False
            while login==False:
                data=[]
                with open("D:\\IP Project\\Professor Data.csv","r")as f:
                    reader=csv.reader(f)
                    for row in reader:
                        data.append(row)
            
                    a=entry1.get()
                    b=entry2.get()
            
                    col0=[x[0] for x in data]
                    col1=[x[1] for x in data]
            
                    if a in col0:
                        for k in range (0,len(col0)):
                            if col0[k]==a and col1[k]==b:
                                    login=True
                                    profwindow.destroy()
                                    
                                    
                                    top=Toplevel()
                                    top.geometry("1400x800+0+0")
    
    
                                    bg=Image.open('D:\\IP Project\\billing bg.jpg')
                                    bg_place=ImageTk.PhotoImage(bg)
                                    bg_img=Label(top,image=bg_place)
                                    bg_img.place(x=0,y=0)
    
    
                                    frame=Frame(top,bg="light yellow",highlightbackground="orange",highlightthickness=5)
                                    frame.place(x=150,y=70,width=1100,height=600)
                                    
                                    
                                    x=random.randint(10908,500876)


                                    D=IntVar()
                                    C=IntVar()
                                    S=IntVar()
                                    B=IntVar()
                                    
                                    
                                    D.set("0")
                                    C.set("0")
                                    S.set("0")
                                    B.set("0")
                                    
                                    def proceed():
                                         a=Toplevel()
                                         a.geometry("1000x600+0+0")
                                         a.title("Billing")
                                         
                                         bg=Image.open('D:\\IP Project\\receipt bg.jpg')
                                         bg_place=ImageTk.PhotoImage(bg)
                                         bg_img=Label(a,image=bg_place)
                                         bg_img.place(x=0,y=0)
                                         
                                         
                                         
                                         
                                         frame=Frame(a,bg="light green",highlightbackground="black",highlightthickness=5)
                                         frame.place(x=100,y=70,width=800,height=450)
                                         
                                         bg=Image.open('D:\\IP Project\\thank you.png')
                                         bg_place=ImageTk.PhotoImage(bg)
                                         bg_img=Label(a,image=bg_place,bg="light green")
                                         bg_img.place(x=520,y=170)
                                         
                                         
                                         Drinks=D.get()
                                         Coffee=C.get()
                                         Sandwitch=S.get()
                                         Burger=B.get()
                                         
                                         
                                         totalquantity=int(Drinks+Coffee+Sandwitch+Burger)
                                         price=int((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))
                                         discount=10
                                         tax=10
                                         
                                         grandtotal=int(((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))-((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))*0.01
                                                        +((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))*0.1)
                                         
                                         
                                         TotalQuantity=Label(a,text=totalquantity,bg="light green", font=("",25)).place(x=400,y=160)
                                         TotalPrice=Label(a,text=(price,"₹"),bg="light green", font=("",25)).place(x=400,y=210)
                                         Discount=Label(a,text=(discount,"%"),bg="light green", font=("",25)).place(x=400,y=260)
                                         Tax=Label(a,text=(tax,"%"),bg="light green", font=("",25)).place(x=400,y=310)
                                         
                                         GrandTotal=Label(a,text=(grandtotal,"₹"),font=("",25),padx=80).place(x=430,y=410)
                                         
                                         
                                         Heading=Label(a,text=("Receipt"),font=("Trebuchet MS",40,"bold"),bg="green",padx=50).place(x=330,y=40)
                                         Qua=Label(a,text="Total Quantity",bg="light green", font=("tisa",25),).place(x=130,y=160)
                                         Cost=Label(a, text="Total Cost",bg="light green", font=("tisa",25)).place(x=130,y=210)
                                         Discount=Label(a,text="Discount",bg="light green", font=("tisa",25)).place(x=130,y=260)
                                         Tax=Label(a, text="Tax",bg="light green", font=("tisa",25)).place(x=130,y=310)
                                         Grand=Label(a, text="Grand Total :",bg="light green", font=("tisa",25,"bold"),padx=17).place(x=130,y=410)
                                         
                                         a.mainloop()
                                        
                                    def reset():
                                        
                                        D.set("0")
                                        C.set("0")
                                        S.set("0")
                                        B.set("0")
    
                                        totalquantity=0
                                        price=0
                                        grandtotal=0  
                                        
                                        
                                        
                                        
                                        
                                        
                                    heading=Label(top,text="Choose your Daymaker",bg="orange",font=("Trebuchet MS",50,"bold"))
                                    heading.place(x=310,y=35)
                                        
                                        
                                    
                                    # Choosing the quantity of Items
                                    Orderno=Label(top,text="Order No:", font=("tisa",25,"bold"),bg="light yellow",padx=10).place(x=190,y=200)
                                    Order=Label(top,text=x, font=("tisa", 25),bg="light yellow",padx=10).place(x=370,y=200)
                                    Items=Label(top, text="Items",bg="light yellow", font=("Lucida Handwriting",30)).place(x=200,y=300)
                                    Quantity=Label(top, text="Quantity",bg="light yellow", font=("Lucida Handwriting", 30)).place(x=470,y=300)
                                    Drinks=Label(top, text="Drinks",bg="light yellow", font=("tisa",25),padx=31.5).place(x=170,y=400)
                                    Coffee=Label(top, text="Coffee",bg="light yellow", font=("tisa",25),padx=30.5).place(x=170,y=450)
                                    Sanwitch=Label(top, text="Sandwitch",bg="light yellow", font=("tisa",25),padx=4).place(x=195,y=500)
                                    Burgers=Label(top, text="Burger",bg="light yellow", font=("tisa",25),padx=30).place(x=170,y=550)
        
                                    #Choosing Quantity
                                    Drinks=Entry(top, font=("tisa",20),bg="light yellow",textvariable=D).place(x=420, y=400)
                                    Coffee=Entry(top,font=("tisa",20),bg="light yellow",textvariable=C).place(x=420, y=450)
                                    Sandwitch=Entry(top,font=("tisa",20),bg="light yellow",textvariable=S).place(x=420, y=500)
                                    Burgers=Entry(top,font=("tisa",20),bg="light yellow",textvariable=B).place(x=420, y=550)
                                    
                                    
                                    # Price list
                                    price=Label(top,text="Price List",bg="light yellow",font=("Lucida Handwriting",25,"bold"),height=1,padx=40).place(x=830, y=160)
                                    drinks=Label(top,text="Drinks        50₹",bg="light yellow", font=("tisa",25),padx=10).place(x=820, y=220)
                                    coffee=Label(top,text="Coffee        70₹",bg="light yellow", font=("tisa",25),padx=10).place(x=820, y=270)
                                    sandwitch=Label(top,text="Sandwitch   60₹",bg="light yellow", font=("tisa",25),padx=5).place(x=820, y=320)
                                    burgers=Label(top,text="Burgers      80₹",bg="light yellow", font=("tisa",25),padx=8.5).place(x=820, y=370)
    
                                    Next=Button(top, text="Proceed",bg="orange", font=("Trebuchet MS",25,"bold italic"),command=proceed).place(x=770,y=570)
                                    RESET=Button(top,text="Reset",bg="orange", font=("Trebuchet MS",25,"bold italic"),command=reset).place(x=970,y=570)
                                        
                                    top.mainloop()
                                    
                                         
                    else:
                        messagebox.showerror("Error","Please enter correct Name and Professor ID \n If Recently Joined Please Sign in..")
                        break 
             
    def signin():
        profwindow.destroy()
        window=Toplevel()
        window.geometry("900x600+250+45")
        window.title("Sign In Form")
        
        
        bg=Image.open('D:\\IP Project\\signin bg.jpg')
        bg_place=ImageTk.PhotoImage(bg)
        bg_img=Label(window,image=bg_place)
        bg_img.place(x=0,y=0)
    
        frame=Frame(window,bg="orange",highlightbackground="black",highlightthickness=5).place(x=150,y=70,width=600,height=400)
        
        bg2=Image.open('D:\\IP Project\\hello.jpg')
        bg_place2=ImageTk.PhotoImage(bg2)
        bg_img2=Label(window,image=bg_place2,bg="black")
        bg_img2.place(x=580,y=170)
        
        
        
        def emptyerror():
            
            if entry1.get()=="" and entry2.get()=="":
                
                messagebox.showerror("Error","Please Fill Professor ID ")    
            else:
                
                    
                with open("D:\\IP Project\\Professor Data.csv","a",newline='') as f:
                        
                    Writer=csv.writer(f)
                    lst=[entry1.get(),entry2.get()]
                    Writer.writerow(lst)
                    messagebox.showinfo("SAVED","The Data Is Succesfully Saved")
                    window.destroy()
                    
                    
        heading=Label(window,text="Sign In Here",fg="white",bg='black',bd=10,font=("Trebuchet MS",40,"bold"))     
        heading.place(x=285,y=30)
        
        Login=Label(window,text="Username",fg="Black",bg="orange",bd=10,font=("tisa",25,"italic"))
        Login.place(x=210,y=170)
    
        entry1=Entry(window,width=25,bg="orange",bd=0.5,font=("tisa",15,"italic"))
        entry1.place(x=220,y=222,height=30)
        
        Login=Label(window,text="Professor ID",fg="Black",bg="orange",bd=10,font=("tisa",25,"italic"))
        Login.place(x=210,y=260)
    
        entry2=Entry(window,width=25,bg="orange",bd=0.5,font=("tisa",15,"italic"))
        entry2.place(x=220,y=320,height=30)
        
        
        signup_button=Button(window,text="SIGN UP",font=("Trebuchet MS",17,"bold"),fg="white",bg="black",bd=0,padx=80,pady=10,cursor="hand2",command=emptyerror)
        signup_button.place(x=320,y=430)           
          
                    
       
        window.mainloop()
                
                
                
                
                
         
    
    
    
    
    loginbg1=Image.open('D:\\IP Project\\login bg.jpg')
    loginbg_place1=ImageTk.PhotoImage(loginbg1)
    loginbg_img1=Label(profwindow,image=loginbg_place1).place(x=0,y=0)
    
    
    frame=Frame(profwindow,bg="pink",highlightbackground="orange",highlightthickness=5).place(x=150,y=70,width=650,height=400)
    
    loginbg2=Image.open('D:\\IP Project\\welcome.jpg')
    loginbg_place2=ImageTk.PhotoImage(loginbg2)
    loginbg_img2=Label(profwindow,image=loginbg_place2,bg="orange").place(x=580,y=160)
    
    
    
    heading=Label(profwindow,text="Login Here",fg="Black",bg='orange',bd=10,font=("Trebuchet MS",40,"bold"))     
    heading.place(x=305,y=50)
    
    Login=Label(profwindow,text="Username",fg="black",bg="pink",bd=10,font=("tisa",25,"italic"))
    Login.place(x=230,y=180)
    
    entry1=Entry(profwindow,width=25,bg="pink",bd=0.5,font=("tisa",15,"italic"))
    entry1.place(x=240,y=235,height=30)
    
    Login=Label(profwindow,text="Professor ID",fg="Black",bg="pink",bd=10,font=("tisa",25,"italic"))
    Login.place(x=230,y=270)
    
    entry2=Entry(profwindow,width=25,bg="pink",bd=0.5,font=("tisa",15,"italic"))
    entry2.place(x=240,y=330,height=33)
    
    login_button=Button(profwindow,text="LOGIN",font=("Trebuchet MS",17,"bold"),bd=0,bg="orange",padx=55,pady=10,cursor="hand2",command=login).place(x=200,y=430)
    
    signup_button=Button(profwindow,text="Recently Joined? SIGN UP",bg="orange",font=("Trebuchet MS",17,"bold"),bd=0,padx=20,pady=10,cursor="hand2",command=signin).place(x=440,y=430)
    

    
    profwindow.mainloop()

def nonstud():
    top=Toplevel()
    top.geometry("1400x800+0+0")
    
    
    bg=Image.open('D:\\IP Project\\billing bg.jpg')
    bg_place=ImageTk.PhotoImage(bg)
    bg_img=Label(top,image=bg_place)
    bg_img.place(x=0,y=0)
    
    
    frame=Frame(top,bg="light yellow",highlightbackground="orange",highlightthickness=5)
    frame.place(x=150,y=70,width=1100,height=600)


    x=random.randint(10908,500876)


    D=IntVar()
    C=IntVar()
    S=IntVar()
    B=IntVar()


    D.set("0")
    C.set("0")
    S.set("0")
    B.set("0")
    
    
    
    def proceed():
        
        a=Toplevel()
        a.geometry("1000x600+0+0")
        a.title("Billing")
        
        bg=Image.open('D:\\IP Project\\receipt bg.jpg')
        bg_place=ImageTk.PhotoImage(bg)
        bg_img=Label(a,image=bg_place)
        bg_img.place(x=0,y=0)
        
        
        
        
        frame=Frame(a,bg="light green",highlightbackground="black",highlightthickness=5)
        frame.place(x=100,y=70,width=800,height=450)
        
        bg=Image.open('D:\\IP Project\\thank you.png')
        bg_place=ImageTk.PhotoImage(bg)
        bg_img=Label(a,image=bg_place,bg="light green")
        bg_img.place(x=520,y=170)
        
        
        Drinks=D.get()
        Coffee=C.get()
        Sandwitch=S.get()
        Burger=B.get()
        
        
        totalquantity=int(Drinks+Coffee+Sandwitch+Burger)
        price=int((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))
        discount=0
        tax=10
        grandtotal=int(((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))+((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))*0.1)
        
        
        TotalQuantity=Label(a,text=totalquantity,bg="light green", font=("",25)).place(x=400,y=160)
        TotalPrice=Label(a,text=(price,"₹"),bg="light green", font=("",25)).place(x=400,y=210)
        Discount=Label(a,text=(discount,"%"),bg="light green", font=("",25)).place(x=400,y=260)
        Tax=Label(a,text=(tax,"%"),bg="light green", font=("",25)).place(x=400,y=310)
        
        GrandTotal=Label(a,text=(grandtotal,"₹"),font=("",25),padx=80).place(x=430,y=410)
        
        
        Heading=Label(a,text=("Receipt"),font=("Trebuchet MS",40,"bold"),bg="green",padx=50).place(x=330,y=40)
        Qua=Label(a,text="Total Quantity",bg="light green", font=("tisa",25),).place(x=130,y=160)
        Cost=Label(a, text="Total Cost",bg="light green", font=("tisa",25)).place(x=130,y=210)
        Discount=Label(a,text="Discount",bg="light green", font=("tisa",25)).place(x=130,y=260)
        Tax=Label(a, text="Tax",bg="light green", font=("tisa",25)).place(x=130,y=310)
        Grand=Label(a, text="Grand Total :",bg="light green", font=("tisa",25,"bold"),padx=17).place(x=130,y=410)
        
        a.mainloop()
        
    def reset():
        D.set("0")
        C.set("0")
        S.set("0")
        B.set("0")
        
        
        
        
        
    totalquantity=0
    price=0
    grandtotal=0
    
    heading=Label(top,text="Choose your Daymaker",bg="orange",font=("Trebuchet MS",50,"bold"))
    heading.place(x=310,y=35)
    
       

    # Choosing the quantity of Items
    Orderno=Label(top,text="Order No:", font=("tisa",25,"bold"),bg="light yellow",padx=10).place(x=190,y=200)
    Order=Label(top,text=x, font=("tisa", 25),bg="light yellow",padx=10).place(x=370,y=200)
    Items=Label(top, text="Items",bg="light yellow", font=("Lucida Handwriting",30)).place(x=200,y=300)
    Quantity=Label(top, text="Quantity",bg="light yellow", font=("Lucida Handwriting", 30)).place(x=470,y=300)
    Drinks=Label(top, text="Drinks",bg="light yellow", font=("tisa",25),padx=31.5).place(x=170,y=400)
    Coffee=Label(top, text="Coffee",bg="light yellow", font=("tisa",25),padx=30.5).place(x=170,y=450)
    Sanwitch=Label(top, text="Sandwitch",bg="light yellow", font=("tisa",25),padx=4).place(x=195,y=500)
    Burgers=Label(top, text="Burger",bg="light yellow", font=("tisa",25),padx=30).place(x=170,y=550)
        
    #Choosing Quantity
    Drinks=Entry(top, font=("tisa",20),bg="light yellow",textvariable=D).place(x=420, y=400)
    Coffee=Entry(top,font=("tisa",20),bg="light yellow",textvariable=C).place(x=420, y=450)
    Sandwitch=Entry(top,font=("tisa",20),bg="light yellow",textvariable=S).place(x=420, y=500)
    Burgers=Entry(top,font=("tisa",20),bg="light yellow",textvariable=B).place(x=420, y=550)

    # Price list
    price=Label(top,text="Price List",bg="light yellow",font=("Lucida Handwriting",25,"bold"),height=1,padx=40).place(x=830, y=160)
    drinks=Label(top,text="Drinks        50₹",bg="light yellow", font=("tisa",25),padx=10).place(x=820, y=220)
    coffee=Label(top,text="Coffee        70₹",bg="light yellow", font=("tisa",25),padx=10).place(x=820, y=270)
    sandwitch=Label(top,text="Sandwitch   60₹",bg="light yellow", font=("tisa",25),padx=5).place(x=820, y=320)
    burgers=Label(top,text="Burgers      80₹",bg="light yellow", font=("tisa",25),padx=8.5).place(x=820, y=370)
    
    Next=Button(top, text="Proceed",bg="orange", font=("Trebuchet MS",25,"bold italic"),command=proceed).place(x=770,y=570)
    RESET=Button(top,text="Reset",bg="orange", font=("Trebuchet MS",25,"bold italic"),command=reset).place(x=970,y=570)  
        
    top.mainloop()
        
    
    


bg=Image.open('D:\\IP Project\\start bg.png')
bg_place=ImageTk.PhotoImage(bg)
bg_img=Label(windows,image=bg_place).place(x=0,y=0)



Student=Button(windows,text="Student",fg="white",bg='black',bd=1,padx=100,pady=18,cursor="hand2",font=("Trebuchet MS",25,"bold italic"),command=stud)
Student.place(x=90,y=550)
Professor=Button(windows,text="Professor",fg="white",bg='black',bd=1,padx=100,pady=20,cursor="hand2",font=("Trebuchet MS",25,"bold italic"),command=prof)
Professor.place(x=480,y=550)
Not_A_College_Student=Button(windows,text="Not A College Student",fg="white",bg='black',bd=1,padx=50,pady=20,font=("Trebuchet MS",25,"bold italic"),command=nonstud)
Not_A_College_Student.place(x=880,y=550)



HEADING=Label(windows,text="The Coffee Shop",fg="Black",bg='yellow',padx=80,font=("Trebuchet MS",60,"bold italic"))
HEADING.place(x=300,y=0)

HEADING2=Label(windows,text="We Serve The Best",fg="white",bg='black',font=("Trebuchet MS",30,"italic"))
HEADING2.place(x=747,y=105)



windows.mainloop()
