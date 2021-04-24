import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from ImageUtils import *
from tkinter import ttk


def mode_select():
    if cmb.get() == '图片集':
        path.set(askopenfilename())
        deal_images(path.get())
    if cmb.get() == '图片文件':
        path.set(askopenfilename(filetypes=[('JPEG','*.jpeg'), ('JPG', '*.jpg'), ('BMP', '*.bmp'), ('PNG', '*.png'), ('ALL FILES', '*')]))
        deal_image(path.get())
    if cmb.get() == '图片文件多选':
        path.set(askdirectory(title="选择地址"))
        deal_multi_image(path.get())


top = tk.Tk()

path = tk.StringVar()
tk.Label(top, text="目标路径/文件").grid(row=0, column=0)
tk.Entry(top, textvariable=path).grid(row=0, column=1)
tk.Button(top, text="选择", command=mode_select).grid(row=0, column=2)
tk.Label(top, text='类型选择').grid(row=1, column=0)
cmb = tk.ttk.Combobox(top)
cmb.grid(row=1, column=1)
cmb['value'] = ('图片集', '图片文件', '图片文件多选')

top = tk.mainloop()


