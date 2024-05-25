import tkinter as tk
from tkinter import messagebox
from datetime import date
import connectdatabase

def borrow(student_id):
    root = tk.Tk()
    root.title("Borrow")
    root.geometry("400x350")
    root.configure(bg="#2b2929")

    title = tk.Label(root, text="Equipeth", font=("Norwester", 45, "bold"), fg="#d9d9d9", bg="#2b2929")
    title.pack(pady=10)

    itemlabel = tk.Label(root, text="Item Id:", font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    itemlabel.pack(pady=10)
    itementry = tk.Entry(root, font=("Norwester", 15), bg="#919191", fg="#2b2929")
    itementry.pack()

    Submitbutton = tk.Button(root, text="Submit", command=lambda: checkitem(root, itementry, student_id), font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    Submitbutton.pack(pady=10)

    root.mainloop()

def checkitem(root, itementry, student_id):
    try:
        with connectdatabase.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM itemtbl WHERE itemID = %s",
                (itementry.get(),)
            )
            result = cursor.fetchone()
            if result:
                # Unpack the result tuple
                x = result
                submit_item(x, student_id)
                # Destroy the login window after successful login
                root.destroy()
            else:
                messagebox.showerror("Error", "Item does not exist")
    except Exception as e:
        # Handle any exceptions here
        messagebox.showerror("Error", str(e))


def submit_item(x, student_id):
    try:
        with connectdatabase.connection.cursor() as cursor:
            # Extracting itemID from the tuple
            item_id = x[0]  # Assuming itemID is the first element of the tuple x
            # Inserting into historytbl
            cursor.execute(
                "INSERT INTO historytbl (studentid, itemID, dateBorrowed, status) VALUES (%s, %s, %s, %s)",
                (student_id, item_id, date.today(), "borrowed")
            )
        connectdatabase.connection.commit()
    except Exception as e:
        # Handle any exceptions here
        messagebox.showerror("Error", str(e))
