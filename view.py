from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('250x200')

def clicked():

   label['text'] ="hee"

        

btn1 = Button(window, text= "Click Here !!!",command=clicked)

btn1.grid(column=1, row=0)

lower_frame = Frame(window, bg= '#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=('Courier', 30)) # ไว้แสดงข้อความบน lower_frame
label.place(relwidth=1, relheight=1)
label['text'] ="kuy"

window.mainloop()