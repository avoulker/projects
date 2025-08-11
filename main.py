import tkinter as tk

root = tk.Tk()
root.title("User manager")

def add_btn_handler():
    name = name_entry.get().strip()
    age = age_entry.get().strip()

    if name and age:
        users_list.insert(tk.END, f"{name} ({age})")
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

def update_btn_handler():
    selected_index = users_list.curselection()
    if selected_index:
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        if name and age:
            users_list.delete(selected_index)
            users_list.insert(selected_index, f"{name} ({age})")
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)

def delete_btn_handler():
    selected_index = users_list.curselection()
    if selected_index:
        users_list.delete(selected_index)

def on_select(event):
    selected_index = users_list.curselection()
    if selected_index:
        user_text = users_list.get(selected_index)
        if "(" in user_text and user_text.endswith(")"):
            name = user_text[:user_text.rfind("(")].strip()
            age = user_text[user_text.rfind("(")+1:-1].strip()
            name_entry.delete(0, tk.END)
            name_entry.insert(0, name)
            age_entry.delete(0, tk.END)
            age_entry.insert(0, age)

# inputs:
tk.Label(root, text="name: ").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="age: ").grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=5, pady=5)

# buttons:
add_btn = tk.Button(root, text="add", width=10, command=add_btn_handler)
update_btn = tk.Button(root, text="update", width=10, command=update_btn_handler)
delete_btn = tk.Button(root, text="delete", width=10, command=delete_btn_handler)

add_btn.grid(row=2, column=0, padx=5, pady=5)
update_btn.grid(row=2, column=1, padx=5, pady=5)
delete_btn.grid(row=2, column=2, padx=5, pady=5)

# users list:
users_list = tk.Listbox(root, width=40)
users_list.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
users_list.bind("<<ListboxSelect>>", on_select)

root.mainloop()
