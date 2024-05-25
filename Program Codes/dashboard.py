import connectdatabase
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
import borrow
import Catalouge


# Function to create the dashboard GUI
def dashboard(student_name, student_id, student_email):

    root = tk.Tk()
    root.title("Dashboard")
    root.geometry("500x500")
    root.configure(bg="#2b2929")

    # Create a label to display the user's name
    user_label = tk.Label(root, text=f"Welcome, {student_name}!", font=("Norwester", 25), bg="#2b2929", fg="#919191")
    user_label.pack(pady=25)

    # Create a title label
    title_label = tk.Label(root, text="Equipeth", font=("Norwester", 100), bg="#2b2929")
    title_label.pack()

    # Create a label for the buttons
    button_label = tk.Label(root, text="Actions", font=("Norwester", 15), bg="#2b2929", fg="#919191")
    button_label.pack(pady=10)

    # Create buttons
    borrow_button = tk.Button(root, text="Borrow", command=lambda: borrow.borrow(student_id), bg="#2b2929", fg="#919191", font=("Norwester", 20))
    borrow_button.pack(pady=5)

    reserve_button = tk.Button(root, text="Catalouge", command=lambda: Catalouge.inventory(), bg="#2b2929", fg="#919191", font=("Norwester", 20))
    reserve_button.pack(pady=5)

    history_button = tk.Button(root, text="History", command=lambda: history(student_id), bg="#2b2929", fg="#919191", font=("Norwester", 20))
    history_button.pack(pady=5)

    # Start the main event loop
    root.mainloop()



def history(student_id):
    # Make a GUI to display all the items in itemtbl
    root = tk.Tk()
    root.title("Student History")
    root.geometry("1000x450")
    root.config(bg="#2b2929")  # Set background color

    # Define custom font
    title = tk.Label(root, text="Equipeth History", font=("Norwester", 55, "bold"), fg="#d9d9d9", bg="#2b2929")
    title.pack(pady=10)


    # Create a listbox to display all the items
    listbox_frame = tk.Frame(root, bg="#2b2929")  # Set background color
    listbox_frame.pack(fill="both", expand=True)

    listbox = tk.Listbox(listbox_frame, width=60,fg="#d9d9d9", bg="#2b2929")  # Apply custom font and colors
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    # Fetch all the items from the database
    try:
        with connectdatabase.connection.cursor() as cursor:
            cursor.execute(
                "SELECT  historytbl.dateBorrowed, historytbl.status, itemtbl.itemID, itemtbl.itemDescription FROM historytbl INNER JOIN itemtbl ON historytbl.itemID = itemtbl.itemID WHERE historytbl.studentid = %s",
                (student_id,)
            )
            result = cursor.fetchall()
            if result:
                for row in result:
                    listbox.insert(tk.END, row)  # Insert each row into the listbox
            else:
                messagebox.showerror("Error", "No items found for this student")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    root.mainloop()

