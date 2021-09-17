from tkinter import *


def Deposit():
    dep = Toplevel(window)
    dep.geometry("600x600")
    dep.resizable(0,0)
    dep.title("Deposit Window")
    dep.grab_set()

    titleL = Label(window, text="BMI Calculator", font="Tahoma")
    titleL.place(x=250, y=40)

    resE = Entry(dep, bd = 3, textvariable = myresult)
    resE.place(x=250, y=310)

def new_window():
    new_win = Toplevel(window)
    new_win.geometry("600x600")
    new_win.resizable(0,0)
    new_win.title("New Window")
    new_win.grab_set()

def compute():
    hf = float( hfE.get() )
    hi = float ( hiE.get() )
    wkg = float ( wkgE.get() )
    hm = ( (hf*30.48)+(hi*2.54) ) /100
    bmi = wkg/(hm*hm)
    result.set( round(bmi,2) ) # assigning bmi value to result variable

def clear():
    result.set("")
    hf_txtvar.set("")
    hi_txtvar.set("")
    wkg_txtvar.set("")

window = Tk()
window.geometry("800x600")
window.resizable(0,0)
window.title("ATM Program")


#Text Variables Declaration
result = StringVar()
hf_txtvar = StringVar()
hi_txtvar = StringVar()
wkg_txtvar = StringVar()
myresult = StringVar()

titleL = Label(window, text="ATM Program", font="Tahoma")
titleL.place(x=350,y=10)

titleL = Label(window, text="BMI Calculator", font="Tahoma")
titleL.place(x=350,y=40)

hfL = Label(window,text="Height in feet:", font="Tahoma")
hfL.place(x=150, y=100)

hfE = Entry(window, bd=3, textvariable = hf_txtvar)
hfE.place(x=300,y=100)

hiL = Label(window,text="Height in inches:", font="Tahoma")
hiL.place(x=130, y=150)

hiE = Entry(window, bd=3, textvariable = hi_txtvar)
hiE.place(x=300,y=150)

wkgL = Label(window,text="Weight in kilogram:", font="Tahoma")
wkgL.place(x=106, y=200)

wkgE = Entry(window, bd=3, textvariable = wkg_txtvar)
wkgE.place(x=300,y=200)

calc = Button(window, text="Calculate", width=8, command = compute )
calc.place(x=290, y=250)

clear = Button(window, text="Clear", width=8, command = clear )
clear.place(x=370, y=250)

bmiE = Entry(window, bd=3, textvariable = result)
bmiE.place(x=300,y=300)

open = Button(window, text="Open New Window", width=15, command = Deposit)
open.place(x=305, y=450)

window.mainloop()
