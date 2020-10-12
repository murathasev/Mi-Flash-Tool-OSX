from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import os
pencere = Tk()
pencere.title("Mi Flash Tool")
pencere.geometry("900x500")

fontduzeltmesi = font.Font(family='Helvetica', size=15, weight='bold')




def adb():
    messagebox.showinfo("Please wait","ADB Drivers Installing...")
adbb = Button(pencere, text = "Install ADB Drivers",font=fontduzeltmesi, command = adb).pack(side=RIGHT, anchor=NE)


def flash():
    print("ADB Command = fastboot flash x x")
    print(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system('./fastboot flash system_a images/system.img')
    os.system('./fastboot flash vendor_a images/vendor.img')
    os.system('./fastboot flash boot_a images/boot.img')
    os.system('./fastboot flash system_b images/system.img')
    os.system('./fastboot flash vendor_b images/vendor.img')
    os.system('./fastboot flash boot_b images/boot.img')
    os.system('./fastboot flash splash images/splash.img')
    os.system('./fastboot erase userdata')
    os.system('./fastboot flash userdata images/userdata.img')
    os.system('ls -a')
flashb = Button(pencere, text = "Flash",font=fontduzeltmesi, command = flash).pack(side=LEFT,anchor=NW)


def refresh():
    print("Refresh")
    print(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system('./fastboot devices')
    os.system('ls -a')

refreshb = Button(pencere, text = "Refresh", font=fontduzeltmesi, command = refresh).pack(side=LEFT,anchor=NW)



text_box = Text(pencere, bg="#ecf0f1",fg="black",font=fontduzeltmesi, height=1, width=100 ).pack(anchor=NW, pady=4)
flashall = Radiobutton(pencere,font=fontduzeltmesi, text="Flash All").pack(side=BOTTOM, pady=10)




pencere.mainloop()
