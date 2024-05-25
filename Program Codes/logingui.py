import tkinter as tk
from tkinter import messagebox
import connectdatabase
import dashboard
import admin

def login():
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x350")
    root.configure(bg="#2b2929")

    title = tk.Label(root, text="Equipeth", font=("Norwester", 45, "bold"), fg="#d9d9d9", bg="#2b2929")
    title.pack(pady=10)

    studentidlabel = tk.Label(root, text="Student ID:", font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    studentidlabel.pack(pady=10)
    studentidentry = tk.Entry(root, font=("Norwester", 15), bg="#919191", fg="#2b2929")
    studentidentry.pack()

    studentpasswordlabel = tk.Label(root, text="Student Password:", font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    studentpasswordlabel.pack(pady=10)
    studentpasswordentry = tk.Entry(root, font=("Norwester", 15), bg="#919191", fg="#2b2929", show="*")
    studentpasswordentry.pack()



    
    def checklogin():
        if studentidentry.get() == "ADMIN" and studentpasswordentry.get() == "ADMIN":
            admin.admin()
        else:
            try:
                with connectdatabase.connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT studentname, studentid, studentemail FROM usertbl WHERE studentid = %s AND studentpassword = %s",
                        (studentidentry.get(), studentpasswordentry.get())
                    )
                    result = cursor.fetchone()

                    if result:
                        # Unpack the result tuple
                        studentname, studentid, studentemail = result
                        # Pass all three values to the dashboard function
                        dashboard.dashboard(studentname, studentid, studentemail)
                        root.destroy()

                    else:
                        messagebox.showerror("Error", "Sorry You don't exist")

            except Exception as e:
                # handle any exceptions here
                messagebox.showerror("Error sa login, checklogin()", str(e))

    loginbutton = tk.Button(root, text="Login", command=checklogin, font=("Norwester", 15), fg="#d9d9d9", bg="#2b2929")
    loginbutton.pack(pady=10)


