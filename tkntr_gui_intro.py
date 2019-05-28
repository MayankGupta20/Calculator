import tkinter as tk
import tkinter.messagebox as msgbox


mainWindow = tk.Tk()
mainWindow.title=("Calculator")

label_1 =tk.Label(mainWindow,text="Enter First Number ",padx=(10),pady=(20))
label_1.pack()

first_number = tk.Entry(mainWindow)
first_number.pack()

label_2 = tk.Label(mainWindow,text ="Enter Second Number",padx=(10),pady=(20))
label_2.pack()

second_number = tk.Entry(mainWindow)
second_number.pack()


label_3 =tk.Label(mainWindow,text="Operation",padx=(10),pady=(20))
label_3.pack()


def plus():
    try:
        num1,num2 =take_input()
        result = num1+num2
        result_display.config(text="Operation result is "+ str(result))
    except ValueError:
        msgbox.showerror('INVALID INPUT','Enter Only Numeric data')


def sub():
    try:
        num1, num2 = take_input()
        result = num1-num2
        result_display.config(text="Operation result is " + str(result))
    except ValueError:
        msgbox.showerror('INVALID INPUT', 'Enter Only Numeric data')


def mul():
    try:
        num1, num2 = take_input()
        result = round(num1*num2,10)
        result_display.config(text="Operation result is " + str(result))
    except ValueError:
        msgbox.showerror('INVALID INPUT', 'Enter Only Numeric data')


def division():
    try:
        num1, num2 = take_input()
        result = num1 / num2
        result_display.config(text="Operation result is " + str(result))
    except ZeroDivisionError :
        msgbox.showinfo('ERROR','Attempt to Divide by Zero')
    except ValueError :
        msgbox.showerror('INVALID INPUT','Enter Only Numeric value')

def take_input():
    n1 = first_number.get()
    n2 = second_number.get()
    try :
        n1 =float(n1)
        n2 =float(n2)
        return(n1,n2)
    except ValueError:
        msgbox.showerror('INVALID INPUT','Enter Only Numeric Value')
        quit(0)


button_plus = tk.Button(mainWindow,text="  +  ",command = lambda : plus())
button_plus.pack()

button_minus = tk.Button(mainWindow,text="  -  ",command = lambda : sub())
button_minus.pack()

button_mul = tk.Button(mainWindow,text="  *  ",command = lambda : mul())
button_mul.pack()

button_div = tk.Button(mainWindow,text="  /  ",command = lambda : division())
button_div .pack()

result_display = tk.Label(mainWindow,text="Operation result is ",padx=(10),pady=(20))
result_display.pack()



mainWindow.mainloop()







