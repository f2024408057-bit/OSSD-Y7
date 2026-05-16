import tkinter as tk
from tkinter import messagebox

def read_file():
    users = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    user, pwd = line.split(",")
                    users[user] = pwd
    except FileNotFoundError:
        pass
    return users

def write_file(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

def login():
    login_win = tk.Toplevel(root)
    login_win.title("Login")
    login_win.geometry("250x150")

    tk.Label(login_win, text="Username").pack()
    user_entry = tk.Entry(login_win)
    user_entry.pack()

    tk.Label(login_win, text="Password").pack()
    pass_entry = tk.Entry(login_win, show="*")
    pass_entry.pack()

    def check_login():
        username = user_entry.get()
        password = pass_entry.get()
        users = read_file()
        if username in users and users[username] == password:
            tk.messagebox.showinfo("Success", "Login successful!")
            login_win.destroy()
        else:
            tk.messagebox.showerror("Error", "Invalid username or password")

    tk.Button(login_win, text="Login", command=check_login).pack(pady=10)


def signup():
    signup_win = tk.Toplevel(root)
    signup_win.title("Signup")
    signup_win.geometry("250x150")

    tk.Label(signup_win, text="Username").pack()
    user_entry = tk.Entry(signup_win)
    user_entry.pack()

    tk.Label(signup_win, text="Password").pack()
    pass_entry = tk.Entry(signup_win, show="*")
    pass_entry.pack()

    def save_user():
        username = user_entry.get()
        password = pass_entry.get()
        if username == "" or password == "":
            tk.messagebox.showerror("Error", "Fields cannot be empty")
            return
        users = read_file()
        if username in users:
            tk.messagebox.showerror("Error", "Username already exists")
        else:
            write_file(username, password)
            tk.messagebox.showinfo("Success", "Signup successful!")
            signup_win.destroy()

    tk.Button(signup_win, text="Register", command=save_user).pack(pady=10)


def main():
    tk.Label(root, text="Welcome", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Login", command=login, width=15).pack(pady=5)
    tk.Button(root, text="Signup", command=signup, width=15).pack(pady=5)


root = tk.Tk()
root.title("Login System")
root.geometry("300x200")
main()
root.mainloop()