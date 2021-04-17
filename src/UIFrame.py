import tkinter as tk
from tkinter.filedialog import askdirectory


def select_path():
    path.set(askdirectory())


top = tk.Tk()

path = tk.StringVar()
tk.Label(top, text="目标路径").grid(row=0, column=0)
tk.Entry(top, textvariable=path).grid(row=0, column=1)
tk.Button(top, text="路径选择", command=select_path).grid(row=0, column=2)

top = tk.mainloop()
