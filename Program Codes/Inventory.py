import pandas as pd
import tkinter as tk
from tkinter import messagebox
import connectdatabase
import dashboard

"""path = "D:/Downloads/eport/Summary 2 - Summary 2.csv"
summary = pd.read_csv(path)

for index, row in summary.iterrows():
    itemID = row['no']
    itemCategory = row['CATEGORY']
    itemClass = row['CLASS']
    Quantity = row['QTY']
    itemDescription = row['ITEM DESCRIPTION']
    DateAcquired = row['DATE ACQUIRED']
    remarks = row['REMARKS']
    with connectdatabase.connection.cursor() as cursor:
                    query = "INSERT INTO itemtbl (itemID, itemCategory, itemClass, Quantity, itemDescription, DateAcquired, remarks, availability) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, (itemID, itemCategory, itemClass, Quantity, itemDescription, DateAcquired, remarks, 'Available'))
    connectdatabase.connection.commit()
print("Done")

""" 

def inventory():
    
    #Make a GUI to display all the items in itemtbl
    root = tk.Tk()
    root.title("All Items")
    root.geometry("500x400")

    # Create a listbox to display all the items
    listbox_frame = tk.Frame(root)
    listbox_frame.pack(fill="both", expand=True)

    listbox = tk.Listbox(listbox_frame, width=60)
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    # Fetch all the items from the database
    try:
        with connectdatabase.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM itemtbl")
            result = cursor.fetchall()

            # Insert the items into the listbox
            for item in result:
                listbox.insert(tk.END, item)
    except Exception as e:
        messagebox.showerror("Error", str(e))

    root.mainloop()

def history():
    
    #Make a GUI to display all the items in itemtbl
    root = tk.Tk()
    root.title("All Items")
    root.geometry("500x400")

    # Create a listbox to display all the items
    listbox_frame = tk.Frame(root)
    listbox_frame.pack(fill="both", expand=True)

    listbox = tk.Listbox(listbox_frame, width=60)
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    # Fetch all the items from the database
    try:
        with connectdatabase.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM historytbl")
            result = cursor.fetchall()

            # Insert the items into the listbox
            for item in result:
                listbox.insert(tk.END, item)
    except Exception as e:
        messagebox.showerror("Error", str(e))

    root.mainloop()