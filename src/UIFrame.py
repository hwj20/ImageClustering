import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from ImageUtils import *
from tkinter import ttk


def mode_select():
    if cmb.get() == '图片集':
        path.set(askdirectory())
        deal_images(path.get(), check.get() == 1, 'ecludDist' if cmb.get() == '欧拉距离' else 'manhattanDist',
                    cmb3.get() == '随机取值', int(dots.get()))
    if cmb.get() == '图片文件':
        path.set(askopenfilename(
            filetypes=[('JPEG', '*.jpeg'), ('JPG', '*.jpg'), ('BMP', '*.bmp'), ('ALL FILES', '*')]))
        ret = deal_image(path.get(), int(steps.get()), int(dots.get()), True, check.get() == 1,
                         'ecludDist' if cmb.get() == '欧拉距离' else 'manhattanDist', cmb3.get() == '随机取值')
        if ret is ReturnCode.INVALID_STEPS:
            messagebox.showerror('错误', '无效的steps')
        if ret is ReturnCode.NO_SUCH_FILE:
            messagebox.showerror('错误', '未找到文件')
        if ret is ReturnCode.INVALID_DOTS:
            messagebox.showerror('错误', '错误的均值点个数')
    # if cmb.get() == '图片文件多选':
    #     path.set(askdirectory(title="选择地址"))
    #     deal_multi_image(path.get(), 50)


top = tk.Tk()
top.title('ImageClustering')

path = tk.StringVar()
check = tk.IntVar()
steps = tk.StringVar()
dots = tk.StringVar()

tk.Label(top, text="目标路径/文件").grid(row=0, column=0)
tk.Entry(top, textvariable=path).grid(row=0, column=1)
tk.Button(top, text="选择", command=mode_select).grid(row=0, column=2)
tk.Label(top, text='类型选择').grid(row=1, column=0)
cmb = tk.ttk.Combobox(top)
cmb.grid(row=1, column=1)
# cmb['value'] = ('图片集', '图片文件', '图片文件多选')
cmb['value'] = ('图片集', '图片文件')
cmb.current(1)
tk.Checkbutton(top, text='保存', variable=check, onvalue=1, offvalue=0).grid(row=1, column=2)
tk.Label(top, text='steps').grid(row=2, column=0)
tk.Entry(top, textvariable=steps).grid(row=2, column=1)
steps.set('50')
tk.Label(top, text='距离方法').grid(row=2, column=2)
cmb2 = tk.ttk.Combobox(top)
cmb2.grid(row=2, column=3)
cmb2['value'] = ('欧拉距离', '曼哈顿距离')
cmb2.current(0)

tk.Label(top, text='均值点个数').grid(row=3, column=0)
tk.Entry(top, textvariable=dots).grid(row=3, column=1)
dots.set('3')
tk.Label(top, text='初始值选择').grid(row=3, column=2)
cmb3 = tk.ttk.Combobox(top)
cmb3.grid(row=3, column=3)
cmb3['value'] = ('随机取值', '顺序取值')
cmb3.current(0)

top = tk.mainloop()
