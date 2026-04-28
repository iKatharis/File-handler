from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
import customtkinter
import json
from pynput import keyboard


def text(name, row, column):
    customtkinter.CTkLabel(root, text = name).grid(column=column, row=row)

def file_chose_file():
    global target_des
    target_des = filedialog.askdirectory(title="Where go")
    print(target_des)
    save_var(target_des)

def chose_file():
    global file_des
    file_des = filedialog.askopenfilename(title='ho')
    print(file_des)

def move_file():
    if file_des == '' or target_des == '':
        messagebox.showerror("Error", "No paths have been found")
    else:
        shutil.move(file_des, target_des)

def update_labels():
    text(target_des, 2, 2)
    text(file_des, 3, 2)
    root.after(100, update_labels)

def save_var(variable):
    with open ('dir.json', 'w') as f:
        json.dump(variable, f, indent=4)

def open_dir():
    try:
        with open ('dir.json', 'r') as f:
            new = json.load(f)
            return new
    except FileNotFoundError:
        return("Nothing")

####WHAT I DID TODAY


##WHAT I DID TODAY








file_des = ''
target_des = open_dir()


customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title('File Manager')
root.geometry('400x1000')
text('File Handler', 1, 1)

##BUTTON BASE
target_file = customtkinter.CTkButton(root, text="File destination", command=file_chose_file)
filechoose_button = customtkinter.CTkButton(root, text='File Choose', command=chose_file)
confirm_button = customtkinter.CTkButton(root, text='Move', command=move_file)

##PUTTING BUTTONS ON SCREEN
target_file.grid(column=1,row=2, pady=50,)
filechoose_button.grid(column=1, row=3, pady=50)
confirm_button.grid(column=1, row=4, pady=20)
update_labels()
root.mainloop()