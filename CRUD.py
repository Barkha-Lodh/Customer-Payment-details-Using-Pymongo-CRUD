import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# Database Connection
client = MongoClient("mongodb://localhost:27017")
db = client["Payment_db_463"]  # Database
collection = db["payments_463"]  # Payments Collection

# CRUD
def insert_payment():
    order_id = entry_order_id.get().strip()
    payment_date = entry_payment_date.get().strip()
    payment_method = entry_payment_method.get().strip()
    payment_status = entry_payment_status.get().strip()
    payment_amount = entry_payment_amount.get().strip()

    if not (order_id and payment_date and payment_method and payment_status and payment_amount):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        payment_date = datetime.datetime.strptime(payment_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    collection.insert_one({
        "order_id": order_id,
        "payment_date": payment_date,
        "payment_method": payment_method,
        "payment_status": payment_status,
        "payment_amount": float(payment_amount)
    })

    messagebox.showinfo("Success", f"Payment for order '{order_id}' added!")
    clear_fields()
    read_payments()


def read_payments():
    listbox.delete(0, tk.END)

    # Add a header for clarity with improved spacing
    listbox.insert(tk.END,
                   f"{'Date':<25} | {'Order ID':<20} | {'Payment Method':<25} | {'Payment Status':<25} | {'Payment Amount':<12}")
    listbox.insert(tk.END, "-" * 150)  # Add a separator line

    for payment in collection.find():
        listbox.insert(
            tk.END,
            f"{payment['payment_date'].strftime('%Y-%m-%d'):<15} | {payment['order_id']:<25} | {payment['payment_method']:<41} | "
            f"{payment['payment_status']:<30} | {payment['payment_amount']:<12.2f}"
        )

def update_payment():
    try:
        selected = listbox.get(listbox.curselection())
        payment_id = selected.split(" | ")[0].strip()
    except:
        messagebox.showwarning("Select a payment", "Click on a payment first")
        return

    order_id = entry_order_id.get().strip()
    payment_date = entry_payment_date.get().strip()
    payment_method = entry_payment_method.get().strip()
    payment_status = entry_payment_status.get().strip()
    payment_amount = entry_payment_amount.get().strip()

    if not (order_id and payment_date and payment_method and payment_status and payment_amount):
        messagebox.showerror("Error", "All fields are required to update!")
        return

    try:
        payment_date = datetime.datetime.strptime(payment_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    collection.update_one(
        {"_id": ObjectId(payment_id)},
        {"$set": {
            "order_id": order_id,
            "payment_date": payment_date,
            "payment_method": payment_method,
            "payment_status": payment_status,
            "payment_amount": float(payment_amount)
        }}
    )

    messagebox.showinfo("Updated", "Payment updated successfully!")
    clear_fields()
    read_payments()


def delete_payment():
    try:
        selected = listbox.get(listbox.curselection())
        payment_id = selected.split(" | ")[0].strip()
    except:
        messagebox.showwarning("Select a payment", "Click on a payment first")
        return

    collection.delete_one({"_id": ObjectId(payment_id)})
    messagebox.showinfo("Deleted", "Payment record deleted!")
    read_payments()


def clear_fields():
    entry_order_id.delete(0, tk.END)
    entry_payment_date.delete(0, tk.END)
    entry_payment_method.delete(0, tk.END)
    entry_payment_status.delete(0, tk.END)
    entry_payment_amount.delete(0, tk.END)


# GUI
root = tk.Tk()
root.title("Payment Management (MongoDB CRUD)")
root.geometry("950x550")

# Define a custom font for all fields
custom_font = ('Georgia', 10)

frame_entry = tk.Frame(root)
frame_entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Apply the custom font to all labels and entries
tk.Label(frame_entry, text="Order ID:", font=custom_font).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_order_id = tk.Entry(frame_entry, width=30, font=custom_font)
entry_order_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_entry, text="Payment Date (YYYY-MM-DD):", font=custom_font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_payment_date = tk.Entry(frame_entry, width=30, font=custom_font)
entry_payment_date.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_entry, text="Payment Method:", font=custom_font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_payment_method = tk.Entry(frame_entry, width=30, font=custom_font)
entry_payment_method.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_entry, text="Payment Status:", font=custom_font).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_payment_status = tk.Entry(frame_entry, width=30, font=custom_font)
entry_payment_status.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame_entry, text="Payment Amount:", font=custom_font).grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_payment_amount = tk.Entry(frame_entry, width=30, font=custom_font)
entry_payment_amount.grid(row=4, column=1, padx=10, pady=5)

button_height = 1
button_width = 18

frame_buttons = tk.Frame(root)
frame_buttons.grid(row=1, column=0, padx=10, pady=10, sticky="w")

tk.Button(frame_buttons, text="Insert", bg='blue', fg="white", command=insert_payment, width=button_width,
          height=button_height).grid(row=0, column=0, padx=10, pady=10)

tk.Button(frame_buttons, text="Read", bg='blue', fg="white", command=read_payments, width=button_width,
          height=button_height).grid(row=0, column=1, padx=10, pady=10)

tk.Button(frame_buttons, text="Update", bg='blue', fg="white", command=update_payment, width=button_width,
          height=button_height).grid(row=0, column=2, padx=10, pady=10)

tk.Button(frame_buttons, text="Delete", bg='blue', fg="white", command=delete_payment, width=button_width,
          height=button_height).grid(row=0, column=3, padx=10, pady=10)

# Data Display with a scrollbar
listbox = tk.Listbox(root, width=70, height=15, font=('Georgia', 10), selectmode=tk.SINGLE)
listbox.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

scrollbar = tk.Scrollbar(root, bg='blue', troughcolor='lightblue')
scrollbar.grid(row=2, column=4, sticky="ns")
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.state('zoomed')

read_payments()

root.mainloop()
