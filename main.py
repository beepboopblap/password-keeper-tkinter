from tkinter import *
from datetime import datetime
import tkinter as tk
import os
import pickle as pickle
import stdiomask


global password_list



def main():



    def dump():

        global login
        global passwords

        login = pickle.load(open("login.txt", "rb")) 
        passwords = pickle.load(open("passwords.txt", "rb"))


    def exit_app():

        window.destroy()

    
    def create_pass():

 
        title = input("Enter Title following by the password: ")
        password = stdiomask.getpass("Enter password for the title: ")
        
        final_pass = title, ":", password
        
        pickle.dump(final_pass, open("passwords.txt", "ab"))


        print("Password added for:", title)

        
    def del_pass():

        passwords = []

        with (open("passwords.txt", "rb")) as openfile:
            while True:
                try:
                    passwords.append(pickle.load(openfile))
                except EOFError:
                    break


        user_inp = input("Enter the number to delete: ")

        passwords = [x for x in passwords if x[1] != user_inp]
        
    
        pickle.dump(passwords, open("passwords.txt", "ab"))
        print(f"Password and Title for number {user_inp} has been deleted")



    def view_pass():

        global passwords

        passwords = []

        with (open("passwords.txt", "rb")) as openfile:
            while True:
                try:
                    passwords.append(pickle.load(openfile))
                except EOFError:
                    break
        
        for i in passwords:
            i = str(i)
            i = i.replace("(", "")
            i = i.replace(")", "")
            i = i.replace(",", "")
            i = i.replace("'", "")
            print(i,"\n")


    def home_screen():

        window.withdraw()
        window1.withdraw()

        window3 = Toplevel(window)
        window3.title("Home")
        window3.geometry("500x500")
        window3.resizable(0,0)

        
        home_label = tk.Label(window3, text="Password Keeper", font=("Calibri", 31)) 
        home_label.grid(padx=(80,0), pady=(0,0))
        button = tk.Button(window3, text="Add", command=create_pass)
        button.grid(padx=(80,0), pady=(120,0))
        button1 = tk.Button(window3, text="Delete", command=del_pass)
        button1.grid(padx=(80,0), pady=(20,0))
        button2 = tk.Button(window3, text="View", command=view_pass)
        button2.grid(padx=(80,0), pady=(20,0))
        button3 = tk.Button(window3, text="Exit", command=exit_app, bg="red")
        button3.grid(padx=(320,0), pady=(140,0))


    def registration_confirmer():
        
        user_confirmation = entry1.get()
        entry1.delete(0, END)

        if user_password == user_confirmation:
            login = pickle.dump(user_confirmation, open("login.txt", "wb"))
            home_screen()

        else:
            print("Invalid")

    
    def login_confirmer():

        login = pickle.load(open("login.txt", "rb"))
        user_password = entry2.get()
        entry2.delete(0, END)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if user_password == login:
            print("Logged in at:", current_time, "\n")
            home_screen()

        else:
            print("Invalid")

        
    def register_screen():

        global entry
        global window1
        
        window1 = Toplevel(window)
        window1.title("Register")
        window1.geometry("500x500")
        window1.resizable(0,0)

        label = tk.Label(window1, text="Create a Password", font=("Calibri", 31))
        label.grid(padx=(80,0), pady=(0,0))
        entry = tk.Entry(window1, width=40, show="*")
        entry.focus_set()
        entry.grid(padx=(100,0), pady=(100,0))
        button = tk.Button(window1, text="Create", command=create_password_screen)
        button.grid(padx=(100,0), pady=(100,0))



    def login_screen():

        global entry2
        global window1
 
        window1 = Toplevel(window)
        window1.title("Register")
        window1.geometry("500x500")
        window1.resizable(0,0)

        label = tk.Label(window1, text="Enter Your Password", font=("Calibri", 31))
        label.grid(padx=(40,0), pady=(0,0))
        entry2 = tk.Entry(window1, width=40, show="*")
        entry2.focus_set()
        entry2.grid(padx=(100,0), pady=(200,0))
        button = tk.Button(window1, text="Login", command=login_confirmer)
        button.grid(padx=(100,0), pady=(100,0))



    def create_password_screen():

        global user_password

        user_password = entry.get()
        entry.delete(0, END)
        length = len(user_password)

        if length < 8:
            print("Password must be at least 8 characters long")

        else:
            confirm_password_screen()

    def confirm_password_screen():

        global entry1
        global window1

        window1.destroy()
        window1 = Toplevel(window)
        window1.title("Confirm Password")
        window1.geometry("500x500")
        window1.resizable(0,0)

        label = tk.Label(window1, text="Confirm Password", font=("Calibri", 31))
        label.grid(padx=(80,0), pady=(0,0))
        entry1 = tk.Entry(window1, width=40, show="*")
        entry1.focus_set()
        entry1.grid(padx=(100,0), pady=(100,0))
        button = tk.Button(window1, text="Confirm", command=registration_confirmer)
        button.grid(padx=(100,0), pady=(100,0))



    window = tk.Tk()
    window.geometry("500x500")
    window.resizable(0,0)
    
    if os.stat("login.txt").st_size == 0:
        label = tk.Label(window, text="Register", font=("Calibri", 40))
        label.grid(padx=(138,0), pady=(0,0))
        button = tk.Button(window, text="Register", command=register_screen)
        button.grid(padx=(138,0), pady=(100,0))



    else:
        label = tk.Label(window, text="Login", font=("Calibri", 40))
        label.grid(padx=(138,0), pady=(0,0))
        button = tk.Button(window, text="Login", command=login_screen)
        button.grid(padx=(138,0), pady=(100,0))


    window.mainloop()


    

if __name__ == '__main__':
    main()
