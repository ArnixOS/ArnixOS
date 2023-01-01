from tkinter import *
from subprocess import check_output
from os import system
from os.path import isfile
from tkinter.messagebox import showerror

self = Tk()
self.title("arnix-byemenu")
self.resizable(False , False)
self.configure(bg="#232a2d")
self.geometry("500x200")

user = check_output("whoami").decode("utf-8")

canvas = Canvas(self , width=500 , height=200 , bg="#232a2d")
canvas.pack()

def lock():
    global lockcmd
    slimpath="/etc/pam.d/slimlock"
    betterlockscreen="/usr/bin/betterlockscreen"
    i3lockpath="/usr/bin/i3lock"
    slockpath="/usr/bin/slock"
    xflockpath="/usr/bin/xflock4"

    slockexists=isfile(slockpath)
    i3lockexists=isfile(i3lockpath)
    betterlockscreenexists=isfile(betterlockscreen)
    slimexists=isfile(slimpath)
    xflockexists=isfile(xflockpath)

    if slockexists==True:
        lockcmd="slock"
    elif i3lockexists==True:
        lockcmd="i3lock"
    elif slimexists==True:
        lockcmd="slimlock"
    elif betterlockscreenexists==True:
        lockcmd="betterlockscreen -l"
    elif xflockexists==True:
        lockcmd="xflock4"
    else:
        showerror('Error' , 'Please open an issue on https://gitlab.com/arnix-os/byemenu to fix this...')
        self.destroy()

lock()

b1 = Button(self , text="" , font=("Iosevka 14") , fg="#dadada" , bg="#232a2d" , activebackground="#e57474" , activeforeground="#232a2d" , command=lambda:system("poweroff") , width=3 , height=2)
b2 = Button(self , text="" , font=("Iosevka 14") , fg="#dadada" , bg="#232a2d" , activebackground="#8ccf7e" , activeforeground="#232a2d" , command=lambda:system("reboot"), width=3, height=2)
b3 = Button(self , text="" , font=("Iosevka 14") , fg="#dadada" , bg="#232a2d" , activebackground="#e5c76b" , activeforeground="#232a2d" , command=lambda:system(f"{lockcmd}"), width=3, height=2)
b4 = Button(self , text="ﴚ" , font=("Iosevka 14") , fg="#dadada" , bg="#232a2d" , activebackground="#67b0e8" , activeforeground="#232a2d" , command=lambda:system(f"pkill -U {user}"), width=3, height=2)
b5 = Button(self , text="" , font=("Iosevka 14") , fg="#dadada" , bg="#232a2d" , activebackground="#c47fd5" , activeforeground="#232a2d" , command=lambda:system("systemctl suspend"), width=3, height=2)

canvas.create_window(250 , 40, window=Label(self , text=f"bye {user}" , font=("Iosevka 12") , fg="#dadada" , bg="#232a2d"))
canvas.create_window(100 , 100, window=b1)
canvas.create_window(175 , 100, window=b2)
canvas.create_window(250 , 100, window=b3)
canvas.create_window(325 , 100, window=b4)
canvas.create_window(400 , 100, window=b5)

self.bind("<Escape>" , lambda event:self.destroy())

self.mainloop()
