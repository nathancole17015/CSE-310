import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

def GenerateKey(): 
    return Fernet.generate_key()

def EncryptPassword(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def DecryptPassword(key, encryptedPassword):
    f = Fernet(key)
    return f.decrypt(encryptedPassword.encode()).decode()

passwords = {}

def AddPassword():
    service = serviceEntry.get()
    username = usernameEntry.get()
    password = passwordEntry.get()

    if service and username and password:
        encryptedPassword = EncryptPassword(key, password)
        passwords[service] = {"username": username, "password": encryptedPassword}
        messagebox.showinfo("Success", "Password added successfully!")
    else: 
        messagebox.showwarning("Error", "Please fill in all the fields")

def GetPassword():
    service = serviceEntry.get()
    if service in passwords:
        encryptedPassword = passwords[service]["password"]
        decryptedPassword = DecryptPassword(key, encryptedPassword)
        messagebox.showinfo ("Password",f"Username: {passwords[service]["username"]}\nPassword: {decryptedPassword}")
    else:
        messagebox.showwarning("Error", " Password not found")
    
key = GenerateKey()

HowTo = 'To add password fill out and press "Add Password" to see password, enter Account Name and press "Get Password'

window = tk.Tk()
window.title("Password Manager")
window.configure(bg="red")

window.resizable(False,False)

centerFrame = tk.Frame(window,bg="#d3d3d3")
centerFrame.grid(row = 0, column = 1, padx = 10, pady = 10)

HowToLabel = tk.Label(centerFrame, text= HowTo, bg = "#d3d3d3")
HowToLabel.grid(row = 0, column = 1, padx = 10, pady = 5)

serviceLabel = tk.Label(centerFrame, text = "Account:", bg = "#d3d3d3")
serviceLabel.grid(row=1, column=0, padx=10, pady=5)
serviceEntry = tk.Entry(centerFrame)
serviceEntry.grid(row=1 ,column=1, padx = 10, pady = 5)

usernameLabel = tk.Label(centerFrame, text= "Username:", bg="#d3d3d3")
usernameLabel.grid(row=2, column=0, padx=10, pady=5)
usernameEntry = tk.Entry(centerFrame)
usernameEntry.grid(row=2, column=1, padx=10, pady=5)

passwordLabel = tk.Label(centerFrame, text= "Password:", bg="#d3d3d3")
passwordLabel.grid(row=3, column=0, padx=10, pady=5)
passwordEntry = tk.Entry(centerFrame, show="*")
passwordEntry.grid(row=3, column=1, padx=10, pady=5)

addButton = tk.Button(centerFrame, text="Add Password", command= AddPassword, height=1,width=10)
addButton.grid(row=5, column=4, padx=10, pady=5)

getButton = tk.Button(centerFrame, text= "Get Password", command=GetPassword, height=1,width=10)
getButton.grid(row=6, column=4, padx=10, pady=5)

window.mainloop()
