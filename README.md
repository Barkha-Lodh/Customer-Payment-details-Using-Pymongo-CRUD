# Customer-Payment-details-Using-Pymongo-CRUD

Payment Management App 463 (MongoDB CRUD) 💳💻
This Python application allows users to manage payment records using a Graphical User Interface (GUI) with Tkinter and perform CRUD (Create, Read, Update, Delete) operations using MongoDB as the backend database.

🖼️ Screenshots
<img width="1917" height="769" alt="image" src="https://github.com/user-attachments/assets/7d05687e-a90f-454e-8270-77ba25e93464" />

🚀 Features
1.Insert 📝: Add Customer Payment Details: Allows users to input customer payment details like Order ID, Payment Date, Payment Method, Payment Status, and Payment Amount.

2.Read 👀: View Customer Payment Details: Displays all customer payments stored in the MongoDB database in a Listbox.

3.Update 🔄: Update Payment Details: Users can select an existing payment record from the Listbox and update the payment details.

4.Delete ❌: Delete Payment Details: Allows users to delete a selected payment record from the database.

Dependencies 📦:
Tkinter 📱: For building the GUI.
pymongo 📡: For connecting and interacting with MongoDB.

#How It Works 🔧:
Insert Payment 📝:
The user can input payment details (Order ID, Payment Date, Method, Status, Amount) into the entry fields.
Once the user clicks the Insert button, the data is inserted into the MongoDB database and displayed in the Treeview.

2.Read Payments 👀:
Clicking the Read Payments button will refresh the data in the Treeview, showing the most recent payment records.

3.Update Payment 🔄:
To update a payment, the user selects a record from the Treeview, modifies the input fields, and clicks the Update button to save the changes.

4.Delete Payment ❌:
To delete a payment, the user selects a record from the Treeview and clicks the Delete button. The record is removed from MongoDB, and the Treeview is refreshed.

🗂️ Project Structure
Customer-Payment-Details-Using-Pymongo-CRUD/
│
├── main.py                  
├── README.md               
├── requirements.txt         
└── .gitignore  


