import pandas as pd
import tkinter as tk
from tkinter import messagebox
import connectdatabase


def inventory():
    # Make a GUI to display all the items in itemtbl
    root = tk.Tk()
    root.title("Inventory")
    root.geometry("500x400")
    root.config(bg="#2b2929")  # Set background color

        # Define custom font
    title = tk.Label(root, text="Equipeth Inventory", font=("Norwester", 55, "bold"), fg="#d9d9d9", bg="#2b2929")
    title.pack(pady=10)

    # Create a listbox to display all the items
    listbox_frame = tk.Frame(root, bg="#2b2929")  # Set background color
    listbox_frame.pack(fill="both", expand=True)

    listbox = tk.Listbox(listbox_frame, width=60, fg="#d9d9d9", bg="#2b2929")  # Apply custom font and colors
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    # Fetch all the items from the database
    try:
        with connectdatabase.connection.cursor() as cursor:
            cursor.execute("SELECT itemID, Quantity, ItemDescription, availability FROM itemtbl")
            result = cursor.fetchall()

            # Insert the items into the listbox
            for item in result:
                listbox.insert(tk.END, item)
    except Exception as e:
        messagebox.showerror("Error", str(e))

    root.mainloop()

