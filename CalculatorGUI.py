from tkinter import *
import tkinter as tk

num = ""
total = None
storeOpp = None


def btn(inputNum):
    global num
    num = num + str(inputNum)
    displayNum.set(num)

def opperation(opp):
    global total
    global num
    global storeOpp

    if total == None:
        total = int(num)

    elif storeOpp == 0:
        total = total + int(num)

    elif storeOpp == 1:
        total = total - int(num)

    elif storeOpp == 2:
        total = total * int(num)

    elif storeOpp == 3:
        total = total / int(num)

    num = ""
    storeOpp = opp


        
def clear():
    global num
    num = ""
    displayNum.set("")

def answer():
    global total
    global num
    global storeOpp

    if storeOpp == 0:
        total = total + int(num)
    elif storeOpp == 1:
        total = total - int(num)
    elif storeOpp == 2:
        total = total * int(num)
    elif storeOpp == 3:
        total = total / int(num)

    displayNum.set(str(total))
    total = None
    num = ""
    storeOpp = None



root = tk.Tk()
root.title("Calculator.py")
root.configure(background="darkgrey")
root.geometry("360x400")

displayNum = StringVar()

displayEntry = Entry(root, textvariable=displayNum)
displayEntry.grid(columnspan=4, ipadx=70)

btnOne = Button(root, text="1", command=lambda: btn(1), width = 6)
btnOne.grid(row = 2, column= 0, pady= 5)

btnTwo = Button(root, text="2", command=lambda: btn(2), width = 6)
btnTwo.grid(row = 2, column= 1, pady= 5)

btnThree = Button(root, text="3", command=lambda: btn(3), width = 6)
btnThree.grid(row = 2, column= 2, pady= 5)

btnFour = Button(root, text="4", command=lambda: btn(4), width = 6)
btnFour.grid(row = 3, column= 0, pady= 5)

btnFive = Button(root, text="5", command=lambda: btn(5), width = 6)
btnFive.grid(row = 3, column= 1, pady= 5)

btnSix = Button(root, text="6", command=lambda: btn(6), width = 6)
btnSix.grid(row = 3, column= 2, pady= 5)

btnSeven = Button(root, text="7", command=lambda: btn(7), width = 6)
btnSeven.grid(row = 4, column= 0, pady= 5)

btnEight = Button(root, text="8", command=lambda: btn(8), width = 6)
btnEight.grid(row = 4, column= 1, pady= 5)

btnNine = Button(root, text="9", command=lambda: btn(9), width = 6)
btnNine.grid(row = 4, column= 2, pady= 5)

btnClear = Button(root, text="Clear", command=lambda:clear())
btnClear.grid(row = 5, column= 0, pady= 5)

btnTotal = Button(root, text="Total", command=lambda: answer())
btnTotal.grid(row = 5, column= 2, pady= 5)

btnPlus = Button(root, text="+", command=lambda: opperation(0))
btnPlus.grid(row = 2, column= 4, pady= 5)

btnMinus = Button(root, text="-", command=lambda: opperation(1))
btnMinus.grid(row = 3, column= 4, pady= 5)

btnTimes = Button(root, text="*", command=lambda: opperation(2))
btnTimes.grid(row = 4, column= 4, pady= 5)

btnDivide = Button(root, text="/", command=lambda: opperation(3))
btnDivide.grid(row = 5, column= 4, pady= 5)

root.mainloop()
