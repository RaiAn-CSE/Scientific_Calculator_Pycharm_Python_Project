import tkinter
from tkinter import font
from tkinter import *
from tooltip import *
from datetime import date
import time
import math
import datetime
import calendar
import cmath
import statistics
from statistics import *
from tkinter import ttk


#=====================================Arithmetic operation code========================================

operator = ''
def num(numbers):
    global operator
    operator = text_input.get()
    operator += str(numbers)
    text_input.set(operator)


def calculation():
    s = text_input.get()
    if 'e' in s:
        text_input.set(eval(s))
    elif '^' in s:
        calpow(s)
    else:
        text_input.set(eval(s))
        global operator
        operator = text_input.get()





#=====================================window initialize========================================

root=Tk()
root.title("Scientific Calculator")
root.geometry('900x630')
root.iconbitmap("img.ico")

#--------------------window background change--------------------
root.configure(bg='#30475e')



#---------------------------------font----------------------------
f=font.Font(family='LCDMono2',size=20,weight='bold')
ff1=font.Font(family='Century',size=25,weight='bold')
f1=font.Font(family='Calibri (Body)',size=20,weight='bold')
f2=font.Font(family='Arial italic',size=8,weight='normal')
font.families()


#----------------------------------------Weekday--------------------------------
import datetime
now = datetime.datetime.now()
now=now.strftime("%A,")
week=Label(root,text=now,font=('Arial',18),bg='#30475e',fg='#a8dda8')
week.place(x=400,y=30)



#----------------------------------------Date ----------------------------------
today=date.today()
today=today.strftime("%B %d,%y")
date_label=Label(root,text=today,font=('Arial',18),bg='#30475e',fg='#a8dda8')
date_label.place(x=500,y=30)

#--------------------------------------Time--------------------------------------
def my_watch():
    x=time.strftime("%H:%M:%S")
    clock.config(text=x)
    clock.after(100,my_watch)

clock=Label(root,font=f,bg='#30475e',fg='#19d3da')
clock.place(x=730,y=30)
my_watch()


#Entry box
text_input=StringVar()
enter=Entry(root,bd=10,width=43,insertwidth=4,font=ff1,bg='#cdc9c3',text=text_input)
enter.place(x=30,y=100)


#button widgets

#---------------------------1st line----------------------------------------------------------------------------------


squaret=Button(root,text='√Sqrt',font=("Arial",12,"bold"),bg="#0f0c29",fg="white",command=lambda : sq())
squaret.place(x=30,y=200)
#----------------------------Dynamic-tooltip----------------------
CreateToolTip(squaret,"Enter a value \n find root of a value\n for example: √4=2")

def sq():
    s=text_input.get()
    if '-' in s:
        text_input.set('Cannot be determined!')
    elif '.' in s:
        s=float(s)
        s=math.sqrt(s)
        text_input.set(s)
    else:
        s=int(s)
        s=math.sqrt(s)
        text_input.set(s)

#power
power=Button(root,text='Pow',bg='#0f0c29',fg='white',font=("Arial",12,"bold"),command=lambda : num('^'))
power.place(x=100,y=200)
CreateToolTip(power,"Find x to the power y \n For example: 2^3=8")


def calpow(s):
    a=s.split('^')
    a=[int(i) for i in a ]
    a,b=a
    c=math.pow(a,b)
    text_input.set(c)


#log
loog=Button(root,text='Log',bg='#0f0c29',fg='white',font=("Arial",12,"bold"),command=lambda : logg())
loog.place(x=170,y=200)
CreateToolTip(loog,"Given a value. \n Enter log button")

def logg():
    s=text_input.get()
    if '-' in s:
        text_input.set("cann't be determined")
    elif '.' in s:
        text_input.set("cann't be determined")
    else:
        a=s.split(',')
        a=[int(i) for i in a ]
        a,b=a
        text_input.set(str(math.log(a,b)))

#sin
sine=Button(root,text='Sin',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : sinn())
sine.place(x=240,y=200)
CreateToolTip(sine,"Enter a value. \n click sin button")

def sinn():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    s=math.sin(s)
    s=str(s)
    text_input.set(s)

#cos
cosine=Button(root,text='Cos',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : coss())
cosine.place(x=310,y=200)
CreateToolTip(cosine,"Enter a value. \n click cos button")

def coss():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    s=math.cos(s)
    s=str(s)
    text_input.set(s)

#tan
tangent=Button(root,text='tan',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : tann())
tangent.place(x=380,y=200)
CreateToolTip(tangent,"Enter a value. \n click tan button")


def tann():
    s = text_input.get()
    if '.' in s:
        s = float(s)
    else:
        s = int(s)

    s = math.tan(s)
    s = str(s)
    text_input.set(s)

#asin
arsin=Button(root,text='arcsin',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : acsin())
arsin.place(x=440,y=200)
CreateToolTip(arsin,"Enter a value. \n click arcsin button")


def acsin():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    if s>= -1 and s <= 1:
        s=math.asin(s)
        s=str(s)
        text_input.set(s)
    else:
        text_input.set("Enter value between -1 to 1.")


#acos
arcos=Button(root,text='arcCos',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : accos())
arcos.place(x=520,y=200)
CreateToolTip(arcos,"Enter a value. \n click arcCos button")


def accos():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    if s>= -1 and s <= 1:
        s=math.acos(s)
        s=str(s)
        text_input.set(s)
    else:
        text_input.set("Enter value between -1 to 1.")


#atan
artan=Button(root,text='arctan',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : actan())
artan.place(x=610,y=200)
CreateToolTip(artan,"Enter a value. \n click arctan button")

def actan():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    if s>=-1 and s<=1:
        s=math.atan(s)
        s=str(s)
        text_input.set(s)
    else:
        text_input.set("Enter value between -1 to 1.")


#e to the power x
ex=Button(root,text='e**x',bg="#edc988",fg="black",font=("Arial",12,"bold"),command=lambda : e())
ex.place(x=690,y=200)
CreateToolTip(ex,"Enter a value.\n find e to the power x")

def e():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    s=math.exp(s)
    global operator
    operator=''
    num(s)

# Degrees
de=Button(root,text='DEG',bg="#edc988",fg="black",font=("Arial",12,"bold"),command=lambda : d())
de.place(x=760,y=200)
CreateToolTip(de,"Find value in degree")


def d():
    s = text_input.get()

    if '.' in s:
        a = float(s)
    else:
        a = int(s)

    k = math.degrees(a)
    text_input.set(str(k))

#gcd between two numbers
gcdd=Button(root,text='Gcd',bg="#edc988",fg="black",font=("Arial",12,"bold"),command=lambda : hcf())
gcdd.place(x=830,y=200)
CreateToolTip(gcdd,"Enter two values.: 12,6 \n click gcd button.\nAns:6")


def hcf():
    s=text_input.get()
    a=s.split(',')

    a=[int(i) for i in a]
    a,b=a
    a=abs(a)
    b=abs(b)
    g=math.gcd(a,b)
    text_input.set(str(g))


#---------------------------2nd line---------------------------------------------------------------------------------

#******lcm
lcmm=Button(root,text='Lcm',bg='#0f0c29',fg='white',font=("Arial",12,"bold"),command=lambda: lc())
lcmm.place(x=30,y=260)
CreateToolTip(lcmm,"Enter two values:2,3. \n Click lcm button.\nAns:6")

def lc():
    s=text_input.get()
    a=s.split(',')

    a=[int(i) for i in a]
    a,b=a
    a=abs(a)
    b=abs(b)
    l=a*b//math.gcd(a,b)
    text_input.set(str(l))


#*****************bracket (**************
fb=Button(root,text='   (    ',bg='#0f0c29',fg='white',font=("Arial",12,"bold"),command=lambda: num('('))
fb.place(x=100,y=260)

#*************bracket )****************
lb=Button(root,text='   )    ',bg='#0f0c29',fg='white',font=("Arial",12,"bold"),command=lambda: num(')'))
lb.place(x=170,y=260)

#----------------pi----------------
pai=Button(root,text=' PI ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : pie())
pai.place(x=240,y=260)
CreateToolTip(pai,"3.1416..........")

def pie():
    num(math.pi)

#---------------factorial------------
fact=Button(root,text='  X!  ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : f(text_input.get()))
fact.place(x=310,y=260)
CreateToolTip(fact,"Find factorial")

def f(a):
    if '.' in a:
        text_input.set("factorial Cann't be determined float values!")
    elif '-' in a:
        text_input.set("factorial Cann't determined negative value!")
    else:
        s=math.factorial(int(a))
        text_input.set(str(s))


#-------------------,--------------
coma=Button(root,text='  ,  ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : num(','))
coma.place(x=380,y=260)
CreateToolTip(coma,"Use for comma. ,")

#-----------------------e--------------
fe=Button(root,text='  e  ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : ie())
fe.place(x=450,y=260)
CreateToolTip(fe,"e=2.71------")

def ie():
    num(math.e)

#----------------radians-------------------
r=Button(root,text='RAD',bg="#d7385e",fg="white",font=("Arial",12,"bold"),command=lambda : ra())
r.place(x=520,y=260)
CreateToolTip(r,"Find value in radian")


def ra():
    s = text_input.get()

    if '.' in s:
        a = float(s)
    else:
        a = int(s)

    k = math.radians(a)
    text_input.set(str(k))


#-------------BIN,OCT,HEX,DEC----------------
b=Button(root,text='BIN',bg="#edc988",fg="black",font=("Arial",12,"bold"),command=lambda: bi())
b.place(x=590,y=260)
CreateToolTip(b,"Drcimal to Binary")


def bi():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    s=str(bin(s))
    text_input.set(s)

o=Button(root,text='OCT',bg="#edc988",fg="black",font=("Arial",12,"bold"),command=lambda: oc())
o.place(x=660,y=260)
CreateToolTip(o,"Decimal to Octal")

def oc():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    s=str(oct(s))
    text_input.set(s)

h=Button(root,text='HEX',bg="#edc988",fg="black",font=("Arial",12,"bold"),command=lambda: hx())
h.place(x=730,y=260)
CreateToolTip(h,"Decimal to Hexadecimal")

def hx():
    s=text_input.get()
    if '.' in s:
        s=float(s)
    else:
        s=int(s)
    s=str(hex(s))
    text_input.set(s)

dc=Button(root,text='DEC',bg="#edc988",fg="black",font=("Arial",12,"bold"),width=6,command=lambda: open())
dc.place(x=810,y=260)
CreateToolTip(dc,"Convert any number system into Decimal")


# -----------------------------Decimal converter----------------------
def open():
    global fr
    input_text = StringVar()
    top = Toplevel(bg="#ffe1a8")
    top.title("Decimal converter")
    top.iconbitmap("img.ico")
    top.geometry('600x450')
    top.resizable(False, False)
    # ---------------------------frame
    frame1 = Frame(top, bg='#ffe1a8')
    frame1.place(x=110, y=10)

    frame2 = Frame(top, bg='#ffe1a8')
    frame2.place(x=170, y=180)

    # -----------------------first label
    flabel = Label(frame1, text="Decimal Converter", font=('tahoma', 20, 'bold'), bg="#ffe1a8", fg='#e26d5c')
    flabel.grid(row=0, column=0)
    enter = Entry(frame1, text=input_text, bd=4, bg='#d7e3fc', width=20, font=ff1).grid(row=1, column=0, padx=10,
                                                                                        pady=10)

    # ------------function--------------------------------
    fb = Button(frame2, text='BIN', font=("Arial", 12, "bold"), bg='#00b4d8', fg='white', command=lambda: findbin())
    fb.grid(row=0, column=0, padx=10, pady=10)
    fh = Button(frame2, text='HEX', font=("Arial", 12, "bold"), bg='#00b4d8', fg='white', command=lambda: findhex())
    fh.grid(row=0, column=1, padx=10, pady=10)
    fo = Button(frame2, text='OCT', font=("Arial", 12, "bold"), bg='#00b4d8', fg='white', command=lambda: findoct())
    fo.grid(row=0, column=2, padx=10, pady=10)

    # ----------------------------------------------------
    fclr = Button(frame2, text='CLR', font=("Arial", 12, "bold"), bg='#00b4d8', fg='white', command=lambda: dlt())
    fclr.grid(row=0, column=4, padx=10, pady=10)
    # -----------------------------------------------------
    fex = Button(frame2, text="EXIT", font=("Arial", 12, "bold"), bg='#00b4d8', fg='white', command=top.destroy)
    fex.grid(row=1, column=1, pady=20, columnspan=3)

    # function
    def findhex():
        s = input_text.get()
        res = int(s, 16)
        res = str(res)
        input_text.set(res)

    def findoct():
        s = input_text.get()
        res = int(s, 8)
        res = str(res)
        input_text.set(res)

    def findbin():
        s = input_text.get()
        res = int(s, 2)
        res = str(res)
        input_text.set(res)

    def dlt():
        input_text.set("")






#--------------------------------1234567890.10^x---------------------------------------------------------------------

#1
one=Button(root,text='1',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda:num(1))
one.place(x=30,y=470)
#2
two=Button(root,text='2',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(2))
two.place(x=100,y=470)
#3
three=Button(root,text='3',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(3))
three.place(x=170,y=470)
#4
four=Button(root,text='4',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(4))
four.place(x=30,y=400)
CreateToolTip(four,"4444444")
#5
five=Button(root,text='5',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(5))
five.place(x=100,y=400)
#6
six=Button(root,text='6',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(6))
six.place(x=170,y=400)
#7
seven=Button(root,text='7',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(7))
seven.place(x=30,y=330)
#8
eight=Button(root,text='8',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(8))
eight.place(x=100,y=330)
#9
nine=Button(root,text='9',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(9))
nine.place(x=170,y=330)
#0
zero=Button(root,text='0',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num(0))
zero.place(x=100,y=540)
#.
dot=Button(root,text='. ',bg='#0f0c29',fg='white',font=("Arial",20,"bold"),command=lambda: num('.'))
dot.place(x=30,y=540)
#10^x
ten=Button(root,text='10^x',bg='#0f0c29',fg='white',font=("Arial",10,"bold"),height='3',command=lambda : num('e'))
ten.place(x=170,y=540)
CreateToolTip(ten,"Use for 10 to the power x.\n1e-3=1*10^-3")

#--------clear--------
dlt=Button(root,text='CLR',bg="#edc988",fg="black",font=("Arial",15,"bold"),command=lambda : btnClr())
dlt.place(x=240,y=330)

def btnClr():
    global operator
    operator = ''
    text_input.set(operator)

#--------Exit---------
ac=Button(root,text=' EX ',bg="#edc988",fg="black",font=("Arial",15,"bold"),command=lambda : exit())
ac.place(x=310,y=330)
CreateToolTip(ac,"Off app")

def exit():
    root.quit()

#-----------(+-x/=)-----------
plus=Button(root,text='    +     ',bg="#edc988",fg="black",font=("Arial",12,"bold"),height='2',command=lambda: num('+'))
plus.place(x=240,y=470)

minus=Button(root,text='    -    ',bg="#edc988",fg="black",font=("Arial",12,"bold"),height='2',command=lambda: num('-'))
minus.place(x=310,y=470)

gun=Button(root,text='    X    ',bg="#edc988",fg="black",font=("Arial",12,"bold"),height='2',command=lambda: num('*'))
gun.place(x=240,y=400)

vag=gun=Button(root,text='    /     ',bg="#edc988",fg="black",font=("Arial",12,"bold"),height='2',command=lambda: num('/'))
vag.place(x=310,y=400)

equal=Button(root,text='            =             ',bg="#edc988",fg="black",font=("Arial",12,"bold"),height=2,command=lambda : calculation())
equal.place(x=240,y=540)




#------------ans------------
flor=Button(root,text='  //  ',bg="#edc988",fg="black",font=("Arial",16,"bold"),command=lambda : num("//"))
flor.place(x=740,y=330)
CreateToolTip(flor,"Same as divison,but 1.7=1")





def areacal():
    areawindow = Toplevel()
    areawindow.title("Area calculation")
    areawindow.geometry('400x600')
    areawindow.resizable(False, False)

    # ---------------Label------------
    dfflvl = Label(areawindow, text='Different Calculation', font=("Arial", 14))
    dfflvl.place(x=100, y=20)

    def selected(event):

        s = clicked.get()
        if s == 'Area':
            s1 = StringVar()
            s2 = StringVar()
            al = Label(areawindow, text='Length:', font=('Arial', 15))
            al.place(x=10, y=120)
            le = Entry(areawindow, text=s1)
            le.place(x=100, y=120)
            # -----width
            aw = Label(areawindow, text='Width:', font=('Arial', 15))
            aw.place(x=10, y=160)
            we = Entry(areawindow, text=s2)
            we.place(x=100, y=160)
            # ----button-------
            btn = Button(areawindow, text="Calculate", font=("Arial", 12), command=lambda: cal())
            btn.place(x=60, y=200)
            # ---------show----
            call = StringVar()
            showl = Label(areawindow, textvariable=call, font=("Tahoma", 15, 'bold'), fg='green')
            showl.place(x=60, y=300)
            ext = Button(areawindow, text='Exit', font=('Arial', 12), command=areawindow.destroy)
            ext.place(x=250, y=200)

            def cal():
                first = s1.get()
                second = s2.get()
                if '.' in first:
                    first = float(first)
                    if '.' in second:
                        second = float(second)
                    else:
                        second = int(second)

                else:
                    first = int(first)
                    if '.' in second:
                        second = float(second)
                    else:
                        second = int(second)
                final = first * second
                final = str(final)
                call.set(final)
                al.after(6000, al.destroy)
                le.after(6000, le.destroy)
                aw.after(6000, aw.destroy)
                we.after(6000, we.destroy)
                btn.after(6000, btn.destroy)
                showl.after(6000, showl.destroy)
                ext.after(6000, ext.destroy)

        elif s == 'Triangle':
            s1 = StringVar()
            s2 = StringVar()
            al = Label(areawindow, text='Land:', font=('Arial', 15))
            al.place(x=10, y=120)
            le = Entry(areawindow, text=s1)
            le.place(x=100, y=120)
            # -----width
            aw = Label(areawindow, text='Height:', font=('Arial', 15))
            aw.place(x=10, y=160)
            we = Entry(areawindow, text=s2)
            we.place(x=100, y=160)
            # ----button-------
            btn = Button(areawindow, text="Calculate", font=("Arial", 12), command=lambda: cal())
            btn.place(x=60, y=200)
            # ---------show----
            call = StringVar()
            showl = Label(areawindow, textvariable=call, font=("Tahoma", 15, 'bold'), fg='green')
            showl.place(x=60, y=300)
            ext = Button(areawindow, text='Exit', font=('Arial', 12), command=areawindow.destroy)
            ext.place(x=250, y=200)

            def cal():
                first = s1.get()
                second = s2.get()
                if '.' in first:
                    first = float(first)
                    if '.' in second:
                        second = float(second)
                    else:
                        second = int(second)

                else:
                    first = int(first)
                    if '.' in second:
                        second = float(second)
                    else:
                        second = int(second)
                final = 0.5 * first * second
                final = str(final)
                call.set(final)
                al.after(6000, al.destroy)
                le.after(6000, le.destroy)
                aw.after(6000, aw.destroy)
                we.after(6000, we.destroy)
                btn.after(6000, btn.destroy)
                showl.after(6000, showl.destroy)
                ext.after(6000, ext.destroy)

        elif s == 'Circle':
            s1 = StringVar()

            al = Label(areawindow, text='Radius:', font=('Arial', 15))
            al.place(x=10, y=120)
            le = Entry(areawindow, text=s1)
            le.place(x=100, y=120)

            # ----button-------
            btn = Button(areawindow, text="Calculate", font=("Arial", 12), command=lambda: cal())
            btn.place(x=60, y=200)
            ext = Button(areawindow, text='Exit', font=('Arial', 12), command=areawindow.destroy)
            ext.place(x=250, y=200)
            # ---------show----
            call = StringVar()
            showl = Label(areawindow, textvariable=call, font=("Tahoma", 15, 'bold'), fg='green')
            showl.place(x=60, y=300)

            def cal():
                first = s1.get()

                if '.' in first:
                    first = float(first)


                else:
                    first = int(first)

                final = math.pi * first * first
                final = str(final)
                call.set(final)
                al.after(6000, al.destroy)
                le.after(6000, le.destroy)

                btn.after(6000, btn.destroy)
                showl.after(6000, showl.destroy)
                ext.after(6000, ext.destroy)
        elif s == 'Farenhite':
            s1 = StringVar()

            al = Label(areawindow, text='F:', font=('Arial', 15))
            al.place(x=10, y=120)
            le = Entry(areawindow, text=s1)
            le.place(x=100, y=120)

            def cal():
                first = s1.get()
                s = combo.get()

                if '.' in first:
                    first = float(first)
                else:
                    first = int(first)
                if 'Celcius' in s:
                    final = (5 * first - 160) / 9
                    final = str(final)
                    call.set(f"Celcius={final} C")
                else:
                    final = (5 * first + 2297) / 9
                    final = str(final)
                    call.set(f"Kelvin={final} K")

                    # ----button-------

            a = ['Celcius', 'Kelvin']
            combo = ttk.Combobox(areawindow, values=a)
            combo.place(x=60, y=200)
            combo.current(0)
            btn = Button(areawindow, text="Calculate", font=("Arial", 12), command=lambda: cal())
            btn.place(x=60, y=300)
            ext = Button(areawindow, text='Exit', font=('Arial', 12), command=areawindow.destroy)
            ext.place(x=300, y=300)
            # ---------show----
            call = StringVar()
            showl = Label(areawindow, textvariable=call, font=("Tahoma", 15, 'bold'), fg='green')
            showl.place(x=60, y=350)
        elif s == 'Celcius':
            s1 = StringVar()

            al = Label(areawindow, text='C:', font=('Arial', 15))
            al.place(x=10, y=120)
            le = Entry(areawindow, text=s1)
            le.place(x=100, y=120)

            def cal():
                first = s1.get()
                s = combo.get()

                if '.' in first:
                    first = float(first)
                else:
                    first = int(first)
                if 'Farenhite' in s:
                    final = (9 * first + 160) / 5
                    final = str(final)
                    call.set(f"Farenhite={final} F")
                else:
                    final = first + 273
                    final = str(final)
                    call.set(f"Kelvin={final} K")

            a = ['Farenhite', 'Kelvin']
            combo = ttk.Combobox(areawindow, values=a)
            combo.place(x=60, y=200)
            combo.current(0)
            btn = Button(areawindow, text="Calculate", font=("Arial", 12), command=lambda: cal())
            btn.place(x=60, y=300)
            ext = Button(areawindow, text='Exit', font=('Arial', 12), command=areawindow.destroy)
            ext.place(x=300, y=300)
            # ---------show----
            call = StringVar()
            showl = Label(areawindow, textvariable=call, font=("Tahoma", 15, 'bold'), fg='green')
            showl.place(x=60, y=350)

        elif s == 'Kelvin':
            s1 = StringVar()

            al = Label(areawindow, text='K:', font=('Arial', 15))
            al.place(x=10, y=120)
            le = Entry(areawindow, text=s1)
            le.place(x=100, y=120)

            def cal():
                first = s1.get()
                s = combo.get()

                if '.' in first:
                    first = float(first)
                else:
                    first = int(first)
                if 'Celcius' in s:
                    final = first - 273
                    final = str(final)
                    call.set(f"Celcius={final} C")
                else:
                    final = (9 * first - 2297) / 5
                    final = str(final)
                    call.set(f"Farenhite={final} F")

                    # ----button-------

            a = ['Celcius', 'Farenhite']
            combo = ttk.Combobox(areawindow, values=a)
            combo.place(x=60, y=200)
            combo.current(0)
            btn = Button(areawindow, text="Calculate", font=("Arial", 12), command=lambda: cal())
            btn.place(x=60, y=300)
            ext = Button(areawindow, text='Exit', font=('Arial', 12), command=areawindow.destroy)
            ext.place(x=300, y=300)
            # ---------show----
            call = StringVar()
            showl = Label(areawindow, textvariable=call, font=("Tahoma", 15, 'bold'), fg='green')
            showl.place(x=60, y=350)

    option = [
        'Area',
        'Triangle',
        'Circle',
        'Farenhite',
        'Celcius',
        'Kelvin'
    ]
    clicked = StringVar()
    clicked.set(option[0])
    drop = OptionMenu(areawindow, clicked, *option, command=selected)
    drop.place(x=150, y=70)

#---------------------Quadratic Equation-------
qe=Button(root,text='ax^2+bx+c=0',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda : equation())
qe.place(x=600,y=330)
CreateToolTip(qe,"ax2 + bx + c = 0, where\na, b and c are real numbers and \na ≠ 0")


def equation():
    s=text_input.get()
    a,b,c=s.split(',')
    a=int(a)
    b=int(b)
    c=int(c)
    d=(b**2)-(4*a*c)
    root1=(-b+cmath.sqrt(d))/(2*a)
    root2=(-b-cmath.sqrt(d))/(2*a) #class complex

    text_input.set(f"root1={root1} and root2={root2}")



#---------------------------sec,cosec,cot-----------
sec=Button(root,text='SEC',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda : sc())
sec.place(x=380,y=330)


def sc():
    s = text_input.get()
    if '.' in s:
        s = float(s)
    else:
        s = int(s)

    s = 1 / (math.cos(s))
    s = str(s)
    text_input.set(s)


cosec=Button(root,text='COSEC',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda : cosc())
cosec.place(x=440,y=330)


def cosc():
    s = text_input.get()
    if '.' in s:
        s = float(s)
    else:
        s = int(s)

    s = 1 / (math.sin(s))
    s = str(s)
    text_input.set(s)


cot=Button(root,text='COT',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda : caught())
cot.place(x=520,y=330)


def caught():
    s = text_input.get()
    if '.' in s:
        s = float(s)
    else:
        s = int(s)

    s = 1 / (math.tan(s))
    s = str(s)
    text_input.set(s)


#-------------------------measures of length------------------
msl=Button(root,text='Unit of length',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda : measure())
msl.place(x=600,y=400)
CreateToolTip(msl,"Find meter,centimeter,millimeter")


def measure():
    txt = StringVar()
    txtc = StringVar()
    n = Toplevel()
    n.title("Measures of length")
    n.iconbitmap("img.ico")
    n.geometry('380x600')
    n.resizable(False, False)
    m = Label(n, text='M:').place(x=80, y=20)
    e = Entry(n, text=txt).place(x=100, y=20)

    cm = Label(n, text='CM:').place(x=70, y=70)
    ce = Entry(n, text=txtc).place(x=100, y=70)

    btn = Button(n, text="M <=> CM", font=("Arial", 12, "bold"), command=lambda: convert())
    btn.place(x=100, y=130)

    def convert():

        if txt.get() != '':
            s = txt.get()
            if '.' in s:
                s = float(s)
            else:
                s = int(s)
            s = 100 * s
            s = str(s)
            txtc.set(s)
        elif txtc.get() != '':
            s = txtc.get()
            if '.' in s:
                s = float(s)
            else:
                s = int(s)
            s = s / 100
            s = str(s)
            txt.set(s)

    # -----------------m to mm----------
    txtm = StringVar()
    txtmm = StringVar()

    m1 = Label(n, text='M:').place(x=80, y=200)
    e1 = Entry(n, text=txtm).place(x=100, y=200)

    mm = Label(n, text='MM:').place(x=70, y=250)
    me = Entry(n, text=txtmm).place(x=100, y=250)

    btn1 = Button(n, text="M <=> mm", font=("Arial", 12, "bold"), command=lambda: convertm())
    btn1.place(x=100, y=300)

    def convertm():
        if txtm.get() != '':
            s = txtm.get()
            if '.' in s:
                s = float(s)
            else:
                s = int(s)
            s = 1000 * s
            s = str(s)
            txtmm.set(s)
        elif txtmm.get() != '':
            s = txtmm.get()
            if '.' in s:
                s = float(s)
            else:
                s = int(s)
            s = s / 1000
            s = str(s)
            txtm.set(s)

    # -----------------cm to mm----------
    txtcm = StringVar()
    tmm = StringVar()

    cm1 = Label(n, text='CM:').place(x=70, y=370)
    cme = Entry(n, text=txtcm).place(x=100, y=370)

    mm1 = Label(n, text='MM:').place(x=70, y=410)
    me1 = Entry(n, text=tmm).place(x=100, y=410)

    btn2 = Button(n, text="CM <=> mm", font=("Arial", 12, "bold"), command=lambda: convertcm())
    btn2.place(x=100, y=460)

    def convertcm():
        if txtcm.get() != '':
            s = txtcm.get()
            if '.' in s:
                s = float(s)
            else:
                s = int(s)
            s = 10 * s
            s = str(s)
            tmm.set(s)
        elif tmm.get() != '':
            s = tmm.get()
            if '.' in s:
                s = float(s)
            else:
                s = int(s)
            s = s / 10
            s = str(s)
            txtcm.set(s)

    btn3 = Button(n, text="Exit", font=("Arial italic", 12, 'bold'), command=n.destroy).place(x=130, y=520)


#-------------------------measures of central tandency----------------
mct=Button(root,text=' Statistics ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda : measurect())
mct.place(x=380,y=400)
CreateToolTip(mct,"Statistics module of python.\nFind mean,median and mode")


def measurect():
    nibo = StringVar()
    window = Toplevel()
    window.title("Statistics")
    window.iconbitmap("img.ico")
    window.geometry('400x400')
    window.resizable(False, False)
    nibol = Label(window, text='Values:', fg="green", font=('Arial', 12)).place(x=20, y=30)
    niboe = Entry(window, text=nibo, font=('Tahoma', 14)).place(x=100, y=30)

    btn = Button(window, text='Calculate', font=('Arial', 10, 'bold'), command=lambda: calculate()).place(x=20, y=80)
    tmean = StringVar()
    tmode = StringVar()
    tmedian = StringVar()
    tmean.set('Mean = 0')
    tmedian.set('Median = 0')
    tmode.set('Mode = 0')
    mean = Label(window, textvariable=tmean, fg="green", font=('Tahoma', 10, 'bold')).place(x=100, y=140)
    median = Label(window, textvariable=tmedian, fg="green", font=('Tahoma', 10, 'bold')).place(x=100, y=170)
    mood = Label(window, textvariable=tmode, fg="green", font=('Tahoma', 10, 'bold')).place(x=100, y=200)

    btn2 = Button(window, text="Exit", font=('Arial italic', 10), command=window.destroy).place(x=300, y=80)

    def calculate():
        s = nibo.get()
        a = s.split(',')
        if '.' in s:
            a = [float(i) for i in a]
            tmean.set(f"Mean = {statistics.fmean(a)}")

        else:
            a = [int(i) for i in a]
            tmean.set(f"Mean = {statistics.mean(a)}")

        tmedian.set(f"Median = {statistics.median(a)}")
        tmode.set(f"Mode = {statistics.multimode(a)}")



#---------------------------Age---------------------------------------
age=Button(root,text='   AGE  ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda : agecal())
age.place(x=500,y=400)
CreateToolTip(age,"Calculate your age")


def agecal():
    newindow = Toplevel()
    newindow.title("Age calculator")
    newindow.iconbitmap("img.ico")
    newindow.geometry('500x500')
    newindow.resizable(False, False)

    # -------------headline---------------
    bhead = Label(newindow, fg='green', text="Age Calculator", font=("Tahoma", 20, 'bold')).place(x=150, y=10)

    # ---------------birthdate------------
    birthd = StringVar()
    birthm = StringVar()
    birthy = StringVar()
    # -----------------------------------
    bdate = Label(newindow, text='Birth date:', font=('Arial', 10)).place(x=14, y=90)
    dcombo = ttk.Combobox(newindow, textvariable=birthd, width=15)
    dcombo.place(x=90, y=90)
    a = []
    for i in range(1, 32):
        a.append(i)

    dcombo.config(values=a)

    bm = Label(newindow, text='Birth Month:', font=('Arial', 10)).place(x=14, y=120)
    mcombo = ttk.Combobox(newindow, textvariable=birthm, width=15)
    mcombo.place(x=90, y=120)
    a = []
    for i in range(1, 13):
        a.append(i)

    mcombo.config(values=a)

    by = Label(newindow, text='Birth Year:', font=('Arial', 10)).place(x=14, y=170)
    ycombo = ttk.Combobox(newindow, textvariable=birthy, width=15)
    ycombo.place(x=90, y=170)
    a = []
    for i in range(1900, (date.today().year) + 1):
        a.append(i)
    ycombo.config(values=a)

    btn = Button(newindow, text="Calculate", font=("Arial", 10), command=lambda: agecalculator())
    btn.place(x=90, y=220)
    txt = StringVar()
    showl = Label(newindow, textvariable=txt, font=('Tahoma', 20), fg='green')
    showl.place(x=80, y=300)

    btn2 = Button(newindow, text='Exit', font=('Arial italic', 10), command=newindow.destroy)
    btn2.place(x=200, y=220)

    def agecalculator():
        dtoday = date.today().day
        mtoday = date.today().month
        ytoday = date.today().year
        day = int(birthd.get())
        month = int(birthm.get())
        year = int(birthy.get())
        dd = mm = yy = 0
        if dtoday < day:
            dtoday += 30
            dd = dtoday - day
            month += 1
            if mtoday < month:
                mtoday += 12
                mm = mtoday - month
                year += 1
                yy = ytoday - year
            else:
                mm = mtoday - month
                yy = ytoday - year
        else:
            dd = dtoday - day
            if mtoday < month:
                mtoday += 12
                mm = mtoday - month
                year += 1
                yy = ytoday - year
            else:
                mm = mtoday - month
                yy = ytoday - year
        showl.config(text=txt.set(f"{yy} years,{mm} months,{dd + 1} days"))


#---------------------------leap--------------------------------------
leapy=Button(root,text='    Leap    ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda: leap())
leapy.place(x=600,y=470)
CreateToolTip(leapy,"Find leap year")


def leap():
    year=text_input.get()
    year=int(year)
    if year%4==0:
        if year%100!=0:
            text_input.set("Leap year.")
        elif year%100==0:
            if year%400!=0:
                text_input.set("Not leap year.")
            else:
                text_input.set("Leap year.")
    else:
        text_input.set("Not leap year.")

#--------------------------weakday-------------------------------------
weakd=Button(root,text='   Weakday  ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda: weak())
weakd.place(x=380,y=470)
CreateToolTip(weakd,"Find weakday from date/month/year")


def weak():
    weakwindow=Toplevel()
    weakwindow.title("Weakday find")
    weakwindow.iconbitmap("img.ico")
    weakwindow.geometry("500x500")
    weakwindow.resizable(False,False)
    #----------------------headline

    weakl=Label(weakwindow,text="Weakday find",fg='green',font=('Arial',14))
    weakl.place(x=200,y=20)
    year=StringVar()
    month=StringVar()
    day=StringVar()
    #----------------year label

    yl=Label(weakwindow,text='Year:',font=('Arial',10,'bold'))
    yl.place(x=10,y=90)
    ye=ttk.Combobox(weakwindow,textvariable=year)
    a=[i for i in range((date.today().year),0,-1)]
    ye.configure(values=a)
    ye.place(x=80,y=90)

    #------------------month
    ml=Label(weakwindow,text='Month:',font=('Arial',10,'bold'))
    ml.place(x=10,y=120)
    me=ttk.Combobox(weakwindow,textvariable=month)
    a=[i for i in range(1,13)]
    me.configure(values=a)
    me.place(x=80,y=120)
    # #----------------day
    dl=Label(weakwindow,text='Day:',font=('Arial',10,'bold'))
    dl.place(x=10,y=150)
    de=ttk.Combobox(weakwindow,textvariable=day)
    a=[i for i in range(1,32)]
    de.configure(values=a)
    de.place(x=80,y=150)

    #-----------------find and exit--------------
    find=Button(weakwindow,text='Find',font=("Tahoma",10),command=lambda : weakfind())
    find.place(x=80,y=200)
    ber=Button(weakwindow,text="Exit",font=('Tahoma',10),command=weakwindow.destroy)
    ber.place(x=130,y=200)

    fweak=StringVar()


    findweak=Label(weakwindow,textvariable=fweak,fg='green',font=("Arial",20,'bold'))
    findweak.place(x=150,y=300)

    def weakfind():
        def findday(k):
            day, month, year = k.split(' ')
            day = int(day)
            month = int(month)
            year = int(year)
            days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATARDAY', 'SUNDAY']
            dn = calendar.weekday(year, month, day)
            return (days[dn])

        y = year.get()
        m = month.get()
        d = day.get()
        k = str(d) + ' ' + str(m) + ' ' + str(y)

        fweak.set(findday(k))


#==========================================PRIME=============================================

prime=Button(root,text='  PRIME ',bg="#d7385e",fg="white",font=("Arial",12,"bold"),height=2,command=lambda: fprime())
prime.place(x=500,y=470)
CreateToolTip(prime,"Check number is prime or not")

def fprime():
    s=text_input.get()
    s=int(s)
    if s>1:
        for i in range(2,s):
            if(s%i)==0:
                text_input.set('Not a prime number.')
                break
        else:
            text_input.set('Prime number.')
    else:
        text_input.set('Not a prime number')


#==========================================Namta=============================================

namta=Button(root,text='Namta',height=13,bg="#edc988",fg="black",font=("Arial",12,'bold'),command=lambda : findnamta())
namta.place(x=820,y=330)
CreateToolTip(namta,"Find namta of given number")


def findnamta():
    namtawindow = Toplevel()
    namtawindow.title("Namta")
    namtawindow.geometry("400x500")
    namtawindow.resizable(False, False)

    # -------------label-----------
    namtalabel = Label(namtawindow, text="NAMTA", fg="green", font=("Tahoma bold", 10))
    namtalabel.place(x=150, y=10)
    l = StringVar()
    l1 = Label(namtawindow, text="Enter a number:", fg="green", font=("Tahoma", 10, 'bold'))
    l1.place(x=10, y=50)
    e1 = Entry(namtawindow, textvariable=l)
    e1.place(x=130, y=50)
    btn = Button(namtawindow, text="Show", font=("Arial", 10), command=lambda: sw())
    btn.place(x=10, y=100)
    rst = Button(namtawindow, text="RESET", font=("Arial", 10), command=lambda: reset())
    rst.place(x=150, y=100)
    ext = Button(namtawindow, text="Exit", font=("Arial", 10), command=namtawindow.destroy)
    ext.place(x=300, y=100)


    t = Text(namtawindow, width=30, height=40, font=("Tahoma", 10, 'bold'), fg='green')
    t.place(x=10, y=140)

    def reset():
        t.delete('1.0', "end")

    def sw():
        s = l.get()
        s = int(s)
        for i in range(1, 11):
            t.insert(INSERT, f"{s} x {i} = {s * i} \n\n")



#==========================================DIU Waiver=============================================

zero=Button(root,text='DIU WAIVER',bg='#d7385e',fg='white',font=("Arial",12,"bold"),height=2,command=lambda: persent())
zero.place(x=690,y=470)

def persent():
    s=text_input.get()
    a,b=s.split(",")
    a = int(a)
    b = int(b)
    final=b/100
    solve=final*a
    #solve=str(solve)
    solve2=a-solve
    #solve2=str(solve2)
    text_input.set(f"Waiver={solve} and Payable={solve2}")


#===================================mainloop================================
root.mainloop()

