from tools import *
from tkinter import *
from tkinter import ttk
def kt(root,icon,ab,an,listbox,hn):
    if an==[] or listbox.curselection()==():return
    rt= Toplevel(root)
    rt.geometry("450x400")
    rt.resizable(False, False)
    rt.iconphoto(True, icon)
    ttk.Label(rt, text="Tên:", font=("Times New Roman bold", 11)).place(relx=0.06, rely=0.05, anchor="center")
    ttk.Label(rt, text=ab[0][1], font=("Times New Roman bold", 11)).place(relx=0.19, rely=0.14, anchor="center")
    ttk.Label(rt, text=ab[0][2], font=("Times New Roman bold", 11)).place(relx=0.13, rely=0.24, anchor="center")
    ttk.Label(rt, text=ab[0][3], font=("Times New Roman bold", 11)).place(relx=0.19, rely=0.33, anchor="center")
    ttk.Label(rt, text=ab[0][4], font=("Times New Roman bold", 11)).place(relx=0.22, rely=0.42, anchor="center")
    ttk.Label(rt, text=ab[0][5], font=("Times New Roman bold", 11)).place(relx=0.16, rely=0.54, anchor="center")
    ttk.Label(rt, text="Thời gian dự kiến:", font=("Times New Roman bold", 11)).place(relx=0.16, rely=0.64, anchor="center")
    ttk.Label(rt, text="Còn khoảng mấy ngày:", font=("Times New Roman bold", 11)).place(relx=0.19, rely=0.73, anchor="center")

    ttk.Label(rt, text=an[listbox.curselection()[0]]['name'], font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.07, anchor="center")
    ttk.Label(rt, text=ab[int(an[listbox.curselection()[0]]['stt'])][1], font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.19, anchor="center")
    ttk.Label(rt, text=ab[int(an[listbox.curselection()[0]]['stt'])][2], font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.27, anchor="center")
    ttk.Label(rt, text=ab[int(an[listbox.curselection()[0]]['stt'])][3], font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.36, anchor="center")
    ttk.Label(rt, text=ab[int(an[listbox.curselection()[0]]['stt'])][4], font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.48, anchor="center")
    ttk.Label(rt, text=ab[int(an[listbox.curselection()[0]]['stt'])][5], font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.59, anchor="center")
    ttk.Label(rt, text=an[listbox.curselection()[0]]['timeEnd'], font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.67, anchor="center")
    ttk.Label(rt, text=tinhngay(hn,an[listbox.curselection()[0]]['timeEnd']), font=("Times New Roman bold", 11)).place(relx=0.5, rely=0.78, anchor="center")
