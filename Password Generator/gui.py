#Password Generator (GUI) by Sankalp Mishra!!

import tkinter as tk
from tkinter import messagebox
import random
import string

def make_password():
    try:
        size = int(length_entry.get())
        if size < 4:
            messagebox.showwarning("Oops!", "Pick at least 4 characters!")
            return

        chars = ""
        if var_upper.get():
            chars += string.ascii_uppercase
        if var_lower.get():
            chars += string.ascii_lowercase
        if var_digits.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("Oops!", "Pick at least one character type!")
            return

        result = "".join(random.choice(chars) for _ in range(size))
        password_label.config(text=result)
    except Exception:
        messagebox.showerror("Error", "Please type a number for length.")

root = tk.Tk()
root.title("🔑 Fun Password Maker")

tk.Label(root, text="How long should your password be?").pack()
length_entry = tk.Entry(root)
length_entry.pack()

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include UPPERCASE", variable=var_upper).pack(anchor='w')
tk.Checkbutton(root, text="Include lowercase", variable=var_lower).pack(anchor='w')
tk.Checkbutton(root, text="Include numbers", variable=var_digits).pack(anchor='w')
tk.Checkbutton(root, text="Include symbols", variable=var_symbols).pack(anchor='w')

tk.Button(root, text="Make me a password!", command=make_password).pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()