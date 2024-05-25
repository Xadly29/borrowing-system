import tkinter as tk
from tkinter import messagebox
import connectdatabase

def createregistergui():
    root = tk.Tk()
    root.title("Register")
    root.geometry("400x500")
    root.configure(bg="#2b2929")

    title = tk.Label(root, text="Equipeth", font=("Norwester", 45, "bold"), fg="#d9d9d9", bg="#2b2929")
    title.pack(pady=10)

    studentidlabel = tk.Label(root, text="Student ID:", font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    studentidlabel.pack(pady=10)
    studentidentry = tk.Entry(root, font=("Norwester", 15), bg="#919191", fg="#2b2929")
    studentidentry.pack()

    studentnamelabel = tk.Label(root, text="Student Name:", font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    studentnamelabel.pack(pady=10)
    studentnameentry = tk.Entry(root, font=("Norwester", 15), bg="#919191", fg="#2b2929")
    studentnameentry.pack()

    studentemaillabel = tk.Label(root, text="Student Email:", font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    studentemaillabel.pack(pady=10)
    studentemailentry = tk.Entry(root, font=("Norwester", 15), bg="#919191", fg="#2b2929")
    studentemailentry.pack()

    studentpasswordlabel = tk.Label(root, text="Student Password:", font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    studentpasswordlabel.pack(pady=10)
    studentpasswordentry = tk.Entry(root, font=("Norwester", 15), bg="#919191", fg="#2b2929", show="*")
    studentpasswordentry.pack()

    def register():
        studentid = studentidentry.get()
        studentname = studentnameentry.get()
        studentemail = studentemailentry.get()
        studentpassword = studentpasswordentry.get() # can't hash this because theres no way to unhash it for the login
         

        if not studentid.isdigit():
            messagebox.showerror("Error", "Please enter a valid student ID")
        elif not studentid or not studentname or not studentemail or not studentpassword:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        else:
            try:
                 with connectdatabase.connection.cursor() as cursor:
                     query = "SELECT * FROM usertbl WHERE studentid = %s and studentemail = %s"
                     cursor.execute(query, (studentid,studentemail))
                     result = cursor.fetchone()

                     if studentid == result:
                         messagebox.showerror("Error", "This account already exists")
                         return

                 with connectdatabase.connection.cursor() as cursor:
                     query = "INSERT INTO usertbl (studentid, studentname, studentemail, studentpassword) VALUES (%s, %s, %s, %s)"
                     cursor.execute(query, (studentid, studentname, studentemail, studentpassword))

                 connectdatabase.connection.commit()

                 messagebox.showinfo("Success", "User registered successfully")

            except Exception as e:
                messagebox.showerror("Error in register()", str(e))


    buttonframe = tk.Frame(root, bg="#2b2929")
    buttonframe.pack(pady=10)

    registerbutton = tk.Button(buttonframe, text="Register", command=register, font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    registerbutton.pack(side=tk.LEFT, padx=5)

    backbutton = tk.Button(buttonframe, text="Back", command=root.destroy, font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    backbutton.pack(side=tk.LEFT, padx=5)
    buttonframe.pack(anchor=tk.CENTER)



    root.mainloop()


