from tkinter import *
from tkinter import ttk
import hashlib
import json
from pathlib import Path
from menustart import start

def setup(us,up):
    rt = Toplevel(up)
    rt.title("đăng kí")
    rt.geometry("350x200")
    rt.resizable(False, False)
    icon = PhotoImage(file=r"data\icon.png")
    rt.iconphoto(True, icon)
    dkuser = StringVar()
    dkpas = StringVar()

    def dk():
        for i in us:
            if dkuser.get() in i:
                dkuser.set("")
                dkpas.set("")
                ttk.Label(up, text="đã có tên tài khoản như vậy").place(
                    relx=0.5, rely=0.55, anchor="center"
                )
                return
        p = hashlib.md5(dkpas.get().encode()).hexdigest()
        us.append({'user':dkuser.get(),'pass':p},)

        with open("data/user.json", "w") as f:
            json.dump(us,f,indent=4)
        folder = Path("data/" + dkuser.get())
        folder.mkdir(exist_ok=True)
        with open('data/'+dkuser.get()+'/list.json', 'x') as file:
            file.write("[\n]")
        rt.destroy()

    ttk.Entry(rt, textvariable=dkuser, width=37).place(relx=0.52, rely=0.1, anchor="center")
    ttk.Entry(rt, textvariable=dkpas, width=37, show="*").place(relx=0.52, rely=0.25, anchor="center")
    ttk.Button(rt, text="Đăng kí", command=dk).place(relx=0.5, rely=0.4, anchor="center")
    ttk.Label(rt, text="Tên:").place(relx=0.1, rely=0.1, anchor="center")
    ttk.Label(rt, text="Mật khuẩn:").place(relx=0.1, rely=0.25, anchor="center")

def dkdn(us,ab):
    up = Tk()
    up.title("Đăng Nhập")
    up.geometry("350x200")
    up.resizable(False, False)
    icon = PhotoImage(file=r"data\icon.png")
    up.iconphoto(True, icon)

    user = StringVar()
    pas = StringVar()


    def lo():
        p = hashlib.md5(pas.get().encode()).hexdigest()
        for i in us:
            if i['user']==user.get():
                if i['pass']==p:
                    up.destroy()
                    start(user,ab)
                    return
        user.set("")
        pas.set("")
        ttk.Label(up, text="Mật khuẩn sai hay tên tài khoản sai").place(relx=0.5, rely=0.55, anchor="center")


    ttk.Entry(up, textvariable=user, width=37).place(relx=0.52, rely=0.1, anchor="center")
    ttk.Entry(up, textvariable=pas, width=37, show="*").place(relx=0.52, rely=0.25, anchor="center")
    ttk.Button(up, text="Đăng nhập", command=lo).place(relx=0.37, rely=0.4, anchor="center")
    ttk.Button(up, text="đăng kí", command=lambda: setup(us,up)).place(relx=0.6, rely=0.4, anchor="center")
    ttk.Label(up, text="Tên:").place(relx=0.1, rely=0.1, anchor="center")
    ttk.Label(up, text="Mật khuẩn:").place(relx=0.1, rely=0.25, anchor="center")
    up.mainloop()
