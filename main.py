#База, константи
import pandas as pd
import tkinter as tk
from tkinter import ttk   #Імпортуємо бібліотеки

top_10_gdp_per_capita_table = {
    "Top 10 GDP per Capita (PPP, International Dollars)": ["Monaco($270,100)", "Liechtenstein($210,600)", "Singapore($132,600)", "Luxembourg($131,000)", "Ireland($115,300)", "Macau($112,800)", "Qatar($110,900)", "Bermuda($105,300)", "Norway($91,100)", "Switzerland($82,000)"]
}

top_10_gdp_nominal_table = {
    "Top 10 nominal GDP (in Trillions USD)": ["USA($25,43T)", "China($14,72T)", "Japan($4,25T)", "Germany($3,85T)", "India($3,41T)", "United Kingdom($2,67T)", "France($2,63T)", "Russia($2,24T)", "Canada($2,16T)", "Italy($2,04T)"]
}

top_10_gdp_ppp_table = {
    "Top 10 GDP (Purchasing Power Parity, in International Dollars)|": ["China($37.1T)", "USA($29,2T)", "India($16.0T)", "Russia($6.9T)", "Japan($6.6T)", "Germany($6.0T)", "Brazil($4.7T)", "Indonesia($4.7T)", "France($4.4T)", "United Kingdom($4.3T)"]
}

df_1 = pd.DataFrame(top_10_gdp_per_capita_table)
df_2 = pd.DataFrame(top_10_gdp_nominal_table)
df_3 = pd.DataFrame(top_10_gdp_ppp_table)    #Таблиці

def show_frame(frame):
    frame.tkraise()   #Піднімаємо вибраний екран(фрейм)

root = tk.Tk()
root.title("GDP of countries")
root.attributes("-fullscreen", True)    #Робимо вікно

all_frames = tk.Frame(root)
all_frames.pack(expand = True, fill = "both")
all_frames.grid_rowconfigure(0, weight=1)
all_frames.grid_columnconfigure(0, weight=1)    #Розміщуємо та налаштовуємо переміну в якій будуть всі екрани(фрейми)

main = tk.Frame(all_frames, bg = "white")
top_10_gdp = tk.Frame(all_frames, bg = "white")
top_10_gdp_per_capita = tk.Frame(all_frames, bg = "white")
top_10_gdp_nominal = tk.Frame(all_frames, bg = "white")
top_10_gdp_ppp = tk.Frame(all_frames, bg = "white")   #Екрани(фрейми)

for frame in (main, top_10_gdp, top_10_gdp_per_capita, top_10_gdp_nominal, top_10_gdp_ppp):
    frame.grid(row=0, column=0, sticky="nsew")   #Ростягуємо екран(фрейм)


#Кнопки, лейбли
top_frame = tk.Frame(main, bg = "grey", height = 100)
top_frame.pack(side = "top", fill = "both")   #Робимо верхню частину сірого кольору(main)

label = tk.Label(top_frame, text = "Top 10 GDP countries in each category", font = ("Airal", 20), bg = "grey")
label.pack()    #Розміщуємо текст(main(top_frame))

button = tk.Button(main, text = "View the top 10 GDP", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(top_10_gdp))
button.place(x = 100, y = 50)
button = tk.Button(main, text = "View the chart of GDP growth over the last 25 years", font = ("Airal", 20), bg = "grey")
button.place(x = 600, y = 50)
button = tk.Button(main, text = "View the average values", font = ("Airal", 20), bg = "grey")
button.place(x = 1500, y = 50)
button = tk.Button(main, text = "Exit", font = ("Airal", 20), bg = "grey")
button.place(x = 10, y = 1015)
button = tk.Button(main, text = "Update log", font = ("Airal", 20), bg = "grey")
button.place(x = 1400, y = 1015)
button = tk.Button(main, text = "Setting", font = ("Airal", 20), bg = "grey")
button.place(x = 1600, y = 1015)
button = tk.Button(main, text = "FAQ", font = ("Airal", 20), bg = "grey")
button.place(x = 1750, y = 1015)    #Розміщуємо кнопки(main)

top_frame = tk.Frame(top_10_gdp, top_10_gdp_per_capita,  bg = "grey", height = 38)
top_frame.pack(side = "top", fill = "both")   #Робимо верхню частину сірого кольору(top_10_gdp)

label = tk.Label(top_frame, text = "Top 10 GDP", font = ("Airal", 20), bg = "grey")
label.pack()    #Розміщуємо текст(top_10_gdp(top_frame))

button = tk.Button(top_10_gdp, text = "View top 10 GDP per capita (PPP, International Dollars)", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(top_10_gdp_per_capita))
button.place(x = 100, y = 50)
button = tk.Button(top_10_gdp, text = "View top 10 nominal GDP (in Trillions USD))", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(top_10_gdp_nominal))
button.place(x = 1260, y = 50)
button = tk.Button(top_10_gdp, text = "View top 10 GDP (Purchasing Power Parity, in International Dollars)", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(top_10_gdp_ppp))
button.place(x = 550, y = 115)
button = tk.Button(top_10_gdp, text = "Back", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(main))
button.place(x = 10, y = 1015)
button = tk.Button(top_10_gdp_per_capita, text = "Back", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(top_10_gdp))
button.place(x = 10, y = 1015)   #Розміщуємо кнопки(top_10_gdp) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

top_frame = tk.Frame(top_10_gdp_per_capita, bg = "grey", height = 38)
top_frame.pack(side = "top", fill = "both")   #Робимо верхню частину сірого кольору(top_10_gdp_per_capita)

label = tk.Label(top_frame, text = "Top 10 GDP per capita (PPP, International Dollars)", font = ("Airal", 20), bg = "grey")
label.pack()    #Розміщуємо текст(top_10_gdp_per_capita(top_frame))


#Таблиці
table_1 = ttk.Treeview(top_10_gdp_per_capita, columns=list(df_1.columns), show="headings")   #Робимо таблицю(1)

for col in df_1.columns:
    table_1.heading(col, text=col)
    table_1.column(col, width=300, anchor="center")

for _, row in df_1.iterrows():
    table_1.insert("", tk.END, values=list(row))

table_1.pack(expand=True, fill="both")    #Задаємо параметри та розміщуємо таблицю(1)

table_2 = ttk.Treeview(top_10_gdp_nominal, columns=list(df_2.columns), show="headings")   #Робимо таблицю

for col in df_2.columns:
    table_2.heading(col, text=col)
    table_2.column(col, width=300, anchor="center")

for _, row in df_2.iterrows():
    table_2.insert("", tk.END, values=list(row))

table_2.pack(expand=True, fill="both")    #Задаємо параметри та розміщуємо таблицю(2)

table_3 = ttk.Treeview(top_10_gdp_ppp, columns=list(df_3.columns), show="headings")   #Робимо таблицю(3)

for col in df_3.columns:
    table_3.heading(col, text=col)
    table_3.column(col, width=300, anchor="center")

for _, row in df_3.iterrows():
    table_3.insert("", tk.END, values=list(row))

table_3.pack(expand=True, fill="both")    #Задаємо параметри та розміщуємо таблицю(2)


#Виклик та ініціалізація
show_frame(main)    #Викликаємо фунцію

root.mainloop()   #Запуск вікна