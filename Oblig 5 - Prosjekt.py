# ===Obligatory Assignment 5===

import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import json
from Functions import *
content = "" # Global variable for Open function

# Defining main functions

def open_file():
    list_file = open ("list_complete.json", "r") # Open the list file, read only
    arg = list_file.read()
    list_file.close()
    view_list.insert(END, arg)

def save_file():
    list_complete = display_list.get(0, END) # Getting list data. From index 0 to end.
    with open("list_complete.json", "w") as json_file: # Writing list data to json-file
            json.dump(list_complete, json_file, ensure_ascii=False) # dumping list, NOR Alphabet allowed
    tkinter.messagebox.showwarning(title=Warning, message="Data saved to list_complete.json!")


def add():
    qty_items = (qty_slider.get())  # getting number value from slider widget
    display_list.insert(tkinter.END, qty_items)  # inserting slider value in Listbox
    list_item = (user_input.get())  # getting user's input from Entry
    display_list.insert(tkinter.END, list_item)  # inserting user's input in Listbox
    user_input.delete(0, tkinter.END)
    if list_item == "Enter item here :" or list_item == "":  # Handling user input
        tkinter.messagebox.showwarning(title=Warning, message="Please enter a valid item!")
    else:
        tkinter.messagebox.showwarning(title=Warning, message="Item added!")


def delete():
    selected_item = display_list.curselection() # getting selected item from Listbox
    for index in selected_item[::-1]:
        display_list.delete(index)
    display_list.delete(ACTIVE) # deleting selected items from Listbox
    tkinter.messagebox.showwarning(title=Warning, message="Item deleted!") # Feedback dialogue box if item deleted


def clear_list():
    display_list.delete(0, END) # Deleting all list entries in Listbox
    tkinter.messagebox.showwarning(title=Warning, message="List cleared!")


# Creating GUI

root = Tk()
root.geometry("1200x600") # Setting window size in px.
root.title("PROJECT SHOPPING LIST 2020") # Setting window title
root.iconbitmap("ico/program_logo.ico") # Setting window title icon
title_label = Label(root, text="PROJECT  SHOPPING  LIST  2020", pady=5, font=("arial black", 15)) # Setting heading title
title_label.grid(row=0, column=0) # Placing heading title


# Listbox Widget, displays items and quantity of items.

display_list = Listbox(root, width=60, selectmode=MULTIPLE, font=("arial", 14)) # Able to select multiple items at once.
display_list.grid(row=4, column=0, pady=10, padx=40)


# Creating main control buttons

add_icon = PhotoImage(file="ico/add.png") # Giving button an icon
add_button = Button(root, text="Add list item", command=add, bg="green") # Giving button text and color
add_button.config(image=add_icon, compound=LEFT) # placing icon on button
add_button.grid(row=3, column=2) # placing button in root

del_icon = PhotoImage(file="ico/del.png")
del_button = Button(root, text="Delete list item(s)", bg="red", command=delete)
del_button.config(image=del_icon, compound=LEFT)
del_button.grid(row=3, column=3, padx=20)

save_icon = PhotoImage(file="ico/save.png")
save_button = Button(root, text="Save list")
save_button.config(image=save_icon, compound=LEFT, command=save_file)
save_button.grid(row=4, column=1)

open_icon = PhotoImage(file="ico/open.png")
open_button = Button(root, text="Open list", command=open_file)
open_button.config(image=open_icon, compound=LEFT)
open_button.grid(row=4, column=2)

clear_icon = PhotoImage(file="ico/clear.png")
clear_button = Button(root, text="Clear list", command=clear_list)
clear_button.config(image=clear_icon, compound=LEFT)
clear_button.grid(row=4, column=3)

# Creating entry field for user input

user_input = Entry(root, width=40) # Placing Entry in root, given width of 40 characters
user_input.grid(row=1, column=0) # Specifying placement in root
user_input.insert(0, "Enter item here :") # Pre set entry with instruction
user_input.focus() # Blinking "|"

# Creating horizontal scale widget, values ranging from 1-10.

qty_slider = Scale(root, from_=1, to=10, orient=HORIZONTAL)
qty_slider.grid(row=3, column=1)

# Creating textbox for reading file

view_list = Text(root)
view_list.grid(row=6, column=0)

root.mainloop()
