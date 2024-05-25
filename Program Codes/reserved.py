import tkinter as tk

# Define global variables
root = None
table_frame = None

def reservegui(student_id):
    global root, table_frame
    root = tk.Tk()
    root.title("Borrow Entries")
    table_frame = tk.Frame(root)
    table_frame.pack(fill="both", expand=True)

    student_id = student_id

    # Create labels in the first row
    labels = [
        "Inventory ID",
        "JRU Code",
        "Category",
        "Class",
        "Item Description",
        "Date Acquired",
        "Location",
        "Remark"
    ]
    for j, label_text in enumerate(labels):
        label = tk.Label(table_frame, text=label_text, padx=10, pady=5, borderwidth=1, relief="solid")
        label.grid(row=0, column=j)

    # Create entry widgets for each column except the first row
    for i in range(4):
        for j in range(8):
            entry = tk.Entry(table_frame, width=15)
            entry.grid(row=i+1, column=j, padx=10, pady=5)

    # Create a submit button
    submit_button = tk.Button(table_frame, text="Submit", command=lambda: submit_borrow_entries(table_frame, root))
    submit_button.grid(row=5, column=0, columnspan=8, pady=5)

def submit_borrow_entries(table_frame, root):
    for i in range(4):
        for j in range(8):
            entry = table_frame.grid_slaves(row=i+1, column=j)[0]
            print(entry.get())
    root.destroy()
