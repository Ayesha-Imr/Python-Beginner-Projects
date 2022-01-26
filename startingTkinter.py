from tkinter import*
#doing above declaration exempts one from using extended methods like tkinter.Tk() etc


#Widgets: Labels, buttons, entry boxes, list boxes, checkboxes, images, frames etc 》used to design interface
#frame is used to divide the window into different sections containing related items
#Every widget has certain properties that help visualize them e.g: bg(background colour), fg(foreground colour), width(in pixels), height(in pixels), image, text(caption of widgets/ for usage in labels for entry boxes etc)
#Geometry Managers: 《decides placement of widgets》      •grid() •pack() •place() °grid(row=x, column=y)    °pack() ---> positions top, bottom, left, right


#define the window screen
m=Tk()
l1=Label(m, text="Name", bg="gold", fg="black", width=20, height=5).grid(row=0, column=0)
#properties can be set in no particular order
l2=Label(m, text="Address", bg="gold", fg="black", width=20, height=5).grid(row=1, column=0)
e1=Entry(m, bg="gold", fg="black", width=20)
e1.grid(row=0, column=1)
e2=Entry(m, bg="gold", fg="black", width=20)
e2.grid(row=1, column=1)
l3=Label(m, text="Dept", bg="gold", fg="black", width=20, height=5).grid(row=3, column=0)
l4=Label(m, text="Phone", bg="gold", fg="black", width=20, height=5).grid(row=4, column=0)
e3=Entry(m, bg="gold", fg="black", width=20)
e3.grid(row=3, column=1)
e4=Entry(m, bg="gold", fg="black", width=20)
e4.grid(row=4, column=1)
b1=Button(m, text="Submit", bg="green", fg="white", command="").grid(row=5, column=1)

lb=Listbox(m)
lb.insert(1,"BESE")
lb.insert(2, "BEEE")
lb.insert(3, "BEEL")
lb.insert(4, "BECE")
lb.insert(5, "BCIT")
lb.grid(row=5, column=0)





m.mainloop()
#above is the last line which basically calls the code. It is an infinite loop bc the interface window does not close until you manually do it.

