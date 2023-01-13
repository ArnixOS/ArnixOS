from PIL import Image , ImageTk , UnidentifiedImageError
from tkinter import Label , Tk , Scrollbar 
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from os import chdir
from requests import get

root = Tk()
root.title("arnix-imgview")

imagerender = False

def imageopen(event):
    global image , img , imagerender
    file = askopenfilename(multiple=True)

    for f in file:
        try:
            img = Image.open(f) 
        except UnidentifiedImageError: 
            showerror("Error" , f"Cannot identify {f}")
            break

        root.title(f"{f} - arnix-imgview")        
        image = ImageTk.PhotoImage(img)
        if imagerender == False:
            imagerender = Label(image=image)
            imagerender.pack()
        else:
            imagerender.configure(image=image)

def url_render(filename: str):
    global image , img , imagerender
    img = Image.open(filename)
    image = ImageTk.PhotoImage(img)
    if imagerender == True:
        imagerender.configure(image=image)
    else:
        imagerender = Label(image=image)
        imagerender.pack()
    

def open_from_url(url: str):
    chdir("/tmp")
    try:
        contents = get(url)
    except ConnectionResetError:
        askopenfilename("Error" , "Image downloading failed")

    urla = list(url)

    if urla[len(urla)-1] == "g" and urla[len(urla)-2] == "n" and urla[len(urla)-3] == "p":
        image = open('image.png' , "wb")
        image.write(contents.content)
        url_render("image.png")
    elif urla[len(urla)-1] == "g" and urla[len(urla)-2] == "p" and urla[len(urla)-3] == "j":
        image = open('image.jpg' , "wb")
        image.write(contents.content)
        url_render("image.jpg")
    elif urla[len(urla)-1] == "b" and urla[len(urla)-2] == "m" and urla[len(urla)-3] == "p":
        image = open('image.bmp' , "wb")
        image.write(contents.content)
        url_render("image.bmp")
    elif urla[len(urla)-1] == "o" and urla[len(urla)-2] == "c" and urla[len(urla)-3] == "i":
        image = open('image.ico' , "wb")
        image.write(contents.content)
        url_render("image.ico")
    elif urla[len(urla)-1] == "g" and urla[len(urla)-2] == "e" and urla[len(urla)-3] == "p" and urla[len(urla)-4] == "j":
        image = open('image.jpeg' , "wb")
        image.write(contents.content)
        url_render("image.jpeg")
    else:
        showerror("Error" , "WebOpen does not support your file extension. Please report this issue on https://github.com/ArnixOS/ArnixOS")

root.bind("<Control-o>" , imageopen)

if __name__ == "__main__":
    root.mainloop()
