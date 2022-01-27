from tkinter import*
m=Tk()

def sum():
    x=int(e1.get())
    y=int(e2.get())
    z=x+y
    l3.config(text=z)
    
def subt():
    x=int(e1.get())
    y=int(e2.get())
    b=x-y
    l3.config(text=b)
    
def mult():
    x=int(e1.get())
    y=int(e2.get())
    w=x*y
    l3.config(text=w)
    
def div():
    x=int(e1.get())
    y=int(e2.get())
    j=x//y
    l3.config(text=j)
    
l3=Label(m, text="Result", font=("Times New Roman", 10), bg="green", fg="white", width=8)
l3.grid(row=6, column=1, pady=5)
l1=Label(m, text="No#1", font=("Times New Roman", 12), bg="red", fg="white", width=5)
l1.grid(row=0, column=0, pady=20)
l2=Label(m, text="No#2", font=("Times New Roman", 12), bg="red", fg="white", width=5)
l2.grid(row=1, column=0, pady=20)
e1=Entry(m, width=8)
e1.grid(row=0, column=1, padx=20)
e2=Entry(m, width=8)
e2.grid(row=1, column=1, padx=20)
b1=Button(m, bg="blue", font=("Times New Roman", 8), fg="white", text="Add", height=1, width=4, command=sum)
b1.grid(row=2, column=1, padx=4, pady=4)
b2=Button(m, bg="blue", font=("Times New Roman", 8), fg="white", text="Divide", height=1, width=4, command=div)
b2.grid(row=5, column=1, padx=4, pady=4)
b3=Button(m, bg="blue", font=("Times New Roman", 8), fg="white", text="Multiply", height=1, width=4, command=mult)
b3.grid(row=4, column=1, padx=4, pady=4)
b4=Button(m, bg="blue", font=("Times New Roman", 8), fg="white", text="Subtract", height=1, width=4, command=subt)
b4.grid(row=3, column=1, padx=4, pady=4)

m.mainloop()
    

