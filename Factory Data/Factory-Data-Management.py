from tkinter import *
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
from tkinter import messagebox
# from tabulate import tabulate
import mysql.connector as con
import csv

n = 1

# Combining two functions to run them together using a single button


def combine(*funcs):
    def inner_combine(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return inner_combine


def addundelivered():
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    root = Tk()
    root.title("Data Input")
    root.geometry("300x250")
    root.config(bg='#ddb892')

    Label(root, text="Order ID", bg='#ddb892').place(x=10, y=10)
    Label(root, text="Name", bg='#ddb892').place(x=10, y=40)
    Label(root, text="Quantity", bg='#ddb892').place(x=10, y=70)
    Label(root, text="Status", bg='#ddb892').place(x=10, y=100)
    Label(root, text="Client Name", bg='#ddb892').place(x=10, y=130)
    Label(root, text="Client Details", bg='#ddb892').place(x=10, y=160)

    e1 = Entry(root, bg='#ede0d4')
    e1.place(x=140, y=10)

    e2 = Entry(root, bg='#ede0d4')
    e2.place(x=140, y=40)

    e3 = Entry(root, bg='#ede0d4')
    e3.place(x=140, y=70)

    e4 = Entry(root, bg='#ede0d4')
    e4.place(x=140, y=100)

    e5 = Entry(root, bg='#ede0d4')
    e5.place(x=140, y=130)

    e6 = Entry(root, bg='#ede0d4')
    e6.place(x=140, y=160)

    Button(root, text="Add", command=combine(commitaddundelivered, root.destroy), height=2, width=13, bg='#ede0d4').place(x=165, y=190)

    root.mainloop()


def commitaddundelivered():
    orderid = e1.get()
    name = e2.get()
    quantity = e3.get()
    status = e4.get()
    clientname = e5.get()
    clientdetails = e6.get()

    mysqldb = con.connect(host="localhost", user="root", password="root", database="factory")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO undelivered VALUES (%s, %s, %s, %s, %s, %s)"
        val = (orderid, name, quantity, status, clientname, clientdetails)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record inserted successfully...")


    except Exception:
        mysqldb.rollback()
        mysqldb.close()


def removeundelivered():
    global c1
    root = Tk()
    root.title("Data Input")
    root.geometry("300x250")
    root.config(bg='#ddb892')

    Label(root, text="Order ID", bg='#ddb892').place(x=10, y=10)

    c1 = Entry(root, bg='#ede0d4')
    c1.place(x=140, y=10)

    Button(root, text="Remove", command=combine(commitremoveundelivered, root.destroy), height=2, width=13, bg='#ede0d4').place(x=165, y=190)

    root.mainloop()


def commitremoveundelivered():
    orderid = c1.get()

    mysqldb = con.connect(host="localhost", user="root", password="root", database="factory")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from undelivered where ordreid = '" + orderid + "'"
        val = orderid
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record deleted successfully...")


    except Exception:
        mysqldb.rollback()
        mysqldb.close()


def addorder():
    global a1
    global a2
    global a3
    global a4
    global a5
    root = Tk()
    root.title("Data Input")
    root.geometry("300x250")
    root.config(bg='#ddb892')

    Label(root, text="Name", bg='#ddb892').place(x=10, y=10)
    Label(root, text="Quantity", bg='#ddb892').place(x=10, y=40)
    Label(root, text="Status", bg='#ddb892').place(x=10, y=70)
    Label(root, text="Client Name", bg='#ddb892').place(x=10, y=100)
    Label(root, text="Client Details", bg='#ddb892').place(x=10, y=130)

    a1 = Entry(root, bg='#ede0d4')
    a1.place(x=140, y=10)

    a2 = Entry(root, bg='#ede0d4')
    a2.place(x=140, y=40)

    a3 = Entry(root, bg='#ede0d4')
    a3.place(x=140, y=70)

    a4 = Entry(root, bg='#ede0d4')
    a4.place(x=140, y=100)

    a5 = Entry(root, bg='#ede0d4')
    a5.place(x=140, y=130)

    Button(root, text="Add", command=combine(commitaddorder, root.destroy), height=2, width=13, bg='#ede0d4').place(x=165, y=190)

    root.mainloop()


def commitaddorder():
    name = a1.get()
    quantity = a2.get()
    status = a3.get()
    clientname = a4.get()
    clientdetails = a5.get()

    mysqldb = con.connect(host="localhost", user="root", password="root", database="factory")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO orderdetails VALUES (%s, %s, %s, %s, %s)"
        val = (name, quantity, status, clientname, clientdetails)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record inserted successfully...")


    except Exception:
        mysqldb.rollback()
        mysqldb.close()


def removeorder():
    global b1
    root = Tk()
    root.title("Data Input")
    root.geometry("300x250")
    root.config(bg='#ddb892')

    Label(root, text="Name", bg='#ddb892').place(x=10, y=10)

    b1 = Entry(root, bg='#ede0d4')
    b1.place(x=140, y=10)

    Button(root, text="Remove", command=combine(commitremoveorder, root.destroy), height=2, width=13, bg='#ede0d4').place(x=165, y=190)

    root.mainloop()


def commitremoveorder():
    name = b1.get()

    mysqldb = con.connect(host="localhost", user="root", password="root", database="factory")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from orderdetails where name = '" + name + "'"
        mycursor.execute(sql)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record deleted successfully...")


    except Exception:
        mysqldb.rollback()
        mysqldb.close()


def removeraw():
    global f1
    root = Tk()
    root.title("Data Input")
    root.geometry("300x250")
    root.config(bg='#ddb892')

    Label(root, text="Name", bg='#ddb892').place(x=10, y=10)

    f1 = Entry(root, bg='#ede0d4')
    f1.place(x=140, y=10)

    Button(root, text="Remove", command=combine(commitremoveraw, root.destroy), height=2, width=13, bg='#ede0d4').place(x=165, y=190)

    root.mainloop()


def commitremoveraw():
    name = f1.get()

    mysqldb = con.connect(host="localhost", user="root", password="root", database="factory")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from rawmaterials where name = '" + name + "'"
        mycursor.execute(sql)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record deleted successfully...")


    except Exception:
        mysqldb.rollback()
        mysqldb.close()


def addraw():
    global d1
    global d2
    global d3
    global d4
    global d5
    root = Tk()
    root.title("Data Input")
    root.geometry("300x250")
    root.config(bg='#ddb892')

    Label(root, text="SNO", bg='#ddb892').place(x=10, y=10)
    Label(root, text="Name", bg='#ddb892').place(x=10, y=40)
    Label(root, text="Quantity", bg='#ddb892').place(x=10, y=70)
    Label(root, text="Distributor", bg='#ddb892').place(x=10, y=100)
    Label(root, text="Status", bg='#ddb892').place(x=10, y=130)

    d1 = Entry(root, bg='#ede0d4')
    d1.place(x=140, y=10)

    d2 = Entry(root, bg='#ede0d4')
    d2.place(x=140, y=40)

    d3 = Entry(root, bg='#ede0d4')
    d3.place(x=140, y=70)

    d4 = Entry(root, bg='#ede0d4')
    d4.place(x=140, y=100)

    d5 = Entry(root, bg='#ede0d4')
    d5.place(x=140, y=130)

    Button(root, text="Add", command=combine(commitaddraw, root.destroy), height=2, width=13, bg='#ede0d4').place(x=165, y=190)

    root.mainloop()


def commitaddraw():
    sno = d1.get()
    name = d2.get()
    quantity = d3.get()
    distributor = d4.get()
    status = d5.get()

    mysqldb = con.connect(host="localhost", user="root", password="root", database="factory")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO rawmaterials VALUES (%s, %s, %s, %s, %s)"
        val = (sno, name, quantity, distributor, status)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record inserted successfully...")


    except Exception:
        mysqldb.rollback()
        mysqldb.close()


def success():
    messagebox.showinfo('', 'Task Initiated successfully.')


def orderdetails():
    mysqldb = con.connect(host='localhost', user='root', passwd='root', database='factory')
    cursor = mysqldb.cursor()

    cursor.execute('use factory')
    sql = 'select * from orderdetails'
    cursor.execute(sql)
    fetch1 = cursor.fetchall()

    root = Tk()
    root.title("Order Details")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Details", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    tableFrame1 = Frame(root, bg='black', bd=5)
    tableFrame1.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.5)

    Label(tableFrame1, text="%-20s%-20s%-20s%-10s%-70s" % ('Name', 'Quantity', 'Status',
                                                           'Client Name', '    Client Details'), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(tableFrame1, text="----------------------------------------------------------------------------------------"
          , bg='black', fg='white').place(relx=0.05, rely=0.2)

    placement = 0.3
    for i in range(len(fetch1)):
        Label(tableFrame1, text="%-20s%-20s%-20s%-20s%-70s" % (fetch1[i][0], fetch1[i][1], fetch1[i][2], fetch1[i][3],
                                                               fetch1[i][4]),
              bg='black', fg='white').place(relx=0.07, rely=placement)
        placement += 0.1

    quitBtn = Button(root, text="Back", fg='black', command=root.destroy, bg='#ede0d4')
    quitBtn.place(relx=0.75, rely=0.9, relwidth=0.18, relheight=0.08)

    addBtn = Button(root, text="Add new order", command=addorder, bg='#ede0d4')
    addBtn.place(relx=0.40, rely=0.9, relwidth=0.18, relheight=0.08)

    addBtn = Button(root, text="Remove order", command=removeorder, bg='#ede0d4')
    addBtn.place(relx=0.07, rely=0.9, relwidth=0.18, relheight=0.08)

    mysqldb.close()


def rawmaterials():
    mysqldb = con.connect(host='localhost', user='root', passwd='root', database='factory')
    cursor = mysqldb.cursor()

    cursor.execute('use factory')
    sql = 'select * from rawmaterials'
    cursor.execute(sql)
    fetch1 = cursor.fetchall()

    root = Tk()
    root.title("Raw Materials")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Raw Materials", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    tableFrame1 = Frame(root, bg='black', bd=5)
    tableFrame1.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.5)

    Label(tableFrame1, text="%-10s%-40s%-30s%-20s%-20s" % ('SNo.', 'Name', 'Quantity', 'Distributor', 'Status'),
          bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(tableFrame1, text="-" * 90,
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    placement = 0.3
    for i in range(len(fetch1)):
        Label(tableFrame1, text="%-10s%-50s%-20s%-30s%-70s" % (fetch1[i][0], fetch1[i][1], fetch1[i][2], fetch1[i][3],
                                                               fetch1[i][4]),
              bg='black', fg='white').place(relx=0.07, rely=placement)
        placement += 0.1

    quitBtn = Button(root, text="Back", fg='black', command=root.destroy, bg='#ede0d4')
    quitBtn.place(relx=0.75, rely=0.9, relwidth=0.18, relheight=0.08)

    addBtn = Button(root, text="Add new material", command=addraw, bg='#ede0d4')
    addBtn.place(relx=0.40, rely=0.9, relwidth=0.18, relheight=0.08)

    addBtn = Button(root, text="Remove material", command=removeraw, bg='#ede0d4')
    addBtn.place(relx=0.07, rely=0.9, relwidth=0.18, relheight=0.08)

    mysqldb.close()


def stocks():
    root = Tk()
    root.title("Stocks")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Stocks", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    tableFrame1 = Frame(root, bg='black', bd=5)
    tableFrame1.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.5)

    Label(tableFrame1, text="%-10s%-40s%-30s%-20s" % ('SNo.', 'Name', 'Quantity', 'Distributor'), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(tableFrame1, text="----------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    Label(tableFrame1, text="%-10s%-40s%-30s%-20s" % ('1       ', 'Iron  ', '4500', 'Bharat Metals'),
          bg='black', fg='white').place(relx=0.07, rely=0.3)

    Label(tableFrame1, text="%-10s%-40s%-30s%-20s" % ('2      ', 'Graphite   ', '50 ', 'Graphite Sheet'),
          bg='black', fg='white').place(relx=0.07, rely=0.4)

    '''image1 = Image.open("Stocks.jpg")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0.5, y=0.5)'''

    quit_Btn = Button(root, text="Back", fg='black', command=root.destroy, bg='#ede0d4')
    quit_Btn.place(relx=0.77, rely=0.9, relwidth=0.18, relheight=0.08)


def statistics():
    root = Tk()
    root.title("Statistics")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Statistics", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    tableFrame1 = Frame(root, bg='#D6ED17', bd=5)
    tableFrame1.place(relx=0.25, rely=0.25, relwidth=0.9, relheight=0.5)

    Label(tableFrame1, text='Check the latest Company statistics here!!', bg='#D6ED17',
          fg='black').place(relx=0.05, rely=0.01)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = Treeview(TableMargin, columns=("Governance Factors", "Positive Econ. Profit", "PN 4 Companies",
                                          'Negative Econ. Profit', 'Pos. vs PN4', 'Neg. vs PN4'),
                    height=700, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Governance Factors', text="Governance Factors", anchor=W)
    tree.heading('Positive Econ. Profit', text="Positive Econ. Profit", anchor=W)
    tree.heading('PN 4 Companies', text="PN 4 Companies", anchor=W)
    tree.heading('Negative Econ. Profit', text='Negative Econ. Profit', anchor=W)
    tree.heading('Pos. vs PN4', text='Pos. vs PN4', anchor=W)
    tree.heading('Neg. vs PN4', text='Neg. vs PN4', anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=300)
    tree.column('#5', stretch=NO, minwidth=0, width=300)
    tree.column('#6', stretch=NO, minwidth=0, width=300)
    tree.pack()
    with open('test.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            GovernanceFactors = row['Governance Factors']
            PositiveEconProfit = row['Positive Econ. Profit']
            PN4Companies = row['PN 4 Companies']
            NegativeEconProfit = row['Negative Econ. Profit']
            PosvsPN4 = row['Pos. vs PN4']
            NegvsPN4 = row['Neg. vs PN4']
            tree.insert("", 0, values=(GovernanceFactors, PositiveEconProfit, PN4Companies, NegativeEconProfit,
                                       PosvsPN4, NegvsPN4))

    quitBtn = Button(root, text="Back", fg='black', command=root.destroy, bg='#ede0d4')
    quitBtn.place(relx=0.82, rely=0.45, relwidth=0.18, relheight=0.08)


def undelivered():
    mysqldb = con.connect(host='localhost', user='root', passwd='root', database='factory')
    cursor = mysqldb.cursor()

    cursor.execute('use factory')
    sql = 'select * from undelivered'
    cursor.execute(sql)
    fetch1 = cursor.fetchall()

    root = Tk()
    root.title("Undelivered")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff1a1a")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Undelivered \n Orders", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    tableFrame1 = Frame(root, bg='black', bd=5)
    tableFrame1.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.5)

    Label(tableFrame1, text="%-5s%-20s%-20s%-20s%-10s%-70s" % ('Order ID    ', 'Name', 'Quantity', 'Status',
                                                               'Client Name', '    Client Details'), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(tableFrame1, text="----------------------------------------------------------------------------------------"
          , bg='black', fg='white').place(relx=0.05, rely=0.2)

    placement = 0.3
    for i in range(0, len(fetch1)):
        Label(tableFrame1, text="%-10s%-20s%-20s%-25s%-15s%-70s" % (fetch1[i][0], fetch1[i][1], fetch1[i][2],
                                                                    fetch1[i][3], fetch1[i][4], fetch1[i][5]),
              bg='black', fg='white').place(relx=0.07, rely=placement)
        placement += 0.1

    quitBtn = Button(root, text="Back", fg='black', command=root.destroy, bg='#ede0d4')
    quitBtn.place(relx=0.75, rely=0.9, relwidth=0.18, relheight=0.08)

    addBtn = Button(root, text="Add order", command=addundelivered, bg='#ede0d4')
    addBtn.place(relx=0.40, rely=0.9, relwidth=0.18, relheight=0.08)

    addBtn = Button(root, text="Remove order", command=removeundelivered, bg='#ede0d4')
    addBtn.place(relx=0.07, rely=0.9, relwidth=0.18, relheight=0.08)

    mysqldb.close()


root = Tk()
root.title("Factory Management")
root.minsize(width=400, height=400)
root.geometry("600x500")

background_image = Image.open("laptops.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)
headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome! To Factory \n Database Management System", bg='black', fg='white',
                     font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
btn1 = Button(root, text="Order Details", bg='black', fg='white', command=orderdetails)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Raw material inputs", bg='black', fg='white', command=rawmaterials)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Stocks", bg='black', fg='white', command=stocks)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Statistics", bg='black', fg='white', command=statistics)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Undelivered orders", bg='black', fg='white', command=undelivered)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
quitBtn.place(relx=0.8, rely=0.91, relwidth=0.18, relheight=0.08)

root.mainloop()
