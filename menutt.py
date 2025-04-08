from tkinter import *
from tkinter import ttk
from tools import *

def tt(root,icon):
    rt=Toplevel(root)
    rt.title("Thông tin phần mềm")
    rt.geometry("450x400")
    rt.resizable(False, False)
    rt.iconphoto(True, icon)
    ttk.Label(rt, text="Phần mềm Nhật Ký Phát Triển Nông Nhiệp", font=("Times New Roman bold", 13)).place(relx=0.5, rely=0.1, anchor="center")
    ttk.Label(rt, text="Nhà phát triển:", font=("Times New Roman bold", 12)).place(relx=0.13, rely=0.2, anchor="center")
    ttk.Label(rt, text="Trương Minh Thành 8A1 (Thanh20VN)", font=("Times New Roman bold", 11)).place(relx=0.35, rely=0.25, anchor="center")
    ttk.Label(rt, text="Suorce code (github):", font=("Times New Roman bold", 12)).place(relx=0.17, rely=0.3, anchor="center")
    t = Label(rt, text="https://github.com/thanh20VN/Nhat_kiPhatTrien_Trong_Trot_VN", fg="blue", cursor="hand2", font=("Times New Roman", 10, 'underline'))
    t.place(relx=0.45, rely=0.35, anchor="center")
    t.bind("<Button-1>", lambda event: l1())
    ttk.Label(rt, text="Nguồn:", font=("Times New Roman bold", 12)).place(relx=0.07, rely=0.4, anchor="center")
    ttk.Label(rt, text="Các loài cây từ ChatGPT (đã lược bỏ bớt)", font=("Times New Roman bold", 11)).place(relx=0.35, rely=0.45, anchor="center")
    ttk.Label(rt, text="Phiên bản:", font=("Times New Roman bold", 12)).place(relx=0.095, rely=0.5, anchor="center")
    ttk.Label(rt, text="Beta 0.3", font=("Times New Roman bold", 11)).place(relx=0.25, rely=0.5, anchor="center")
