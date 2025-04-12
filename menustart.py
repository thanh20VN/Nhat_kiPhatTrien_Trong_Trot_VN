from datetime import datetime
from tkinter import *
from tkinter import ttk
import json
from tools import *
from listtree import *
from menukt import *
from menutt import *
from menutb import *

class Cay:
    def __init__(self, value):
        self.value = value

cay = Cay(0)
def start(user,ab):
    root = Tk()
    with open('data/'+user.get()+'/list.json',"r", encoding='utf-8') as f:an=json.load(f)
    to = datetime.today()
    if len(str(to.day))==1:
        hn ="0"+ str(to.day) + " " + str(to.month) + " " + str(to.year)
        hn1 ="0"+ str(to.day) + "/" + str(to.month) + "/" + str(to.year)
    elif len(str(to.month))==1:
        hn = str(to.day) + " 0" + str(to.month) + " " + str(to.year)
        hn1 = str(to.day) + "/0" + str(to.month) + "/" + str(to.year)
    if len(str(to.day))==1 and len(str(to.month))==1:
        hn ="0"+ str(to.day) + " 0" + str(to.month) + " " + str(to.year)
        hn1 ="0"+ str(to.day) + "/0" + str(to.month) + "/" + str(to.year)
    else:
        hn = str(to.day) + " " + str(to.month) + " " + str(to.year)
        hn1 = str(to.day) + "/" + str(to.month) + "/" + str(to.year)
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

    listbox = Listbox(root,width=60,height=15)
    listbox.place(relx=0.5, rely=0.58, anchor="center")
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
    3.0, listbox.select_set(0)
    ttk.Button(root, text="Kiểm tra", command=lambda: kt(root,icon,ab,an,listbox,hn)).place(relx=0.5, rely=0.95, anchor="center")
    ttk.Button(root, text="Lưu", command=lambda: tb(root,icon,an,tg,user,tm,listbox,kq,hn,ab,cay)).place(relx=0.86, rely=0.18, anchor="center")
    ttk.Button(root,text="Thông tin", command=lambda: tt(root,icon)).place(relx=0.1, rely=0.95, anchor="center")
    ttk.Label(root, text=hn1, font=("Times New Roman bold", 10)).place(relx=0.9, rely=0.03, anchor="center")
    ttk.Label(root, text="Hôm nay là:", font=("Times New Roman bold", 10)).place(relx=0.75, rely=0.03, anchor="center")
    t = Label(root, text="Tìm kiếm", fg="blue", cursor="hand2", font=("Times New Roman", 10, 'underline'))
    t.place(relx=0.07, rely=0.03, anchor="center")
    t.bind("<Button-1>", lambda event: l2())
    root.mainloop()