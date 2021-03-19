from tkinter import *
from PIL import ImageGrab
import pyautogui
from pynput import mouse
def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'


def on_click(x, y, button, pressed):
    global root,rgbLabel,hexLabel,rgbButton,hexButton
    if button == mouse.Button.right:
        pixel = ImageGrab.grab().load()
        root.geometry(f"100x120+{x}+{y}")
        pxl = pixel[x,y]
        hexcolor = rgbtohex(pxl[0],pxl[1],pxl[2])
        root.configure(bg=hexcolor)
        rgbLabel.config(text = str(pxl))
        hexLabel.config(text = str(hexcolor))
        rgbLabel.pack()
        hexLabel.pack()
def copy_rgb():
    global root,rgbLabel,hexLabel,rgbButton,hexButton
    root.clipboard_append(rgbLabel.cget('text'))
    #copied to clipboard
def copy_hex():
    global root,rgbLabel,hexLabel,rgbButton,hexButton
    root.clipboard_append(hexLabel.cget('text'))
    #copied to clipboard

def main():
    global root,rgbLabel,hexLabel,rgbButton,hexButton
    root = Tk()
    pos = pyautogui.position()
    pixel = ImageGrab.grab().load()
    root.geometry(f"100x120+{pos.x}+{pos.y}")
    pxl = pixel[pos.x,pos.y]
    hexcolor = rgbtohex(pxl[0],pxl[1],pxl[2])
    root.configure(bg=hexcolor)
    #global rgbButton,rgbLabel,hexLabel,hexButton
    rgbLabel = Label(root, text = str(pxl))
    rgbLabel.pack()

    rgbButton = Button(root,text = "Copy RGB",command = copy_rgb)
    rgbButton.pack()
    hexLabel = Label(root,text = str(hexcolor))
    hexLabel.pack()

    hexButton = Button(root,text = "Copy HEX", command = copy_hex)
    hexButton.pack()
    listener = mouse.Listener(
        on_click = on_click
        )
    listener.start()

    root.mainloop()
main()
