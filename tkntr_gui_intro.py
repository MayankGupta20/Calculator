import tkinter as tk


# mainWindow = tk.Tk()
# mainWindow.title =("Sample Window ")
#
# heading_label=tk.Label(mainWindow,text="Hello World ")
# heading_label.pack()
#
# name_field = tk.Entry(mainWindow)
# name_field.pack()
#
# def takeValueInput():
#     name =name_field.get()
#     print(name)
#
# button = tk.Button(mainWindow,text="Get Value",command = lambda : takeValueInput())
# button.pack()
#
# mainWindow.mainloop()

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
    num1 =int(first_number.get())
    num2 = int(second_number.get())
    #print(num1+num2)
    result = num1+num2
    result_display.config(text="Operation result is "+ str(result))


def sub():
    num1 =int(first_number.get())
    num2 = int(second_number.get())
    #print(num1-num2)
    result = num1-num2
    result_display.config(text="Operation result is " + str(result))


def mul():
    num1 =int(first_number.get())
    num2 = int(second_number.get())
    #print(num1*num2)
    result = num1*num2
    result_display.config(text="Operation result is " + str(result))


def division():
    num1 =int(first_number.get())
    num2 = int(second_number.get())
    #print(num1/num2)
    result = num1/num2
    result_display.config(text="Operation result is " + str(result))


button_plus = tk.Button(mainWindow,text="+",command = lambda : plus())
button_plus.pack()

button_minus = tk.Button(mainWindow,text="-",command = lambda : sub())
button_minus.pack()

button_mul = tk.Button(mainWindow,text="*",command = lambda : mul())
button_mul.pack()

button_div = tk.Button(mainWindow,text="/",command = lambda : division())
button_div .pack()

result_display = tk.Label(mainWindow,text="Operation result is ",padx=(10),pady=(20))
result_display.pack()



mainWindow.mainloop()


