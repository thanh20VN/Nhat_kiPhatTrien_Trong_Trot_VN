from tkinter import *
from tkinter import ttk
from tools import *

def help(p,ab,cay):
    rt = Toplevel(p)
    rt.title("Danh sách")
    rt.geometry("450x400")
    rt.resizable(False, False)
    icon = PhotoImage(file=r'data\icon.png')
    rt.iconphoto(True, icon)

    listbox = Listbox(rt)
    listbox.pack(padx=10, pady=10, fill=BOTH, expand=False)
    for i in range(1, len(ab)):
        listbox.insert(i, ab[i][0])
    listbox.select_set(0)
    
    gia = StringVar(value="None")
    chuKy = StringVar(value="None")
    Thang = StringVar(value="None")
    benh = StringVar(value="None")
    phan = StringVar(value="None")
    def out():
        cay.value=listbox.curselection()[0]
        rt.destroy()
    ttk.Button(rt, text="Chọn", command=out).place(relx=0.6, rely=0.48, anchor="center")
    ttk.Button(rt, text="Thông tin", command=lambda: thongtin(listbox,ab,gia,chuKy,Thang,benh,phan)).place(relx=0.4, rely=0.48, anchor="center")

    ttk.Label(rt, text=ab[0][1], font=("Times New Roman bold", 11)).place(relx=0.21, rely=0.55, anchor="center")
    ttk.Label(rt, text=ab[0][2], font=("Times New Roman bold", 11)).place(relx=0.13, rely=0.64, anchor="center")
    ttk.Label(rt, text=ab[0][3], font=("Times New Roman bold", 11)).place(relx=0.19, rely=0.73, anchor="center")
    ttk.Label(rt, text=ab[0][4], font=("Times New Roman bold", 11)).place(relx=0.22, rely=0.82, anchor="center")
    ttk.Label(rt, text=ab[0][5], font=("Times New Roman bold", 11)).place(relx=0.16, rely=0.91, anchor="center")

    ttk.Label(rt, textvariable=gia, font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.6, anchor="center")
    ttk.Label(rt, textvariable=chuKy, font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.689, anchor="center")
    ttk.Label(rt, textvariable=Thang, font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.78, anchor="center")
    ttk.Label(rt, textvariable=benh, font=("Times New Roman bold", 11)).place(relx=0.50, rely=0.87, anchor="center")
    ttk.Label(rt, textvariable=phan, font=("Times New Roman bold", 10)).place(relx=0.50, rely=0.95, anchor="center")

    rt.mainloop()
