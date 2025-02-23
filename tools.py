import webbrowser
import json

def ad(date, n):
    d, m, y = map(int, date.split())

    def dim(m, y):
        if m == 2:
            return 29 if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) else 28
        return 31 if m in [1, 3, 5, 7, 8, 10, 12] else 30

    while n:
        days = dim(m, y)
        if d + n <= days:
            d += n
            break
        n -= days - d + 1
        d = 1
        m = m + 1 if m < 12 else 1
        if m == 1:
            y += 1
    return f"{d} {m} {y}"

def tinhngay(t,d):
    def dm(m,y):
        i31 = [1, 3, 5, 7, 8, 10, 12]
        i30 = [4, 6, 9, 11]
        if m in i31: return 31
        elif m in i30: return 30
        else:
            if y%4==0: return 29
            else: return 28
    def sn(d1,m1,y1,d2,m2,y2):
        s=0
        if y2-y1<0: return 0
        if y2-y1==0:
            if m2<m1: return 0
            elif m2==m1:
                if d2< d1: return 0
                else: return d2-d1
            else:
                for i in range(m1+1,m2):
                    s=s+dm(i,y1)
                return s + dm(m1,y1)-d1+d2
        for i in range(m1+1,13):
            s=s+dm(i,y1)
        for i in range(1,m2):
            s=s+dm(i,y2)
        dem=0
        for i in range(y1+1,y2):
            if dm(2,i)==29: dem+=1
        return (y2-y1-1)*365+dem+s+(dm(m1,y1)-d1)+d2
    a=[int(x) for x in t.split()]
    b=[int(x) for x in d.split()]
    return sn(a[0],a[1],a[2],b[0],b[1],b[2])

def l1():webbrowser.open_new(r"https://github.com/thanh20VN/Nhat_kiPhatTrien_Trong_Trot_VN")

def ch(kq,tg,ab,cay): kq.set(str(ad(tg.get(), int(ab[cay.value + 1][2]))))
def luu(kq,an,ab,cay,tg,user,tm,listbox):
    if kq.get()=="": ch(kq,tg,ab,cay)
    an.append({
        'name': ab[cay.value + 1][0],
        'time':tg.get(),
        'timeEnd': kq.get(),
        'stt':cay.value+1
    })
    with open('data/'+user.get()+'/list.json',"w", encoding='utf-8') as f: json.dump(an,f,indent=4)
    listbox.insert(tm+1, ab[cay.value + 1][0])

def l2(): webbrowser.open_new(r"https://chatgpt.com/")

def thongtin(listbox,ab,gia,chuKy,Thang,benh,phan):
    index = listbox.curselection()[0] + 1
    gia.set(ab[index][1])
    chuKy.set(ab[index][2])
    Thang.set(ab[index][3])
    benh.set(ab[index][4])
    phan.set(ab[index][5])
