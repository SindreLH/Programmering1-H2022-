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