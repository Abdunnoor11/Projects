from tkinter import *
import math

root = Tk()
root.title("Calulator")
root.iconbitmap('F:tutorial\calculator.ico')
root.geometry("315x302+785+301")

display = Text(root, width=40, height=2.5,padx=10, pady=15,background="#f4ffd4", foreground="#000000")
display.place(relx=0.032, rely=0.033, relheight=0.179, relwidth=0.933)

def Clear():
    display.delete(0.0, END)

def click(value):
    display.insert(END, value)

def Equal():
    try:
        ans = display.get(0.0, END)
        display.delete(0.0, END)
        display.insert(END, eval(ans))
    except SyntaxError:
        pass

def square():
    try:
        x = display.get(0.0, END)
        display.delete(0.0, END)
        ans = eval(x)
        display.insert(END, ans*ans)
    except SyntaxError:
        pass

def square_root():
    try:
        x = display.get(0.0, END)
        display.delete(0.0, END)
        ans = math.sqrt(eval(x))
        display.insert(END, ans)
    except SyntaxError:
        pass

def Delete():
    d = display.get(0.0, END)
    display.delete(0.0, END)
    display.insert(END, d[:-2])

btn7 = Button(root, text="7", command=lambda: click(7)).place(relx=0.032, rely=0.265, height=34, width=57)
btn8 = Button(root, text="8", command=lambda: click(8)).place(relx=0.222, rely=0.265, height=34, width=57)
btn9 = Button(root, text="9", command=lambda: click(9)).place(relx=0.413, rely=0.265, height=34, width=57)
btn_mul = Button(root, text="x", command=lambda: click("*")).place(relx=0.603, rely=0.265, height=34, width=57)
btn_div = Button(root, text="/", command=lambda: click("/")).place(relx=0.794, rely=0.265, height=34, width=57)

btn4 = Button(root, text="4", command=lambda: click(4)).place(relx=0.032, rely=0.397, height=34, width=57)
btn5 = Button(root, text="5", command=lambda: click(5)).place(relx=0.222, rely=0.397, height=34, width=57)
btn6 = Button(root, text="6", command=lambda: click(6)).place(relx=0.413, rely=0.397, height=34, width=57)
btn_add = Button(root, text="+", command=lambda: click("+")).place(relx=0.603, rely=0.397, height=34, width=57)
btn_sub = Button(root, text="-", command=lambda: click("-")).place(relx=0.794, rely=0.397, height=34, width=57)

btn1 = Button(root, text="1", command=lambda: click(1)).place(relx=0.032, rely=0.53, height=34, width=57)
btn2 = Button(root, text="2", command=lambda: click(2)).place(relx=0.222, rely=0.53, height=34, width=57)
btn3 = Button(root, text="3", command=lambda: click(3)).place(relx=0.413, rely=0.53, height=34, width=57)
btn_root = Button(root, text="√", command=lambda: square_root()).place(relx=0.603, rely=0.53, height=34, width=57)
btn_square = Button(root, text="x²",command=lambda: square()).place(relx=0.794, rely=0.53, height=34, width=57)

btn_dot = Button(root, text=".", command=lambda: click(".")).place(relx=0.032, rely=0.662, height=34, width=57)
btn_zero = Button(root, text="0", command=lambda: click(0)).place(relx=0.222, rely=0.662, height=34, width=57)
btn_equal = Button(root, text="=", command=lambda: Equal()).place(relx=0.413, rely=0.662, height=34, width=57)
btn_Clear = Button(root, text="Clear", command= lambda:Clear()).place(relx=0.603, rely=0.662, height=34, width=57)
btn_delete = Button(root, text="\u232B", command= lambda: Delete()).place(relx=0.794, rely=0.662, height=34, width=57)

btn_Exit = Button(root, text="Exit", command=root.quit).place(relx=0.032, rely=0.820, height=40, width=297)

root.mainloop()
