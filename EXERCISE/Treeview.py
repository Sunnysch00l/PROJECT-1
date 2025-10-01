from tkinter import ttk
treeview = ttk.Treeview(master=None)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Treeview")
root.geometry("500x300")

treeview = ttk.Treeview()

treeview.pack(padx=10,pady=10, expand=True, fill=tk.BOTH)

root.mainloop()
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")
root.title("Tkinter Treeview")

treeview = ttk.Treeview()
level1 = treeview.insert("", tk.END, text="San Jose")

treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
root.mainloop()
level1 = treeview.insert("", tk.END, text="San Jose")
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")
root.title("Tkinter Treeview")

treeview = ttk.Treeview()
level1 = treeview.insert("", tk.END, text="San Jose")
treeview.insert(level1, tk.END, text="John Doe")
treeview.insert(level1, tk.END, text="Jane Doe")

treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
root.mainloop()
level1 = treeview.insert("", tk.END, text="San Jose")
treeview.insert(level1, tk.END, text="John Doe")
treeview.insert(level1, tk.END, text="Jane Doe")

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Tkinter Treeview")

treeview = ttk.Treeview(columns=("Salary","Bonus"))

treeview.heading("#0", text="Employee")
treeview.heading("Salary", text="Salary")
treeview.heading("Bonus", text="Bonus")

level1 = treeview.insert('', tk.END, text="San Jose")


treeview.insert(level1, tk.END, text="John Doe", values=(f"${100000: ,}",f"${8000: ,}"))
treeview.insert(level1, tk.END, text="Jane Doe", values=(f"${120000: ,}",f"${9000: ,}"))

treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
treeview = ttk.Treeview(columns=("Salary","Bonus"))
treeview.heading("#0", text="Employee")
treeview.heading("Salary", text="Salary")
treeview.heading("Bonus", text="Bonus")
level1 = treeview.insert('', tk.END, text="San Jose")
treeview.insert(level1, tk.END, text="John Doe", values=(f"${100000: ,}", f"${8000: ,}"))
treeview.insert(level1, tk.END, text="Jane Doe", values=(f"${120000: ,}", f"${9000: ,}"))
icon = tk.PhotoImage(file='icon.png')
treeview.insert(..., image=icon)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Tkinter Treeview")

treeview = ttk.Treeview(columns=( "Salary","Bonus"))

treeview.heading("#0", text="Employee")
treeview.heading("Salary", text="Salary")
treeview.heading("Bonus", text="Bonus")


icon_city = tk.PhotoImage(file="./assets/city.png")
icon_male = tk.PhotoImage(file="./assets/male.png")
icon_female= tk.PhotoImage(file="./assets/female.png")

level1 = treeview.insert('', tk.END, text="San Jose", image=icon_city)
treeview.insert(level1, tk.END, text="John Doe", values=(f"${100000: ,}",f"${8000: ,}"), image=icon_male)
treeview.insert(level1, tk.END, text="Jane Doe", values=(f"${120000: ,}",f"${9000: ,}"), image=icon_female)

treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
icon_city = tk.PhotoImage(file="./assets/city.png")
icon_male = tk.PhotoImage(file="./assets/male.png")
icon_female= tk.PhotoImage(file="./assets/female.png")
level1 = treeview.insert('', tk.END, text="San Jose", image=icon_city)
treeview.insert(level1, tk.END, text="John Doe", values=(f"${100000: ,}",f"${8000: ,}"), image=icon_male)
treeview.insert(level1, tk.END, text="Jane Doe", values=(f"${120000: ,}",f"${9000: ,}"), image=icon_female)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Treeview")

frame = ttk.Frame(root)

# create a treeview widget
treeview = ttk.Treeview(frame, columns=( "Salary","Bonus"))

treeview.heading("#0", text="Employee")
treeview.heading("Salary", text="Salary")
treeview.heading("Bonus", text="Bonus")


icon_city = tk.PhotoImage(file="./assets/city.png")
level1 = treeview.insert('', tk.END, text="San Jose", image=icon_city)


icon_male = tk.PhotoImage(file="./assets/male.png")
icon_female= tk.PhotoImage(file="./assets/female.png")


treeview.insert(level1, tk.END, text="John Doe", values=(f"${100000: ,}",f"${8000: ,}"), image=icon_male)
treeview.insert(level1, tk.END, text="Jane Doe", values=(f"${120000: ,}",f"${9000: ,}"), image=icon_female)

# create a vertical scrollbar
v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=v_scrollbar.set)

# pack the treeview and scrollbar
treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# package the frame
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


root.mainloop()
v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=v_scrollbar.set)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
import tkinter as tk
from tkinter import ttk
import csv


def read_csv(filename):
    rows = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)  
        for row in reader:
            rows.append(row) 

    return rows

def prepare_tree_data(rows, icon_male, icon_female):
    grouped_data = {}
    for row in rows:
        if row['Gender'] == 'Male':
            row['Icon']= icon_male
        else:
            row['Icon']= icon_female

        city = row['City']  # Assuming city is in the 5th column
        if city not in grouped_data:
            grouped_data[city] = []
        grouped_data[city].append(row)
    return grouped_data


def format_currency(value):
    try:
        return f"${int(value):,}"
    except ValueError:
        return value 


def create_tree_view(root, employees, icons):

    frame = ttk.Frame(root)

    treeview = ttk.Treeview(frame, columns=( "Salary","Bonus"))

    treeview.heading("#0", text="Employee")
    treeview.heading("Salary", text="Salary")
    treeview.heading("Bonus", text="Bonus")

        
    employee_data = prepare_tree_data(employees, icons['female'], icons['male'])

    for city in employee_data.keys():
        # add city
        city_id = treeview.insert('', tk.END, text=city, image=icons['city'])

        # add employees in the city
        for employee in employee_data[city]:
            treeview.insert(
                city_id, 
                tk.END, 
                text=employee['First Name'] + ' ' + employee['Last Name'], 
                values=(format_currency(employee['Salary']), format_currency(employee['Bonus'])), 
                image=employee['Icon']
            )
    # create a vertical scrollbar
    v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscrollcommand=v_scrollbar.set)

    # pack the treeview and scrollbar
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # package the frame
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    

def main():
    root = tk.Tk()
    root.title("Employee List")

    icons = {
        'city': tk.PhotoImage(file="./assets/city.png"),
        'male': tk.PhotoImage(file="./assets/male.png"),
        'female': tk.PhotoImage(file="./assets/female.png"),
        
    }

    employees = read_csv('employees.csv')
    create_tree_view(root, employees, icons)    
                
    root.mainloop()


if __name__ == '__main__':
    main()
def read_csv(filename):
    rows = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)  
        for row in reader:
            rows.append(row) 

    return rows
def prepare_tree_data(rows, icon_male, icon_female):
    grouped_data = {}
    for row in rows:
        if row['Gender'] == 'Male':
            row['Icon']= icon_male
        else:
            row['Icon']= icon_female

        city = row['City']  # Assuming city is in the 5th column
        if city not in grouped_data:
            grouped_data[city] = []
        grouped_data[city].append(row)
    return grouped_data
def format_currency(value):
    try:
        return f"${int(value):,}"
    except ValueError:
        return value
def create_tree_view(root, employees, icons):

    frame = ttk.Frame(root)

    treeview = ttk.Treeview(frame, columns=( "Salary","Bonus"))

    treeview.heading("#0", text="Employee")
    treeview.heading("Salary", text="Salary")
    treeview.heading("Bonus", text="Bonus")

        
    employee_data = prepare_tree_data(employees, icons['female'], icons['male'])

    for city in employee_data.keys():
        # add city
        city_id = treeview.insert('', tk.END, text=city, image=icons['city'])

        # add employees in the city
        for employee in employee_data[city]:
            treeview.insert(
                city_id, 
                tk.END, 
                text=employee['First Name'] + ' ' + employee['Last Name'], 
                values=(format_currency(employee['Salary']), format_currency(employee['Bonus'])), 
                image=employee['Icon']
            )
    # create a vertical scrollbar
    v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscrollcommand=v_scrollbar.set)

    # pack the treeview and scrollbar
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # package the frame
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
