import sqlite3 as sq3
from tkinter import *
import tkinter as tk
from datetime import datetime
import re
import sqlite3
import csv


conn = sq3.connect('Shop.sqlite')

def addCustomer(name, family, phone):
    customerName = name.get()
    customerFamily = family.get()
    customerPhone = phone.get()
    createTime = datetime.now()

    # fist check not be any empty input
    if customerName == '' or customerFamily == '' or customerPhone == '':
        massage = 'Please fill all input'
        text.insert(tk.END, f"{massage}\n")
    # second-2 insert values in customer table
    else:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Customer (id, name, surname, phone_number, create_time) VALUES (NULL, ?, ?, ?, ?)
            ''', (customerName, customerFamily, customerPhone, str(createTime)))
            conn.commit()
            massage = f'Customer {customerName} {customerFamily} added'
            text.insert(tk.END, f"{massage}\n")
        except sq3.IntegrityError as e:
            print(f'SQLITE ERROR: {e}')
        
        name.delete(0, 'end')
        family.delete(0, 'end')
        phone.delete(0, 'end')

def customerSelector(name, family, phone, id):
    customerName = name.get()
    customerFamily = family.get()
    customerPhone = phone.get()
    customerId = id.get()

    # fist check not be any empty input
    if customerName == '' and customerFamily == '' and customerPhone == '' and customerId == '':
        if querySelector('customers', '','','','', all=1):
            selectResult = querySelector('customers', '','','','', all=1)
            text.insert(tk.END, f"{selectResult}\n")
    else:
        if querySelector('customers', customerId, customerName, customerFamily, customerPhone):
            selectResult = querySelector('customers', customerId, customerName, customerFamily, customerPhone)
            text.insert(tk.END, f"{selectResult}\n")
        else:
            massage = "The customer doesn't exist"
            text.insert(tk.END, f"{massage}\n")

def querySelector(tableName, id, name, family="", phone="", count="", price="", user_id="", all=0):
    match tableName:
        case 'customers':
            cursor = conn.cursor()
            if all==1:
                query = cursor.execute('''SELECT * FROM Customer''')
                result = query.fetchall()
                return result
            if id != "":
                query = cursor.execute('''
                                    SELECT * FROM Customer WHERE id=?
                                ''', (id, ))
                result = query.fetchall()
                return result
            if name != "" and family == "" and phone == "":
                query = cursor.execute('''
                                    SELECT * FROM Customer WHERE name=?
                                ''', (name, ))
                result = query.fetchall()
                return result
            if family != "" and name == "" and phone == "":
                query = cursor.execute('''
                                    SELECT * FROM Customer WHERE surname=?
                                ''', (family, ))
                result = query.fetchall()
                return result
            if phone != "" and name == "" and family == "":
                query = cursor.execute('''
                                    SELECT * FROM Customer WHERE phone_number=?
                                ''', (phone, ))
                result = query.fetchall()
                return result
            if name != "" and family != "" and phone == "":
                query = cursor.execute('''
                    SELECT * FROM Customer WHERE name=? AND surname=?
                ''',(name, family))
                result = query.fetchall()
                return result
            if name !="" and phone != "" and family == "":
                query = cursor.execute('''
                    SELECT * FROM Customer WHERE name=? AND phone_number=?
                ''',(name, phone))
                result = query.fetchall()
                return result
            if phone != "" and family != "" and name == "":
                query = cursor.execute('''
                    SELECT * FROM Customer WHERE surname=? AND phone_number=?
                ''',(family, phone))
                result = query.fetchall()
                return result
            elif name != "" and family != "" and phone != "":
                query = cursor.execute('''
                    SELECT * FROM Customer WHERE name=? AND surname=? AND phone_number=?
                ''',(name, family, phone))
                result = query.fetchall()
                return result
        case 'invoice':
            cursor = conn.cursor()
            if all == 1:
                query = cursor.execute(''' SELECT * FROM Invoice''')
                result = query.fetchall()
                return result
            if id != '':
                query = cursor.execute('''
                    SELECT * FROM Invoice WHERE id=?
                ''', (id, ))
                result = query.fetchall()
                return result
            if name != '' and price == "" and user_id == "":
                query = cursor.execute('''
                    SELECT * FROM Invoice WHERE name=?
                ''', (name, ))
                result = query.fetchall()
                return result
            if price !='' and name == "" and user_id == "":
                query = cursor.execute('''
                    SELECT * FROM Invoice WHERE price=?
                ''', (price, ))
                result = query.fetchall()
                return result
            if user_id !='' and name == "" and price == "":
                query = cursor.execute('''
                    SELECT * FROM Invoice WHERE user_id=?
                ''', (user_id, ))
                result = query.fetchall()
                return result
            if name != "" and price !="" and user_id == "":
                query = cursor.execute('''
                    SELECT * FROM Invoice WHERE name=? AND price=?
                ''', (name, price))
                result = query.fetchall()
                return result
            if name != "" and user_id !="" and price == "":
                query = cursor.execute('''
                    SELECT * FROM Invoice WHERE name=? AND user_id=?
                ''', (name, user_id))
                result = query.fetchall()
                return result
            if price !="" and user_id != "" and name == "":
                query = cursor.execute('''
                    SELECT * FROM Invoice WHERE price=? AND user_id=?
                ''', (price, user_id))
                result = query.fetchall()
                return result
            elif name != '' and price != '' and user_id !='':
                query = cursor.execute('''
                    SELECT * FROM Invoice WHERE name=? AND price=? AND user_id=?
                ''', (name, price, user_id))
                result = query.fetchall()
                return result
        case 'storage':
            cursor = conn.cursor()
            if all == 1:
                query = cursor.execute(''' SELECT * FROM Storage''')
                result = query.fetchall()
                return result
            if id != '':
                query = cursor.execute('''
                        SELECT * FROM Storage WHERE id=?
                    ''', (id,))
                result = query.fetchall()
                return result
            if name != '' and count == "":
                query = cursor.execute('''
                        SELECT * FROM Storage WHERE name=?
                    ''', (name,))
                result = query.fetchall()
                return result
            if count != '' and name == "":
                query = cursor.execute('''
                        SELECT * FROM Storage WHERE count=?
                    ''', (count,))
                result = query.fetchall()
                return result
            elif name != '' and count != '':
                query = cursor.execute('''
                        SELECT * FROM Storage WHERE name=? AND count=?
                    ''', (name, count))
                result = query.fetchall()
                return result


def updateCustomer(name, family, phone, id):
    customerName = name.get()
    customerFamily = family.get()
    customerPhone = phone.get()
    customerId = id.get()
    createTime = datetime.now()

    if customerName == '' or customerFamily == '' or customerPhone == '' or customerId == '':
        massage = 'Please fill all input'
        text.insert(tk.END, f"{massage}\n")
    else:
        cursor = conn.cursor()
        cursor.execute('''
                        UPDATE Customer SET name=?, surname=?, phone_number=?, create_time=? WHERE id=?
                    ''', (customerName, customerFamily, customerPhone, str(createTime), customerId))
        conn.commit()
        text.insert(tk.END, f"id: {customerId} is updated to {customerName} {customerFamily}, time: {str(createTime)}\n")

    name.delete(0, 'end')
    family.delete(0, 'end')
    phone.delete(0, 'end')

def deleteCustomer(id):
    customerId = id.get()
    if customerId == '':
        massage = 'Please fill ID input'
        text.insert(tk.END, f"{massage}\n")
    else:
        cursor = conn.cursor()
        cursor.execute('''
                        DELETE FROM Customer WHERE id=?
                    ''', (customerId,))
        conn.commit()
        text.insert(tk.END, f"id: {customerId} is Deleted\n")



def addInvoice(name, price, userid):

    invoiceName = name.get()
    invoicePrice = price.get()
    invoiceUser_id = userid.get()
    createTime = datetime.now()

    # fist check not be any empty input
    if invoiceName == '' or invoicePrice == '' or invoiceUser_id == '':
        massage = 'Please fill all input'
        text.insert(tk.END, f"{massage}\n")
    # second-2 insert values in customer table
    else:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Invoice (id, name, price, user_id, create_time) VALUES (NULL, ?, ?, ?, ?)
            ''', (invoiceName, invoicePrice, invoiceUser_id, str(createTime)))
            conn.commit()
            massage = f'Invoice {invoiceName} {invoicePrice} added'
            textInvoice.insert(tk.END, f"{massage}\n")
        except sq3.IntegrityError as e:
            print(f'SQLITE ERROR: {e}')

        name.delete(0, 'end')
        price.delete(0, 'end')
        userid.delete(0, 'end')

def updateInvoice(name, price, userid, invoiceid):
    invoiceName = name.get()
    invoicePrice = price.get()
    invoiceUser_id = userid.get()
    invoice_id = invoiceid.get()
    createTime = datetime.now()

    if invoiceName == '' or invoicePrice == '' or invoiceUser_id == '' or invoice_id == '':
        massage = 'Please fill all input'
        textInvoice.insert(tk.END, f"{massage}\n")
    else:
        cursor = conn.cursor()
        cursor.execute('''
                        UPDATE Invoice SET name=?, price=?, user_id=?, create_time=? WHERE id=?
                    ''', (invoiceName, invoicePrice, invoiceUser_id, str(createTime), invoice_id))
        conn.commit()
        textInvoice.insert(tk.END, f"id: {invoice_id} is updated to {invoiceName} {invoicePrice}, time: {str(createTime)}\n")

    name.delete(0, 'end')
    price.delete(0, 'end')
    userid.delete(0, 'end')

def InvoiceSelector(name, price, userid, invoiceid):
    invoiceName = name.get()
    invoicePrice = price.get()
    invoiceUser_id = userid.get()
    invoice_id = invoiceid.get()

    # fist check not be any empty input
    if invoiceName == '' and invoicePrice == '' and invoiceUser_id == '' and invoice_id == '':
        if querySelector('invoice', id='',name='',price='',user_id='', all=1):
            selectResult = querySelector('invoice', id='',name='',price='',user_id='', all=1)
            textInvoice.insert(tk.END, f"{selectResult}\n")
    else:
        if querySelector('invoice', id=invoice_id, name=invoiceName, price=invoicePrice, user_id=invoiceUser_id):
            selectResult = querySelector('invoice', id=invoice_id, name=invoiceName, price=invoicePrice, user_id=invoiceUser_id)
            textInvoice.insert(tk.END, f"{selectResult}\n")
        else:
            massage = "The Invoice doesn't exist"
            textInvoice.insert(tk.END, f"{massage}\n")

def deleteInvoice(id):
    invoiceId = id.get()
    if invoiceId == '':
        massage = 'Please fill ID input'
        textInvoice.insert(tk.END, f"{massage}\n")
    else:
        cursor = conn.cursor()
        cursor.execute('''
                        DELETE FROM Invoice WHERE id=?
                    ''', (invoiceId,))
        conn.commit()
        textInvoice.insert(tk.END, f"id: {invoiceId} is Deleted\n")


def addStorage(name, count):

    storageName = name.get()
    storageCount = count.get()
    createTime = datetime.now()

    # fist check not be any empty input
    if storageName == '' or storageCount == '' :
        massage = 'Please fill all input'
        textStorage.insert(tk.END, f"{massage}\n")
    # second-2 insert values in customer table
    else:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Storage (id, name, count, create_time) VALUES (NULL, ?, ?, ?)
            ''', (storageName, storageCount, str(createTime)))
            conn.commit()
            massage = f'Storage {storageName} with number of {storageCount} added'
            textStorage.insert(tk.END, f"{massage}\n")
        except sq3.IntegrityError as e:
            print(f'SQLITE ERROR: {e}')

        name.delete(0, 'end')
        count.delete(0, 'end')

def storageSelector(name, count, id):
    storageName = name.get()
    storageCount = count.get()
    storageId = id.get()

    # fist check not be any empty input
    if storageName == '' and storageCount == '' and storageId == '':
        if querySelector('storage', id='', name='', count='', all=1):
            selectResult = querySelector('storage', id='', name='', count='', all=1)
            textStorage.insert(tk.END, f"{selectResult}\n")
    else:
        if querySelector('storage', id=storageId, name=storageName, count=storageCount):
            selectResult = querySelector('storage', id=storageId, name=storageName, count=storageCount)
            textStorage.insert(tk.END, f"{selectResult}\n")
        else:
            massage = "The Storage doesn't exist"
            textStorage.insert(tk.END, f"{massage}\n")

def updateStorage(name, count, id):

    storageName = name.get()
    storageCount = count.get()
    storageId = id.get()
    createTime = datetime.now()

    if storageName == '' or storageCount == '' or storageId == '':
        massage = 'Please fill all input'
        textStorage.insert(tk.END, f"{massage}\n")
    else:
        cursor = conn.cursor()
        cursor.execute('''
                        UPDATE Storage SET name=?, count=?, create_time=? WHERE id=?
                    ''', (storageName, storageCount, str(createTime), storageId))
        conn.commit()
        textStorage.insert(tk.END, f"id: {storageId} is updated to {storageName} {storageCount}, time: {str(createTime)}\n")

    name.delete(0, 'end')
    count.delete(0, 'end')
    id.delete(0, 'end')

def deleteStorage(id):
    storageId = id.get()
    if storageId == '':
        massage = 'Please fill ID input'
        textStorage.insert(tk.END, f"{massage}\n")
    else:
        cursor = conn.cursor()
        cursor.execute('''
                        DELETE FROM Storage WHERE id=?
                    ''', (storageId,))
        conn.commit()
        textStorage.insert(tk.END, f"id: {storageId} is Deleted\n")

root = Tk()
root.title('Main Page')
root.geometry("500x600")
root.config(background="#bdc3c7", padx="20px", pady="20px")

def customerWindowMaker():
    customerWindow = Tk()
    customerWindow.title('Customers')
    customerWindow.geometry("600x800")
    customerWindow.config(background="#eee", padx="20px", pady="20px") 

    customerAddButton = Button(customerWindow, text="Add", command=lambda: addCustomer(name_input, family_input, phone_number_input), font='Helvetica 11 bold', cursor="hand2")
    customerAddButton.grid(row=1, column=0, pady="10px")
    customerUpdateButton = Button(customerWindow, text="Update", command=lambda: updateCustomer(name_input, family_input, phone_number_input, id_input), font='Helvetica 11 bold', cursor="hand2")
    customerUpdateButton.grid(row=1, column=1, pady="10px")
    customerDeleteButton = Button(customerWindow, text="Delete", command=lambda: deleteCustomer(id_input), font='Helvetica 11 bold', cursor="hand2")
    customerDeleteButton.grid(row=1, column=2, pady="10px")
    customerSelectButton = Button(customerWindow, text="Select", command=lambda: customerSelector(name_input, family_input, phone_number_input, id_input), font='Helvetica 11 bold', cursor="hand2")
    customerSelectButton.grid(row=1, column=3, pady="10px")



    name_lable = Label(customerWindow, text="Name: ", font='Helvetica 10 bold')
    name_lable.grid(row=3, column=1, sticky=tk.E, pady="15px")

    name_input = Entry(customerWindow)
    name_input.grid(row=3, column=2, pady="15px")


    family_lable = Label(customerWindow, text="Family: ", font='Helvetica 10 bold')
    family_lable.grid(row=4, column=1, sticky=tk.E, pady="15px")

    family_input = Entry(customerWindow)
    family_input.grid(row=4, column=2, pady="15px")


    phone_number_lable = Label(customerWindow, text="Phone Number: ", font='Helvetica 10 bold', anchor="w")
    phone_number_lable.grid(row=5, column=1, sticky=tk.E, pady="15px")

    phone_number_input = Entry(customerWindow)
    phone_number_input.grid(row=5, column=2, pady="15px")


    id_lable = Label(customerWindow, text="ID Number: ", font='Helvetica 10 bold', anchor="w")
    id_lable.grid(row=6, column=1, sticky=tk.E, pady="15px")

    id_input = Entry(customerWindow)
    id_input.grid(row=6, column=2, pady="15px")
    
    global text
    text = Text(customerWindow, height=6, width=40)
    text.grid(row=7, column=0, columnspan=4, pady="15px")

    customer_col_count, customer_row_count = customerWindow.grid_size()
    for col in range(customer_col_count):
        customerWindow.grid_columnconfigure(col, minsize=130)
    for row in range(customer_row_count):
        customerWindow.grid_rowconfigure(row, minsize=70)

def invoiceWindowMaker():
    invoiceWindow = Tk()
    invoiceWindow.title('Invoice')
    invoiceWindow.geometry("600x800")
    invoiceWindow.config(background="#eee", padx="20px", pady="20px")

    invoiceAddButton = Button(invoiceWindow, text="Add",
                               command=lambda: addInvoice(name_input, price_input, user_id_input),
                               font='Helvetica 11 bold', cursor="hand2")
    invoiceAddButton.grid(row=1, column=0, pady="10px")
    invoiceUpdateButton = Button(invoiceWindow, text="Update",
                                  command=lambda: updateInvoice(name_input, price_input, user_id_input,id_input), font='Helvetica 11 bold', cursor="hand2")
    invoiceUpdateButton.grid(row=1, column=1, pady="10px")
    invoiceDeleteButton = Button(invoiceWindow, text="Delete", command=lambda: deleteInvoice(id_input),
                                  font='Helvetica 11 bold', cursor="hand2")
    invoiceDeleteButton.grid(row=1, column=2, pady="10px")
    invoiceSelectButton = Button(invoiceWindow, text="Select",
                                  command=lambda: InvoiceSelector(name_input, price_input, user_id_input, id_input), font='Helvetica 11 bold', cursor="hand2")
    invoiceSelectButton.grid(row=1, column=3, pady="10px")

    name_lable = Label(invoiceWindow, text="Name: ", font='Helvetica 10 bold')
    name_lable.grid(row=3, column=1, sticky=tk.E, pady="15px")

    name_input = Entry(invoiceWindow)
    name_input.grid(row=3, column=2, pady="15px")

    price_lable = Label(invoiceWindow, text="Price: ", font='Helvetica 10 bold')
    price_lable.grid(row=4, column=1, sticky=tk.E, pady="15px")

    price_input = Entry(invoiceWindow)
    price_input.grid(row=4, column=2, pady="15px")

    user_id_lable = Label(invoiceWindow, text="User ID: ", font='Helvetica 10 bold', anchor="w")
    user_id_lable.grid(row=5, column=1, sticky=tk.E, pady="15px")

    user_id_input = Entry(invoiceWindow)
    user_id_input.grid(row=5, column=2, pady="15px")

    id_lable = Label(invoiceWindow, text="ID Number: ", font='Helvetica 10 bold', anchor="w")
    id_lable.grid(row=6, column=1, sticky=tk.E, pady="15px")

    id_input = Entry(invoiceWindow)
    id_input.grid(row=6, column=2, pady="15px")

    global textInvoice
    textInvoice = Text(invoiceWindow, height=6, width=40)
    textInvoice.grid(row=7, column=0, columnspan=4, pady="15px")

    invoice_col_count, invoice_row_count = invoiceWindow.grid_size()
    for col in range(invoice_col_count):
        invoiceWindow.grid_columnconfigure(col, minsize=130)
    for row in range(invoice_row_count):
        invoiceWindow.grid_rowconfigure(row, minsize=70)


def storageWindowMaker():
    storageWindow = Tk()
    storageWindow.title('Storage')
    storageWindow.geometry("600x800")
    storageWindow.config(background="#eee", padx="20px", pady="20px")

    storageAddButton = Button(storageWindow, text="Add",
                               command=lambda: addStorage(name_input, count_input),
                               font='Helvetica 11 bold', cursor="hand2")
    storageAddButton.grid(row=1, column=0, pady="10px")
    storageUpdateButton = Button(storageWindow, text="Update",
                                  command=lambda: updateStorage(name_input, count_input, id_input), font='Helvetica 11 bold', cursor="hand2")
    storageUpdateButton.grid(row=1, column=1, pady="10px")
    storageDeleteButton = Button(storageWindow, text="Delete", command=lambda: deleteStorage(id_input),
                                  font='Helvetica 11 bold', cursor="hand2")
    storageDeleteButton.grid(row=1, column=2, pady="10px")
    storageSelectButton = Button(storageWindow, text="Select",
                                  command=lambda: storageSelector(name_input, count_input, id_input), font='Helvetica 11 bold', cursor="hand2")
    storageSelectButton.grid(row=1, column=3, pady="10px")

    name_lable = Label(storageWindow, text="Name: ", font='Helvetica 10 bold')
    name_lable.grid(row=3, column=1, sticky=tk.E, pady="15px")

    name_input = Entry(storageWindow)
    name_input.grid(row=3, column=2, pady="15px")

    count_lable = Label(storageWindow, text="Count: ", font='Helvetica 10 bold')
    count_lable.grid(row=4, column=1, sticky=tk.E, pady="15px")

    count_input = Entry(storageWindow)
    count_input.grid(row=4, column=2, pady="15px")


    id_lable = Label(storageWindow, text="ID Number: ", font='Helvetica 10 bold', anchor="w")
    id_lable.grid(row=6, column=1, sticky=tk.E, pady="15px")

    id_input = Entry(storageWindow)
    id_input.grid(row=6, column=2, pady="15px")

    global textStorage
    textStorage = Text(storageWindow, height=6, width=40)
    textStorage.grid(row=7, column=0, columnspan=4, pady="15px")

    storage_col_count, storage_row_count = storageWindow.grid_size()
    for col in range(storage_col_count):
        storageWindow.grid_columnconfigure(col, minsize=130)
    for row in range(storage_row_count):
        storageWindow.grid_rowconfigure(row, minsize=70)
def windowOpener(windowsName):
    match windowsName:
        case 'customers':
            customerWindowMaker()
        case 'invoice':
            invoiceWindowMaker()
        case 'storage':
            storageWindowMaker()

def joinData():

    all_customers = querySelector('customers', '', '', '', '', all=1)
    all_invoices = querySelector('invoice', id='', name='', price='', user_id='', all=1)

    matches = []
    for customer in all_customers:
        customer_id = customer[0]
        for invoice in all_invoices:
            invoice_user_id = invoice[3]
            if customer_id == invoice_user_id:
                matches.append((customer, invoice))

    for customer, invoice in matches:
        textMain.insert(tk.END, f"customer:\n{customer}\ninvoice:\n{invoice}\n\n")

def saveCSV():
    table_csv_map = {
        'Invoice': 'Invoice.csv',
        'Customer': 'Customers.csv',
        'Storage': 'Storage.csv'
    }

    cursor = conn.cursor()
    for table, csv_filename in table_csv_map.items():

        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        column_names = [description[0] for description in cursor.description]

        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(column_names)

            writer.writerows(rows)

        textMain.insert(tk.END, f"Data from table '{table}' has been written to '{csv_filename}'.\n")


customer_win_button = Button(root, text="Customers", command=lambda: windowOpener('customers'), font='Helvetica 11 bold', cursor="hand2")
customer_win_button.grid(row=1, column=0, pady="10px")

invoice_win_button = Button(root, text="Invoice", command=lambda: windowOpener('invoice'), font='Helvetica 11 bold', cursor="hand2")
invoice_win_button.grid(row=1, column=1, pady="10px")

storage_win_button = Button(root, text="Storage", command=lambda: windowOpener('storage'), font='Helvetica 11 bold', cursor="hand2")
storage_win_button.grid(row=1, column=2, pady="10px")

join_button = Button(root, text="Join", command=lambda: joinData(), font='Helvetica 11 bold', cursor="hand2")
join_button.grid(row=3, column=0, pady="10px")

csv_button = Button(root, text="Save CSV", command=lambda: saveCSV(), font='Helvetica 11 bold', cursor="hand2")
csv_button.grid(row=3, column=2, pady="10px")

global textMain
textMain = Text(root, height=6, width=40)
textMain.grid(row=5, column=0, columnspan=3, pady="15px")

col_count, row_count = root.grid_size()
for col in range(col_count):
    root.grid_columnconfigure(col, minsize=140)
for row in range(row_count):
    root.grid_rowconfigure(row, minsize=70)

root.mainloop()
