from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.geometry("700x700")
root.resizable(False,False)
root.title("Rajzolóka")

vonal1=[0,0,0,0,0]
vonal2=[0,0,0,0,0]
korvonal1=[0,0,0,0]
korvonal2=[0,0,0,0]
tvonal1=[0,0,0,0,0]
tvonal2=[0,0,0,0,0]
#1. vonal megrajzolása
def v1():
    try:
        if vonal1[2] + vonal1[3]==0:
            global von1
            von1=vaszon.create_line(kvx.get(),kvy.get(),bvx.get(),bvy.get(),width=vv.get())
            vonal1[0]=kvx.get()
            vonal1[1]=kvy.get()
            vonal1[2]=bvx.get()
            vonal1[3]=bvy.get()
            vonal1[4]=vv.get()
            print(vonal1) 
        else:
            vaszon.delete(von1)
            von1=vaszon.create_line(kvx.get(),kvy.get(),bvx.get(),bvy.get(),width=vv.get())
            vonal1[0]=kvx.get()
            vonal1[1]=kvy.get()
            vonal1[2]=bvx.get()
            vonal1[3]=bvy.get()
            vonal1[4]=vv.get()
    except:
        hiba=messagebox.showerror('Error 404','Értéket adjon meg!')
def vl1():
    kvx.delete(0, END)
    kvy.delete(0, END)
    bvx.delete(0, END)
    bvy.delete(0, END)
    vv.delete(0, END)
    kvx.insert(END,vonal1[0])
    kvy.insert(END,vonal1[1])
    bvx.insert(END,vonal1[2])
    bvy.insert(END,vonal1[3])
    vv.insert(END,vonal1[4])

#2. vonal megrajzolása
def v2():
    try:
        if vonal2[2] + vonal2[3]==0:
            global von2
            von2=vaszon.create_line(kvx.get(),kvy.get(),bvx.get(),bvy.get(),width=vv.get())
            vonal2[0]=kvx.get()
            vonal2[1]=kvy.get()
            vonal2[2]=bvx.get()
            vonal2[3]=bvy.get()
            vonal2[4]=vv.get()
            print(vonal2) 
        else:
            vaszon.delete(von2)
            von2=vaszon.create_line(kvx.get(),kvy.get(),bvx.get(),bvy.get(),width=vv.get())
            vonal2[0]=kvx.get()
            vonal2[1]=kvy.get()
            vonal2[2]=bvx.get()
            vonal2[3]=bvy.get()
            vonal2[4]=vv.get()
    except:
        hiba=messagebox.showerror('Error 404','Értéket adjon meg!')
def vl2():
    kvx.delete(0, END)
    kvy.delete(0, END)
    bvx.delete(0, END)
    bvy.delete(0, END)
    vv.delete(0, END)
    kvx.insert(END,vonal2[0])
    kvy.insert(END,vonal2[1])
    bvx.insert(END,vonal2[2])
    bvy.insert(END,vonal2[3])
    vv.insert(END,vonal2[4])

def v1del():
    try:
        vaszon.delete(von1)
    except:
        hiba=messagebox.showerror('Error 404','A vonal nem létezik!')

def v2del():
    try:
        vaszon.delete(von2)
    except:
        hiba=messagebox.showerror('Error 404','A vonal nem létezik!')

def vonal():
    topv=Toplevel()
    topv.title("Vonal adatai")
    topv.configure(background="#3d3d3d")
    topv.geometry("300x470")
    topv.resizable(False,False)
    lblv=Label(topv, text="Add meg a vonal adatait",background="#3d3d3d",foreground="white", font=("Arial",15))
    lblv.pack(pady=10)

    kezdvframe=LabelFrame(topv,border=0, background="#3d3d3d")
    kezdvframe.pack(pady=10)

    kezdv=Label(kezdvframe, text="Vonal kezdő koordiátái:",background="#3d3d3d",foreground="white", font=("Arial",12)) #Szoveg
    kezdv.grid(row=0, columnspan=2, pady=10)
    global kvx 
    kvx=Entry(kezdvframe, width=5, font=12) #Kezdo x koordinata
    kvx.grid(row=1,column=0, padx=10)
    global kvy
    kvy=Entry(kezdvframe, width=5, font=12) #Kezdo y koordinata
    kvy.grid(row=1,column=1, padx=10,)

    befv=Label(kezdvframe, text="Vonal végső koordiátái:",background="#3d3d3d",foreground="white", font=("Arial",12)) #Szoveg
    befv.grid(row=2, columnspan=2, pady=10)
    global bvx 
    bvx=Entry(kezdvframe, width=5, font=12) #Befejező x koordinata
    bvx.grid(row=3,column=0, padx=10)
    global bvy 
    bvy=Entry(kezdvframe, width=5, font=12) #Befejező y koordinata
    bvy.grid(row=3,column=1, padx=10,)

    vvl=Label(topv, text="Vonal vastagsáaga:",background="#3d3d3d",foreground="white", font=("Arial",12))
    vvl.pack(pady=5)
    global vv
    vv=Entry(topv,width=5, font=12) #Vonal vastagsága
    vv.pack(pady=10)

    mentes=LabelFrame(topv,border=0, background="#3d3d3d")
    mentes.pack(pady=10, padx=5)

    mer1=Button(mentes,text="Rajzolás: Vonal 1",command=v1, padx=9)
    mer1.grid( row=0,column=0,pady=10)

    mer2=Button(mentes,text="Rajzolás: Vonal 2",command=v2, padx=9)
    mer2.grid(row=0, column=1, pady=5)

    lek1=Button(mentes,text="Lekérdezés: Vonal 1",command=vl1)
    lek1.grid(row=1,column=0, pady=5, padx=2)

    lek1=Button(mentes,text="Lekérdezés: Vonal 2",command=vl2)
    lek1.grid(row=1,column=1, pady=5, padx=2)

    del1=Button(mentes,text="Törlés: Vonal 1",padx=13, command=v1del)
    del1.grid(row=2,column=0,pady=5, padx=2)

    del2=Button(mentes,text="Törlés: Vonal 2",padx=13, command=v2del)
    del2.grid(row=2,column=1,pady=5, padx=2)


    btn1=Button(topv,text="Bezárás",command=topv.destroy)
    btn1.pack( pady=10)

#1. kör megrajzolása
def k1():
    try:
        if  korvonal1[1] + korvonal1[2]==0:
            global kvon1
            kvon1=vaszon.create_oval(int(kkx.get())-int(sugar.get()), int(kky.get())-int(sugar.get()), int(kkx.get())+int(sugar.get()), int(kky.get())+int(sugar.get()),width=vk.get())
            korvonal1[0]=kkx.get()
            korvonal1[1]=kky.get()
            korvonal1[2]=sugar.get()
            korvonal1[3]=vk.get()
            print(korvonal1) 
        else:
            vaszon.delete(kvon1)
            kvon1=vaszon.create_oval(int(kkx.get())-int(sugar.get()), int(kky.get())-int(sugar.get()), int(kkx.get())+int(sugar.get()), int(kky.get())+int(sugar.get()),width=vk.get())
            korvonal1[0]=kkx.get()
            korvonal1[1]=kky.get()
            korvonal1[2]=sugar.get()
            korvonal1[3]=vk.get()
    except:
        hiba=messagebox.showerror('Error 404','Értéket adjon meg!')
def kl1():
    try:
            kkx.delete(0, END)
            kky.delete(0, END)
            sugar.delete(0, END)
            vk.delete(0,END)
            kkx.insert(END,korvonal1[0])
            kky.insert(END,korvonal1[1])
            sugar.insert(END,korvonal1[2])
            vk.insert(END,korvonal1[3])
    except:
        hiba=messagebox.showerror('Error 404','Még nem adott meg értéket')

#2. kör megrajzolása
def k2():
    try:
        if  korvonal2[1] + korvonal2[2]==0:
            global kvon2
            kvon2=vaszon.create_oval(int(kkx.get())-int(sugar.get()), int(kky.get())-int(sugar.get()), int(kkx.get())+int(sugar.get()), int(kky.get())+int(sugar.get()),width=vk.get())
            korvonal2[0]=kkx.get()
            korvonal2[1]=kky.get()
            korvonal2[2]=sugar.get()
            korvonal2[3]=vk.get()
            print(korvonal2) 
        else:
            vaszon.delete(kvon2)
            kvon2=vaszon.create_oval(int(kkx.get())-int(sugar.get()), int(kky.get())-int(sugar.get()), int(kkx.get())+int(sugar.get()), int(kky.get())+int(sugar.get()),width=vk.get())
            korvonal2[0]=kkx.get()
            korvonal2[1]=kky.get()
            korvonal2[2]=sugar.get()
            korvonal2[3]=vk.get()
    except:
        hiba=messagebox.showerror('Error 404','Értéket adjon meg!')
def kl2():
    try:
            kkx.delete(0, END)
            kky.delete(0, END)
            sugar.delete(0, END)
            vk.delete(0,END)
            kkx.insert(END,korvonal2[0])
            kky.insert(END,korvonal2[1])
            sugar.insert(END,korvonal2[2])
            vk.insert(END,korvonal2[3])
    except:
        hiba=messagebox.showerror('Error 404','Még nem adott meg értéket')

#korok torlese

def k1del():
    try:
        vaszon.delete(kvon1)
    except:
        hiba=messagebox.showerror('Error 404','A kör nem létezik!')

def k2del():
    try:
        vaszon.delete(kvon2)
    except:
        hiba=messagebox.showerror('Error 404','A kör nem létezik!')

#kor ablak
def kor():
    topk=Toplevel()
    topk.title("Vonal adatai")
    topk.configure(background="#3d3d3d")
    topk.geometry("300x470")
    topk.resizable(False,False)
    lblk=Label(topk, text="Add meg a kör adatait",background="#3d3d3d",foreground="white", font=("Arial",15))
    lblk.pack(pady=10)

    kezdkframe=LabelFrame(topk,border=0, background="#3d3d3d")
    kezdkframe.pack(pady=10)

    kezdk=Label(kezdkframe, text="Kör kezdő koordiátái:",background="#3d3d3d",foreground="white", font=("Arial",12)) #Szoveg
    kezdk.grid(row=0, columnspan=2, pady=10)
    global kkx 
    kkx=Entry(kezdkframe, width=5, font=12) #Kezdo x koordinata
    kkx.grid(row=1,column=0, padx=10)
    global kky
    kky=Entry(kezdkframe, width=5, font=12) #Kezdo y koordinata
    kky.grid(row=1,column=1, padx=10,)

    sug=Label(kezdkframe, text="Kör sugarát:",background="#3d3d3d",foreground="white", font=("Arial",12)) #Szoveg sugár
    sug.grid(row=2, columnspan=2, pady=10)
    global sugar 
    sugar=Entry(kezdkframe, width=5, font=12) #Befejező x koordinata
    sugar.grid(row=3,column=0,columnspan=2, padx=10)

    vvkl=Label(topk, text="Kör vastagsáaga:",background="#3d3d3d",foreground="white", font=("Arial",12))
    vvkl.pack(pady=5)
    global vk
    vk=Entry(topk,width=5, font=12) #Vonal vastagsága
    vk.pack(pady=10)

    mentes=LabelFrame(topk,border=0, background="#3d3d3d")
    mentes.pack(pady=15, padx=5)

    mer1=Button(mentes,text="Rajzolás: Kör 1",command=k1, padx=9)
    mer1.grid( row=0,column=0,pady=10)

    mer2=Button(mentes,text="Rajzolás: Kör 2", command=k2,padx=9)
    mer2.grid(row=0, column=1, pady=5)

    lek1=Button(mentes,text="Lekérdezés: Kör 1",command=kl1)
    lek1.grid(row=1,column=0, pady=5, padx=2)

    lek1=Button(mentes,text="Lekérdezés: Kör 2", command=kl2)
    lek1.grid(row=1,column=1, pady=5, padx=2)

    del1=Button(mentes,text="Törlés: Kör 1",padx=13, command=k1del)
    del1.grid(row=2,column=0,pady=5, padx=2)

    del2=Button(mentes,text="Törlés: Kör 2",padx=13, command=k2del)
    del2.grid(row=2,column=1,pady=5, padx=2)

    btn1=Button(topk,text="Bezárás",command=topk.destroy)
    btn1.pack()

#1. téglalap megrajzolása

def t1():
    try:
        if tvonal1[2] + tvonal1[3]==0:
            global tegl1
            tegl1=vaszon.create_rectangle(ktx.get(),kty.get(),btx.get(),bty.get(),width=vt.get())
            tvonal1[0]=ktx.get()
            tvonal1[1]=kty.get()
            tvonal1[2]=btx.get()
            tvonal1[3]=bty.get()
            tvonal1[4]=vt.get()
            print(tvonal1) 
        else:
            vaszon.delete(tegl1)
            tegl1=vaszon.create_rectangle(ktx.get(),kty.get(),btx.get(),bty.get(),width=vt.get())
            tvonal1[0]=ktx.get()
            tvonal1[1]=kty.get()
            tvonal1[2]=btx.get()
            tvonal1[3]=bty.get()
            tvonal1[4]=vt.get()
    except:
        hiba=messagebox.showerror('Error 404','Értéket adjon meg!')
def tl1():
    ktx.delete(0, END)
    kty.delete(0, END)
    btx.delete(0, END)
    bty.delete(0, END)
    vt.delete(0, END)
    ktx.insert(END,tvonal1[0])
    kty.insert(END,tvonal1[1])
    btx.insert(END,tvonal1[2])
    bty.insert(END,tvonal1[3])
    vt.insert(END,tvonal1[4])

#2. téglalap megrajzolása

def t2():
    try:
        if tvonal2[2] + tvonal2[3]==0:
            global tegl2
            tegl2=vaszon.create_rectangle(ktx.get(),kty.get(),btx.get(),bty.get(),width=vt.get())
            tvonal2[0]=ktx.get()
            tvonal2[1]=kty.get()
            tvonal2[2]=btx.get()
            tvonal2[3]=bty.get()
            tvonal2[4]=vt.get()
            print(tvonal2) 
        else:
            vaszon.delete(tegl2)
            tegl2=vaszon.create_rectangle(ktx.get(),kty.get(),btx.get(),bty.get(),width=vt.get())
            tvonal2[0]=ktx.get()
            tvonal2[1]=kty.get()
            tvonal2[2]=btx.get()
            tvonal2[3]=bty.get()
            tvonal2[4]=vt.get()
    except:
        hiba=messagebox.showerror('Error 404','Értéket adjon meg!')
def tl2():
    ktx.delete(0, END)
    kty.delete(0, END)
    btx.delete(0, END)
    bty.delete(0, END)
    vt.delete(0, END)
    ktx.insert(END,tvonal2[0])
    kty.insert(END,tvonal2[1])
    btx.insert(END,tvonal2[2])
    bty.insert(END,tvonal2[3])
    vt.insert(END,tvonal2[4])

def t1del():
    try:
        vaszon.delete(tegl1)
    except:
        hiba=messagebox.showerror('Error 404','A téglalap nem létezik!')

def t2del():
    try:
        vaszon.delete(tegl2)
    except:
        hiba=messagebox.showerror('Error 404','A téglalap nem létezik!')

        
def teglal():
    topt=Toplevel()
    topt.title("Téglalap adatai")
    topt.configure(background="#3d3d3d")
    topt.geometry("300x470")
    topt.resizable(False,False)
    lblt=Label(topt, text="Add meg a téglalap adatait",background="#3d3d3d",foreground="white", font=("Arial",15))
    lblt.pack(pady=10)

    kezdtframe=LabelFrame(topt,border=0, background="#3d3d3d")
    kezdtframe.pack(pady=10)

    kezdt=Label(kezdtframe, text="Téglalap kezdő koordiátái:",background="#3d3d3d",foreground="white", font=("Arial",12)) #Szoveg
    kezdt.grid(row=0, columnspan=2, pady=10)
    global ktx 
    ktx=Entry(kezdtframe, width=5, font=12) #Kezdo x koordinata
    ktx.grid(row=1,column=0, padx=10)
    global kty
    kty=Entry(kezdtframe, width=5, font=12) #Kezdo y koordinata
    kty.grid(row=1,column=1, padx=10,)

    beft=Label(kezdtframe, text="Téglalap végső koordiátái:",background="#3d3d3d",foreground="white", font=("Arial",12)) #Szoveg
    beft.grid(row=2, columnspan=2, pady=10)
    global btx 
    btx=Entry(kezdtframe, width=5, font=12) #Befejező x koordinata
    btx.grid(row=3,column=0, padx=10)
    global bty 
    bty=Entry(kezdtframe, width=5, font=12) #Befejező y koordinata
    bty.grid(row=3,column=1, padx=10,)

    vtl=Label(topt, text="Téglalap vastagsáaga:",background="#3d3d3d",foreground="white", font=("Arial",12))
    vtl.pack(pady=5)
    global vt
    vt=Entry(topt,width=5, font=12) #Vonal vastagsága
    vt.pack(pady=10)

    mentes=LabelFrame(topt,border=0, background="#3d3d3d")
    mentes.pack(pady=10, padx=5)

    mer1=Button(mentes,text="Rajzolás: Téglalap 1",command=t1, padx=9)
    mer1.grid( row=0,column=0,pady=10)

    mer2=Button(mentes,text="Rajzolás: Téglalap 2",command=t2, padx=9)
    mer2.grid(row=0, column=1, pady=5)

    lek1=Button(mentes,text="Lekérdezés: Téglalap 1",command=tl1)
    lek1.grid(row=1,column=0, pady=5, padx=2)

    lek1=Button(mentes,text="Lekérdezés: Téglalap 2",command=tl2)
    lek1.grid(row=1,column=1, pady=5, padx=2)

    del1=Button(mentes,text="Törlés: Téglalap 1",padx=13, command=t1del)
    del1.grid(row=2,column=0,pady=5, padx=2)

    del2=Button(mentes,text="Törlés: Téglalap 2",padx=13, command=t2del)
    del2.grid(row=2,column=1,pady=5, padx=2)


    btn1=Button(topt,text="Bezárás",command=topt.destroy)
    btn1.pack( pady=10)

def delete():
    vaszon.delete('all')
vaszon=Canvas(root,bg="white",height=400,width=650)
vaszon.pack(pady=25,padx=20)
root.configure(background="#3d3d3d")

aframe=LabelFrame(root,bg="#3d3d3d",border=0,fg="white")
aframe.pack(padx=20)
gomb=Button(aframe,text="Vonal",bg="#81689D",fg="white",padx=10,pady=5, font=("Courier New",20), command=vonal)
gomb.grid(row=0,column=0,padx=30 )

gomb2=Button(aframe,text="Kör",bg="#81689D",fg="white",padx=30,pady=5, font=("Courier New",20),command=kor)
gomb2.grid(row=0,column=1,padx=30 )

gomb3=Button(aframe,text="Téglalap",bg="#81689D",fg="white",padx=10,pady=5, font=("Courier New",20), command=teglal)
gomb3.grid(row=0,column=2,padx=30 )

torol=Button(root,text="Összes törlése",bg="#81689D",fg="white",pady=5, font=("Courier New",10), command=delete)
torol.pack(padx=30, pady=70)

root.mainloop()