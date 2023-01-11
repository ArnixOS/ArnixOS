from tkinter import Text , Label , Button , Tk , Frame
import config

root = Tk()
root.title("acalc")
root.configure(bg=config.bg)

main = Text(root , width=45 , height=10 , state="disabled" , bg=config.bg , fg=config.fg , insertbackground=config.fg)
main.pack()

f1 = Frame(root , width=45 , height=50 , bg=config.bg)
f1.pack()

EtButton = Button(f1 , text="Enter" , bg=config.numbers , fg=config.bg , highlightthickness=0)
EtButton.pack(in_=f1 , side="right")

entry = Text(width=35 , height=1 , bg=config.bg , fg=config.fg , insertbackground=config.fg , highlightthickness=0)
entry.pack(in_=f1 , side='left')

if __name__ == "__main__":
    root.mainloop()
