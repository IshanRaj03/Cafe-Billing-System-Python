from tkinter import *
import random
top=Tk()
top.config(bg="gray35")
top.geometry("1100x1900")


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
    a.geometry("800x600")
    a.config(bg="gray40")
    a.title("Billing")
    
    #frame=Frame(a,width =700,height=450).place(x=40,y=50)
    
    Drinks=D.get()
    Coffee=C.get()
    Sandwitch=S.get()
    Burger=B.get()
    
    
    totalquantity=int(Drinks+Coffee+Sandwitch+Burger)
    price=int((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))
    discount=0
    tax=10
    grandtotal=int(((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))+((Drinks * 50)+(Coffee * 70)+(Sandwitch * 60)+(Burger * 80))*0.1)
        
        
        
    TotalQuantity=Label(a,text=totalquantity,bg="gray80", font=("",25),padx=20).place(x=400,y=150)
    TotalPrice=Label(a,text=(price,"₹"),bg="gray80", font=("",25)).place(x=400,y=200)
    Discount=Label(a,text=(discount,"%"),bg="gray80", font=("",25)).place(x=400,y=250)
    Tax=Label(a,text=(tax,"%"),bg="gray80", font=("",25)).place(x=400,y=300)
    
    GrandTotal=Label(a,text=(grandtotal,"₹"),font=("",25),padx=80).place(x=400,y=400)
    
              

    Heading=Label(a,text=("Reciept"),font=("Times New Roman",30,'bold'),bg="gray85",padx=50).place(x=270,y=25)
    Qua=Label(a,text="Total Quantity",bg="gray80", font=("",25),).place(x=100, y=150)
    Cost=Label(a, text="Total Cost",bg="gray80", font=("",25),padx=27).place(x=100, y=200)
    Discount=Label(a,text="Discount",bg="gray80", font=("",25),padx=37).place(x=100, y=250)
    Tax=Label(a, text="Tax",bg="gray80", font=("",25),padx=74).place(x=100, y=300)
    Grand=Label(a, text="Grand Total",bg="gray80", font=("",25),padx=17).place(x=100, y=400)
    
    a.mainloop()
    
    
    
def reset():
    D.set("0")
    C.set("0")
    S.set("0")
    B.set("0")
    
    totalquantity=0
    price=0
    grandtotal=0
    
    
    

    


heading=Label(top,text="Choose your Daymaker",bg="grey85", font=("",30)).place(x=350,y=50)

# Choosing the quantity of Items
Orderno=Label(top,text="Order No:", font=("", 25),bg="gray80",padx=10).place(x=100, y=200)
Order=Label(top,text=x, font=("", 25),bg="gray80",padx=10).place(x=300, y=200)
Items=Label(top, text="Items",bg="gray80", font=("",25)).place(x=100,y=300)
Quantity=Label(top, text="Quantity",bg="gray80", font=("", 25)).place(x=400, y=300)
Drinks=Label(top, text="Drinks",bg="gray80", font=("",25),padx=31.5).place(x=100, y=400)
Coffee=Label(top, text="Coffee",bg="gray80", font=("",25),padx=30.5).place(x=100, y=450)
Sanwitch=Label(top, text="Sandwitch",bg="gray80", font=("",25),padx=4).place(x=100, y=500)
Burgers=Label(top, text="Burger",bg="gray80", font=("",25),padx=30).place(x=100, y=550)

#Choosing Quantity
Drinks=Entry(top, font=("",20),textvariable=D).place(x=350, y=400)
Coffee=Entry(top,font=("",20),textvariable=C).place(x=350, y=450)
Sandwitch=Entry(top,font=("",20),textvariable=S).place(x=350, y=500)
Burgers=Entry(top,font=("",20),textvariable=B).place(x=350, y=550)








# Price list
price=Label(top, text="Price List",bg="gray80", font=("times new roman",25,"bold"), height=1,padx=40).place(x=760, y=140)
drinks=Label(top, text="Drinks        50₹",bg="gray80", font=("",25),padx=10).place(x=750, y=200)
coffee=Label(top, text="Coffee        70₹",bg="gray80", font=("",25),padx=10).place(x=750, y=250)
sandwitch=Label(top, text="Sandwitch   60₹",bg="gray80", font=("",25),padx=5).place(x=750, y=300)
burgers=Label(top, text="Burgers      80₹",bg="gray80", font=("",25),padx=8.5).place(x=750, y=350)

Next=Button(top, text="Proceed",bg="gray80", font=("times new roman",25),command=proceed).place(x=700,y=550)
RESET=Button(top,text="Reset",bg="gray80", font=("times new roman",25),command=reset).place(x=900,y=550)





top.mainloop()
