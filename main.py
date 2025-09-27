import tkinter as tk
from pandastable import Table
import pandas as pd

top_10_gdp_nominal_table = {
    "Top 10 nominal GDP (in Trillions USD)": ["USA($25,43T)", "China($14,72T)", "Japan($4,25T)", "Germany($3,85T)", "India($3,41T)", "United Kingdom($2,67T)", "France($2,63T)", "Russia($2,24T)", "Canada($2,16T)", "Italy($2,04T)"]
}

top_10_gdp_ppp_table = {
    "Top 10 GDP (Purchasing Power Parity, in International Dollars)|": ["China($37.1T)", "USA($29,2T)", "India($16.0T)", "Russia($6.9T)", "Japan($6.6T)", "Germany($6.0T)", "Brazil($4.7T)", "Indonesia($4.7T)", "France($4.4T)", "United Kingdom($4.3T)"]
}

top_10_gdp_per_capita_table = {
    "Top 10 GDP per Capita (PPP, International Dollars)": ["Monaco($270,100)", "Liechtenstein($210,600)", "Singapore($132,600)", "Luxembourg($131,000)", "Ireland($115,300)", "Macau($112,800)", "Qatar($110,900)", "Bermuda($105,300)", "Norway($91,100)", "Switzerland($82,000)"]
}

df_1 = pd.DataFrame(top_10_gdp_nominal_table)
df_2 = pd.DataFrame(top_10_gdp_ppp_table)
df_3 = pd.DataFrame(top_10_gdp_per_capita_table)

root = tk.Tk()
root.title("GDP of countries")
root.geometry("800x800")

def show_frame(renamed_frame):
    renamed_frame.tkraise()

all_frames = tk.Frame(root)
all_frames.pack(expand = True, fill = "both")
all_frames.grid_rowconfigure(0, weight=1)
all_frames.grid_columnconfigure(0, weight=1)

main = tk.Frame(all_frames)
gdp_nominal = tk.Frame(all_frames)
gdp_ppp = tk.Frame(all_frames)
gdp_per_capita = tk.Frame(all_frames)
table_frame = tk.Frame(gdp_nominal)
table_frame.pack(expand = True, fill = "both")
table_1 = Table(table_frame, dataframe=df_1, showtoolbar=True, showstatusbar=True)
table_1.show()
table_frame = tk.Frame(gdp_ppp)
table_frame.pack(expand = True, fill = "both")
table_2 = Table(table_frame, dataframe=df_2, showtoolbar=True, showstatusbar=True)
table_2.show()
table_frame = tk.Frame(gdp_per_capita)
table_frame.pack(expand = True, fill = "both")
table_3 = Table(table_frame, dataframe=df_3, showtoolbar=True, showstatusbar=True)
table_3.show()

for frame in (main, gdp_nominal, gdp_ppp, gdp_per_capita):
    frame.grid(row=0, column=0, sticky = "nsew")

grey_label = tk.Frame(main, bg = "grey", height = 100)
grey_label.pack(fill = "both")
label = tk.Label(grey_label, text = "Main", font = ("Airal", 20), bg = "grey")
label.pack()
button = tk.Button(main, text = ">", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(gdp_nominal))
button.pack(side = "right")
button = tk.Button(main, text = "<", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(gdp_per_capita))
button.pack(side = "left")
button = tk.Button(main, text = "Exit", font = ("Airal", 20), bg = "grey", command = lambda: exit())
button.pack(side = "bottom")

grey_label = tk.Frame(gdp_nominal, bg = "grey", height = 100)
grey_label.pack(fill = "both")
label = tk.Label(grey_label, text = "Nominal GDP", font = ("Airal", 20), bg = "grey")
label.pack()
button = tk.Button(gdp_nominal, text = ">", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(gdp_ppp))
button.pack(side = "right")
button = tk.Button(gdp_nominal, text = "<", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(main))
button.pack(side = "left")
button = tk.Button(gdp_nominal, text = "Exit", font = ("Airal", 20), bg = "grey", command = lambda: exit())
button.pack(side = "bottom")

grey_label = tk.Frame(gdp_ppp, bg = "grey", height = 100)
grey_label.pack(fill = "both")
label = tk.Label(grey_label, text = "Purchasing Power Parity GDP", font = ("Airal", 20), bg = "grey")
label.pack()
button = tk.Button(gdp_ppp, text = ">", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(gdp_per_capita))
button.pack(side = "right")
button = tk.Button(gdp_ppp, text = "<", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(gdp_nominal))
button.pack(side = "left")
button = tk.Button(gdp_ppp, text = "Exit", font = ("Airal", 20), bg = "grey", command = lambda: exit())
button.pack(side = "bottom")

grey_label = tk.Frame(gdp_per_capita, bg = "grey", height = 100)
grey_label.pack(fill = "both")
label = tk.Label(grey_label, text = "GDP per capita", font = ("Airal", 20), bg = "grey")
label.pack()
button = tk.Button(gdp_per_capita, text = ">", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(main))
button.pack(side = "right")
button = tk.Button(gdp_per_capita, text = "<", font = ("Airal", 20), bg = "grey", command = lambda: show_frame(gdp_ppp))
button.pack(side = "left")
button = tk.Button(gdp_per_capita, text = "Exit", font = ("Airal", 20), bg = "grey", command = lambda: exit())
button.pack(side = "bottom")

show_frame(main)
root.mainloop()