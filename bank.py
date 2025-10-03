#craeting a bank with deposit and withdraw and exit not finished right now 

# def show_balance():
#     pass

# def deposit():
#     pass

# def withdraw():
#     pass

# balance = 0
# is_running = True

# while is_running : 
#     print("bankking program")
#     print("1.show balance")
#     print("2.deposit")
#     print("3.withdraw")
#     print("4.Exit")

#     choice = input("enter your choice (1-4): ")
#     if choice == '1':
#         show_balance()
#     elif choice == '2':
#         deposit()
#     elif choice == '3':
#         withdraw()
#     elif choice == '4':
#         is_running = 'false'
#     else:
#         print("Thank you! have a nice day !")
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()