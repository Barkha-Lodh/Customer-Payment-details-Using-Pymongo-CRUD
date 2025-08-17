from tkinter import *
from tkinter import ttk, messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId

# Database Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["Payment_db_463"]
collection = db["payments_463"]

# CRUD
def insert_payment():
    payment = {
        "order_id": entry_order_id.get(),
        "payment_date": entry_payment_date.get(),
        "payment_method": entry_payment_method.get(),
        "payment_status": entry_payment_status.get(),
        "payment_amount": entry_payment_amount.get()
    }
    collection.insert_one(payment)
    messagebox.showinfo("Success", "Payment inserted!")
    show_payments()

def show_payments():
    for row in tree.get_children():
        tree.delete(row)

    serial_no = 1
    for payment in collection.find():
        tree.insert("", "end", values=(serial_no, payment["_id"], payment["order_id"], payment["payment_date"],
                                       payment["payment_method"], payment["payment_status"],
                                       payment["payment_amount"]))
        serial_no += 1


def delete_payment():
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")
    collection.delete_one({"_id": ObjectId(values[1])})  # ObjectId
    messagebox.showinfo("Deleted", "Payment deleted")
    show_payments()


def update_payment():
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")

    updated_data = {
        "order_id": entry_order_id.get(),
        "payment_date": entry_payment_date.get(),
        "payment_method": entry_payment_method.get(),
        "payment_status": entry_payment_status.get(),
        "payment_amount": entry_payment_amount.get()
    }

    collection.update_one({"_id": ObjectId(values[1])}, {"$set": updated_data})
    messagebox.showinfo("Updated", "Payment updated")
    show_payments()


def read_payments():
    show_payments()

# GUI
root = Tk()
root.title("Payment Management App 463 (MongoDB CRUD)")
root.geometry("800x500")

# Custom font for all fields and buttons
custom_font = ('Georgia', 10)
label_font = ('Georgia', 10)
button_font = ('Georgia', 10, 'bold')

Label(root, text="Order ID", font=label_font).grid(row=0, column=0, padx=10, pady=5)
entry_order_id = Entry(root, width=30, font=custom_font)
entry_order_id.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Payment Date", font=label_font).grid(row=1, column=0, padx=10, pady=5)
entry_payment_date = Entry(root, width=30, font=custom_font)
entry_payment_date.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Payment Method", font=label_font).grid(row=2, column=0, padx=10, pady=5)
entry_payment_method = Entry(root, width=30, font=custom_font)
entry_payment_method.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Payment Status", font=label_font).grid(row=3, column=0, padx=10, pady=5)
entry_payment_status = Entry(root, width=30, font=custom_font)
entry_payment_status.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Payment Amount", font=label_font).grid(row=4, column=0, padx=10, pady=5)
entry_payment_amount = Entry(root, width=30, font=custom_font)
entry_payment_amount.grid(row=4, column=1, padx=10, pady=5)

# Buttons with colors and font
button_height = 1
button_width = 18

frame_buttons = Frame(root)
frame_buttons.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

Button(frame_buttons, text="Insert", command=insert_payment, width=button_width, height=button_height, bg="blue",
       fg="white", font=button_font).grid(row=0, column=0, padx=10, pady=10)

Button(frame_buttons, text="Read Payments", command=read_payments, width=button_width, height=button_height, bg="blue",
       fg="white", font=button_font).grid(row=0, column=1, padx=10, pady=10)

Button(frame_buttons, text="Update Payment", command=update_payment, width=button_width, height=button_height,bg="blue",
       fg="white", font=button_font).grid(row=0, column=2, padx=10, pady=10)

Button(frame_buttons, text="Delete Payment", command=delete_payment, width=button_width, height=button_height, bg="blue",
       fg="white", font=button_font).grid(row=0, column=3, padx=10, pady=10)

columns = ("Sr. No.", "ID", "Order ID", "Payment Date", "Payment Method", "Payment Status", "Payment Amount")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")  # Align column text to the center

tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

show_payments()

root.mainloop()
