from datetime import datetime
from tkinter import *
from tkinter import ttk
import json
from tools import *
from listtree import *
from menukt import *
from menutt import *

class Cay:
    def __init__(self, value):
        self.value = value

cay = Cay(0)
def start(user,ab):
    with open('data/'+user.get()+'/list.json',"r", encoding='utf-8') as f:an=json.load(f)
    to = datetime.today()
    hn = str(to.day) + " " + str(to.month) + " " + str(to.year)
    root = Tk()
    root.title("Nhật Ký Phát Triển Trồng Trọt")
    root.geometry("450x400")
    root.resizable(False, False)
    kq = StringVar()
    tg = StringVar()
    icon = PhotoImage(file=r'data\icon.png')
    root.iconphoto(True, icon)

    for j in range(100):
        i=0
        cu=len(an)
        while True:
            if i==len(an)+1 or i==len(an):
                break
            elif tinhngay(hn,an[i]['timeEnd'])==0:
                del an[i]
                i+=1
            else: i+=1
        if cu==len(an): break
    with open('data/'+user.get()+'/list.json',"w", encoding='utf-8') as f: json.dump(an,f,indent=4)
    

    ttk.Label(root, text="Tên cây:", font=("Times New Roman bold", 10)).place(relx=0.1, rely=0.1, anchor="center")
    ttk.Button(root, text="Danh sách cây", command=lambda: help(root,ab,cay)).place(relx=0.5, rely=0.1, anchor="center")
    ttk.Label(root, text="Thời gian trồng:", font=("Times New Roman bold", 10)).place(relx=0.12, rely=0.18, anchor="center")
    ttk.Entry(root, textvariable=tg, width=35).place(relx=0.48, rely=0.18, anchor="center")

    listbox = Listbox(root,width=60,height=14)
    listbox.place(relx=0.5, rely=0.63, anchor="center")
    tm=0
    if not an==[]:
        for i in range(0,len(an)):
            listbox.insert(i+1, an[i]['name'])
            tm=i+1
    for i in range(0,len(an)):
        s=ab[int(an[i]['stt'])][3].split(" – ")
        if len(s)==1:
            if s[0]==str(to.month):
                listbox.itemconfigure(i, fg="red")
        else:
            for j in s:
                if  j ==str(to.month):
                    listbox.itemconfigure(i, fg="red")
        if tinhngay(hn,an[i]['timeEnd']) <= 5:
            listbox.itemconfigure(i, fg="blue")
    listbox.select_set(0)
    ttk.Button(root, text="Kiểm tra", command=lambda: kt(root,icon,ab,an,listbox,hn)).place(relx=0.5, rely=0.95, anchor="center")
    ttk.Button(root, text="Lấy ngày hôm nay", command=lambda: tg.set(hn)).place(relx=0.86, rely=0.18, anchor="center")
    ttk.Button(root, text="Lưu", command=lambda: luu(kq,an,ab,cay,tg,user,tm,listbox)).place(relx=0.65, rely=0.28, anchor="center")
    ttk.Label(root, text="Thời gian dự kiến:", font=("Times New Roman bold", 10)).place(relx=0.13, rely=0.28, anchor="center")
    ttk.Button(root,text="Thông tin", command=lambda: tt(root,icon)).place(relx=0.1, rely=0.95, anchor="center")
    ttk.Label(root, textvariable=kq, font=("Times New Roman bold", 10)).place(relx=0.31, rely=0.28, anchor="center")
    ttk.Label(root, text=hn, font=("Times New Roman bold", 10)).place(relx=0.9, rely=0.03, anchor="center")
    ttk.Label(root, text="Hôm nay là:", font=("Times New Roman bold", 10)).place(relx=0.75, rely=0.03, anchor="center")
    ttk.Button(root,text="Tìm kiếm", command=l2).place(relx=0.11, rely=0.04, anchor="center")
    root.mainloop()
