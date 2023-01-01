from tkinter import *
from subprocess import check_output
from os import system

self = Tk()
self.title("arnix-byemenu")
self.configure(bg="#24283b")
self.resizable(False , False)

x = int((self.winfo_screenwidth() / 2) - (375/ 2))
y = int((self.winfo_screenheight() / 2) - (375/ 2))
self.geometry(f'400x400+{x}+{y}')

user = check_output("whoami").decode('utf-8')
canvas = Canvas(self , width=400 , height=400, bg="#24283b")
canvas.pack()

canvas.create_window(200 , 50, window=Label(self , text=f"bye , {user}" , bg="#24283b" , fg="#c0caf5" , font=("Caskaydia Cove Nerd Font" , 12)))
canvas.create_window(200 , 100, window=Button(self , text="⏻ Shut Down" , font=("Caskaydia Cove Nerd Font" , 12) , bg="#7aa2f7" , fg="#24283b" , command=lambda:system("poweroff") , width=10))
canvas.create_window(200 , 150, window=Button(self , text=" Restart" , font=("Caskaydia Cove Nerd Font" , 12) , bg="#7aa2f7" , fg="#24283b" , command=lambda:system("reboot") , width=10))
canvas.create_window(200 , 200, window=Button(self , text=" Log Out", font=("Caskaydia Cove Nerd Font" , 12) , bg="#7aa2f7" , fg="#24283b" , command=lambda:system(f"pkill -U {user}") , width=10))
canvas.create_window(200 , 250, window=Button(self , text="⏾ Suspend" , font=("Caskaydia Cove Nerd Font" , 12) , bg="#7aa2f7" , fg="#24283b" , command=lambda:system("systemctl suspend") , width=10))
canvas.create_window(200 , 350, window=Button(self , text=" Quit" , font=("Caskaydia Cove Nerd Font" , 12) , bg="#f7768e" , fg="#24283b" , command=lambda:self.destroy() , width=10))

self.mainloop()
