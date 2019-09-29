from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("learn Tkinter!")
root.iconbitmap('F:/tutorial/Dapino-Summer-Holiday-Palm-tree.ico')
root.geometry("240x250")

frame1 = LabelFrame(root)
frame1.place(relx=0.016, rely=0.023, height=100, width=100)

my_image = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic7.png"))
myLabel = Label(frame1 ,image=my_image)
myLabel.pack()




button_quit = Button(root,text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
