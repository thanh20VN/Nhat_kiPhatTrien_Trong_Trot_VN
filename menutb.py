from tkinter import *
from tkinter import ttk
from tools import *

def tb(ro,icon,an,tg,user,tm,listbox,kq,hn,ab,cay):
    if tg.get()=="": tg.set(hn)
    if kq.get()=="": ch(kq,tg,ab,cay)
    rt=Toplevel(ro)
    rt.title("Bạn chắc chắc chưa")
    rt.geometry("350x200")
    rt.resizable(False, False)
    rt.iconphoto(True, icon)
    def h1():
        luu(kq,an,ab,cay,tg,user,tm,listbox)
        rt.destroy()
        return
    def h2():
        kq.set("")
        rt.destroy()
        return
    Label(rt, text="Bạn đã sẵn sàng trồng cây "+ab[cay.value + 1][0]+"?", font=("Times New Roman bold", 13)).place(relx=0.5, rely=0.1, anchor="center")
    Label(rt, text="Dự kiến thu hoạch:", font=("Times New Roman bold", 15)).place(relx=0.3, rely=0.3, anchor="center")
    Label(rt, textvariable=kq, font=("Times New Roman bold", 15)).place(relx=0.7, rely=0.3, anchor="center")
    Label(rt, text="Giá tham khảo:", font=("Times New Roman bold", 15)).place(relx=0.3, rely=0.5, anchor="center")
    Label(rt, text=ab[cay.value + 1][1], font=("Times New Roman bold", 15)).place(relx=0.7, rely=0.5, anchor="center")
    Button(rt, text="Tôi sẵn sàng trồng", command=lambda: h1()).place(relx=0.3, rely=0.8, anchor="center")
    Button(rt, text="Tôi chưa muốn trồng", command=lambda: h2()).place(relx=0.7, rely=0.8, anchor="center")
    rt.mainloop()