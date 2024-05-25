import tkinter as tk
from tkinter import messagebox
import registergui
import logingui

# Create the main window
root = tk.Tk()
root.title("Equipeth")
root.geometry("500x450")
root.configure(bg="#2b2929")

# Create a title label
title = tk.Label(root, text="Equipeth", font=("Norwester", 85, "bold"), fg="#d9d9d9", bg="#2b2929")
title.pack(pady=10)

# Create a button for login
loginbutton = tk.Button(root, text="Login", font=("Norwester", 35), fg="#d9d9d9", bg="#2b2929", command=logingui.login)
loginbutton.pack(pady=10)

# Create a button for register
registerbutton = tk.Button(root, text="Register", command=registergui.createregistergui, font=("Norwester", 35), fg="#d9d9d9", bg="#2b2929")
registerbutton.pack(pady=10)
# Start the main event loop
root.mainloop()

