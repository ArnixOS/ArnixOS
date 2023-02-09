from PIL import Image , ImageTk , UnidentifiedImageError
from tkinter import Label , Tk , Entry , Button , Frame
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror , showinfo
from os import chdir, getlogin 
from os.path import isfile
from requests import get    
from requests.exceptions import MissingSchema , ConnectionError
from mimes import mimes
                 
root = Tk()
root.title("arnix-imgview")
root.configure(bg="#24283b")

default_history = f"/home/{getlogin()}/.arnix_imgview_history"
hist_exists = isfile(default_history)

if hist_exists == True:
    hist = open(default_history, 'w')
    pass
else:
    hist = open(default_history, 'w')
    pass

imageopened = []

imagerender = False
startuo = Label(root , text="\n \n Welcome to arnix-imgview \n \n Press Ctrl+O to Open File \n Press Ctrl+Shift+O to open Web Image \n \n" , font=("CaskaydiaCove Nerd Font Mono" , 10) , fg="#c0caf5" , bg="#24283b")
startuo.pack(side="bottom")
VERSION = "helix-pb-beta"
fileopen = False
webimage = False

def imageopen(event):
    global image , img , imagerender , file , fileopen , orgimagew , origimageh
    startuo.pack_forget()
    file = askopenfilename(multiple=True , filetypes=mimes)

    for f in file:
        try:
            img = Image.open(f) 
        except UnidentifiedImageError: 
            showerror("Error" , f"Cannot identify {f}")
            break

        imageopened.append(file)

        fileopen = True

        image = ImageTk.PhotoImage(img)
        root.title(f"{f} - arnix-imgview")     

        origimageh = image.height()
        orgimagew = image.width()

        if image.height() and image.width() > root.winfo_screenheight() and root.winfo_screenwidth():
            img.thumbnail((root.winfo_screenheight() , root.winfo_screenwidth()))
            image = ImageTk.PhotoImage(img)
        else:
            pass

        if imagerender == False:
            imagerender = Label(image=image)
            imagerender.pack(side="bottom")
        else:
            imagerender.configure(image=image)

def url_render(filename: str):
    startuo.pack_forget()
    global image , img , imagerender
    img = Image.open(filename)
    image = ImageTk.PhotoImage(img)
    if image.height() and image.width() > root.winfo_screenheight() and root.winfo_screenwidth():
        img.thumbnail((root.winfo_screenheight() , root.winfo_screenwidth()))
        image = ImageTk.PhotoImage(img)
    else:
        pass
    
    if imagerender == False:
        imagerender = Label(image=image)
        imagerender.pack(side="bottom")
    else:
        imagerender.configure(image=image)
    
def open_from_url(url: str):
    global webimage
    startuo.pack_forget()

    chdir("/tmp")
    try:
        contents = get(url)
    except MissingSchema:
        showerror("Error" , "No URL detected")
    except ConnectionResetError:
        showerror("Error" , "Image downloading failed")
    except ConnectionError:
        showerror("Error" , "No internet")
    else:
        webimage = True
        urla = list(url)
        imageopened.append(url)

        if urla[len(urla)-1] == "g" and urla[len(urla)-2] == "n" and urla[len(urla)-3] == "p":
            image = open('image.png' , "wb")
            image.write(contents.content)
            url_render("image.png")
            root.title(f"{url} - arnix-imgview")
            imagefr.pack_forget()
        elif urla[len(urla)-1] == "g" and urla[len(urla)-2] == "p" and urla[len(urla)-3] == "j":
            image = open('image.jpg' , "wb")
            image.write(contents.content)
            url_render("image.jpg")
            root.title(f"{url} - arnix-imgview")
            imagefr.pack_forget()
        elif urla[len(urla)-1] == "b" and urla[len(urla)-2] == "m" and urla[len(urla)-3] == "p":
            image = open('image.bmp' , "wb")
            image.write(contents.content)
            url_render("image.bmp")
            root.title(f"{url} - arnix-imgview")
            imagefr.pack_forget()
        elif urla[len(urla)-1] == "o" and urla[len(urla)-2] == "c" and urla[len(urla)-3] == "i":
            image = open('image.ico' , "wb")
            image.write(contents.content)
            url_render("image.ico")
            root.title(f"{url} - arnix-imgview")
            imagefr.pack_forget()
        elif urla[len(urla)-1] == "g" and urla[len(urla)-2] == "e" and urla[len(urla)-3] == "p" and urla[len(urla)-4] == "j":
            image = open('image.jpeg' , "wb")
            image.write(contents.content)
            url_render("image.jpeg")
            root.title(f"{url} - arnix-imgview")
            imagefr.pack_forget()
        else:
            showerror("Error" , "WebOpen does not support your file extension. Please report this issue on https://github.com/ArnixOS/ArnixOS")

def urlimage_dialog(event):
    global imagefr , getbton , et
    imagefr = Frame(root , width=root.winfo_width() , height=20 , bg="#24283b")

    et = Entry(root , insertbackground="#c0caf5" , fg="#c0caf5" , bg="#24283b")
    getbton = Button(root , text="Preview:-" , bg="#24283b"  , fg="#c0caf5", command=lambda:open_from_url(et.get()) , font=("CaskaydiaCove Nerd Font" , 7))

    Label(text="URL:- " , bg="#24283b" , fg="#c0caf5" , font=("CaskaydiaCove Nerd Font" , 8)).pack(in_=imagefr , side="left")
    et.pack(in_=imagefr , side="left")
    getbton.pack(in_=imagefr , side="right")

    imagefr.pack(side="top")

def about_f(event):
    abdiag = Tk()
    abdiag.title("About arnix-imgview")
    abdiag.configure(bg="#24283b")
    Label(abdiag , text="\n arnix-imgview" , font=("CaskaydiaCove Nerd Font" , 12 , 'bold') , fg="#c0caf5" , bg="#24283b").pack()
    Label(abdiag , text=f"\n {VERSION} \n" , font=("CaskaydiaCove Nerd Font" , 12 ) , fg="#c0caf5" , bg="#24283b").pack()
    Label(abdiag , text="This is not meant to use for production "  , font=("CaskaydiaCove Nerd Font" , 8) , fg="#c0caf5" , bg="#24283b").pack()
    abdiag.mainloop()

def rotate(angle: float):
    global img , image ,  imagerender
    if imagerender==False:
        showerror("Error" , "No image found")
    else:
        img = img.rotate(angle , expand=True)
        image = ImageTk.PhotoImage(img)
        imagerender.configure(image=image)

def save():
    if fileopen == True:
        img.thumbnail((origimageh , orgimagew))
        img.save(file[0])
    elif webimage == True:
        showinfo("Info" , "WebImages are not saved as of 0.1")
    else:
        pass

def write_history():
    hist.write(str(imageopened))
    hist.close()
    exit()

root.bind("<Control-o>" ,imageopen)
root.bind("<Control-a>" , about_f)
root.bind("<Control-r>" , lambda event:rotate(90))
root.bind("<Control-Shift-O>" , urlimage_dialog)
root.bind("<Control-s>" , lambda event:save())

if __name__ == "__main__":
    root.protocol("WM_DELETE_WINDOW", write_history)
    root.mainloop()
