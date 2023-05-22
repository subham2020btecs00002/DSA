import mysql.connector
from tkinter import *

expression = ""

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2020BTECS00002",
    database="subham"
)

cur = con.cursor()
cur = con.cursor()

root = Tk()
root.geometry('500x450')
root.title("Employee Management System")

def add_employee():
    def add_query():
        global root
        stat = "INSERT INTO Employeesss(EmpNo, Name, Address, Grade, Salary, Date_of_joining) VALUES ('" + E1.get() + "','" + E2.get() + "','" + E3.get() + "','" + E4.get() + "','" + E5.get() + "','" + E6.get() + "')"
        cur.execute(stat)
        con.commit()
        add.config(state=NORMAL)
        update.config(state=NORMAL)
        show.config(state=NORMAL)
        delete.config(state=NORMAL)
        newwin.destroy()

    newwin = Toplevel(root)
    newwin.geometry('500x450')
    add.config(state=DISABLED)
    newwin.title("Add New Employee")

    L1 = Label(newwin, text="EmpNo")
    L1.place(x=10, y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=100, y=50)

    L2 = Label(newwin, text="Name")
    L2.place(x=10, y=100)
    E2 = Entry(newwin, bd=5)
    E2.place(x=100, y=100)

    L3 = Label(newwin, text="Address")
    L3.place(x=10, y=150)
    E3 = Entry(newwin, bd=5)
    E3.place(x=100, y=150)

    L4 = Label(newwin, text="Grade")
    L4.place(x=10, y=200)
    E4 = Entry(newwin, bd=5)
    E4.place(x=100, y=200)

    L5 = Label(newwin, text="Salary")
    L5.place(x=10, y=250)
    E5 = Entry(newwin, bd=5)
    E5.place(x=100, y=250)

    L6 = Label(newwin, text="Date of Joining")
    L6.place(x=10, y=300)
    E6 = Entry(newwin, bd=5)
    E6.place(x=120, y=300)

    sub = Button(newwin, text="Submit", command=add_query)
    sub.place(x=120, y=350)

def update_data():
    def UPDD():
        global root
        stat = "UPDATE Employeesss SET Name = '" + E2.get() + "' WHERE EmpNo = '" + E1.get() + "'"
        cur.execute(stat)
        con.commit()
        add.config(state=NORMAL)
        newwin.destroy()

    newwin = Toplevel(root)
    newwin.geometry('400x350')
    newwin.title("Update Employee Info")
    add.config(state=NORMAL)

    L1 = Label(newwin, text="EmpNo")
    L1.place(x=10, y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=100, y=50)

    L2 = Label(newwin, text="Name")
    L2.place(x=10, y=100)
    E2 = Entry(newwin, bd=5)
    E2.place(x=100, y=100)

    sub = Button(newwin, text="Update", command=UPDD)
    sub.place(x=120, y=200)

def del_data():
    def delete():
        global root
        stat = "DELETE FROM Employeesss WHERE EmpNo = '" + E1.get() + "'"
        cur.execute(stat)
        con.commit()
        add.config(state=NORMAL)
        newwin.destroy()

    newwin = Toplevel(root)
    newwin.geometry('400x350')
    newwin.title("Delete Employee")
    add.config(state=NORMAL)

    L1 = Label(newwin, text="EmpNo")
    L1.place(x=10, y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=100, y=50)

    sub = Button(newwin, text="Delete Entry", command=delete)
    sub.place(x=120, y=200)

def display():
    newwin = Toplevel(root)
    newwin.geometry('600x350')
    newwin.title("Employee Details")
    stat = "SELECT * FROM Employeesss"
    cur.execute(stat)

    L1 = Label(newwin, text="EmpNo")
    L1.grid(row=0, column=0)

    L2 = Label(newwin, text="Name")
    L2.grid(row=0, column=1)

    L3 = Label(newwin, text="Address")
    L3.grid(row=0, column=2)

    L4 = Label(newwin, text="Grade")
    L4.grid(row=0, column=3)

    L5 = Label(newwin, text="Salary")
    L5.grid(row=0, column=4)

    L6 = Label(newwin, text="Date of Joining")
    L6.grid(row=0, column=5)

    i = 1
    for row in cur:
        L1 = Label(newwin, text=row[0])
        L1.grid(row=i, column=0)

        L2 = Label(newwin, text=row[1])
        L2.grid(row=i, column=1)

        L3 = Label(newwin, text=row[2])
        L3.grid(row=i, column=2)

        L4 = Label(newwin, text=row[3])
        L4.grid(row=i, column=3)

        L5 = Label(newwin, text=row[4])
        L5.grid(row=i, column=4)

        L6 = Label(newwin, text=row[5])
        L6.grid(row=i, column=5)

        i += 1

add = Button(root, text='Add New Employee', command=add_employee)
delete = Button(root, text='Delete Employee Entry', command=del_data)
update = Button(root, text='Update Employee Info', command=update_data)
show = Button(root, text='Show Employee Details', command=display)
add.place(x=50, y=50)
delete.place(x=50, y=100)
update.place(x=200, y=50)
show.place(x=200, y=100)

root.mainloop()
