import connectdatabase
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel



# Function to create the dashboard GUI
def admin():

    root = tk.Tk()
    root.title("Dashboard")
    root.geometry("500x500")
    root.configure(bg="#2b2929")

    # Create a label to display the user's name
    user_label = tk.Label(root, text=f"Welcome, ADMIN!", font=("Norwester", 25), bg="#2b2929", fg="#919191")
    user_label.pack(pady=25)

    # Create a title label
    title_label = tk.Label(root, text="Equipeth", font=("Norwester", 100), bg="#2b2929")
    title_label.pack()

    # Create a label for the buttons
    button_label = tk.Label(root, text="Actions", font=("Norwester", 15), bg="#2b2929", fg="#919191")
    button_label.pack(pady=10)

    history_button = tk.Button(root, text="History", command=lambda: history(), bg="#2b2929", fg="#919191", font=("Norwester", 20))
    history_button.pack(pady=5)

    logout_button = tk.Button(root, text="inventory", command=lambda: inventory(), bg="#2b2929", fg="#919191", font=("Norwester", 20))
    logout_button.pack(pady=5)

    # Start the main event loop
    root.mainloop()




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
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry("1000x400")
        self.root.config(bg="#2b2929")  # Set background color
        
        # Define custom font
        title = tk.Label(root, text="Equipeth Inventory", font=("Norwester", 55, "bold"), fg="#d9d9d9", bg="#2b2929")
        title.pack(pady=10)

        self.create_widgets()
        
    def create_widgets(self):
        self.listbox_frame = tk.Frame(self.root, bg="#2b2929")  # Set background color
        self.listbox_frame.pack(fill="both", expand=True)



        self.listbox = tk.Listbox(self.listbox_frame, width=60, fg="#d9d9d9", bg="#2b2929")  # Apply custom font and colors
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        try:
            with connectdatabase.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM itemtbl")
                result = cursor.fetchall()
                for item in result:
                    self.listbox.insert(tk.END, item)
        except Exception as e:
            messagebox.showerror("Error", str(e))

        update_button = tk.Button(self.root, text="Update Item", command=self.update_item,  fg="#d9d9d9", bg="#2b2929")  # Apply custom font and colors
        update_button.pack(pady=10)

    def update_item(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            item_id = self.listbox.get(selected_item[0])
            item_window = tk.Toplevel(self.root)
            item_window.title("Update Item")
            item_window.config(bg="#2b2929")  # Set background color

            labels = ["Item Category:", "Item Class:", "Quantity:", "Item Description:", "Date Acquired:", "Remarks:"]
            entries = []

            for i, label_text in enumerate(labels):
                label = tk.Label(item_window, text=label_text,  fg="#d9d9d9", bg="#2b2929")  # Apply custom font and colors
                label.grid(row=i, column=0, padx=5, pady=5)
                entry = tk.Entry(item_window)
                entry.grid(row=i, column=1, padx=5, pady=5)
                entry.insert(0, item_id[i+1])  # Skip item ID
                entries.append(entry)

            update_button = tk.Button(item_window, text="Update", command=lambda: self.update(entries, item_id[0]),  fg="#d9d9d9", bg="#2b2929")  # Apply custom font and colors
            update_button.grid(row=len(labels), column=1, padx=5, pady=5)

    def update(self, entries, item_id):
        values = [entry.get() for entry in entries]
        try:
            with connectdatabase.connection.cursor() as cursor:
                query = "UPDATE itemtbl SET itemCategory = %s, itemClass = %s, Quantity = %s, itemDescription = %s, DateAcquired = %s, remarks = %s WHERE itemID = %s"
                cursor.execute(query, (*values, item_id))
                connectdatabase.connection.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Success", "Item updated successfully")

def inventory():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()









def history():
    # Make a GUI to display all the items in historytbl
    root = tk.Tk()
    root.title("History")
    root.geometry("1000x450")
    root.config(bg="#2b2929")  # Set background color

    # Define custom font
    title = tk.Label(root, text="Equipeth History", font=("Norwester", 55, "bold"), fg="#d9d9d9", bg="#2b2929")
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
            cursor.execute("SELECT * FROM historytbl")
            result = cursor.fetchall()

            # Insert the items into the listbox
            for item in result:
                listbox.insert(tk.END, item)
    except Exception as e:
        messagebox.showerror("Error", str(e))

    root.mainloop()
