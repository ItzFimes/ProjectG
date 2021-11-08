__author__ = "ItzFimes"



try:
    import subprocess
except:
    print("\033[91m {}\033[00m".format("You don't have required modules to run this program"))
    print("\033[91m {}\033[00m".format("Subprocess missing"))
    print("\033[93m {}\033[00m".format("To repair this go to COMMAND PROMPT(cmd) and type pip install subprocess"))
    input("Press enter to exit")
    exit()
try:
    import pydrive
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive 
    from google import auth 
    from oauth2client.client import GoogleCredentials
except:
    print("PyDrive not found")
    print("Installing")
    subprocess.call["gengine\Installers\pydriveinstall.bat"]
    input("Press enter to restart and apply changes")
    exit()
try:
    import os
except:
    print("OS not found")
    print("Installing")
    subprocess.call["gengine\Installers\osinstall.bat"]
    input("Press enter to restart and apply changes")
    exit()
try:
    import pyautogui
except:
    print("\033[91m {}\033[00m".format("PyAutoGui missing"))
    print("\033[92m {}\033[00m".format("Installing"))
    subprocess.call["genginge\Installers\pyautoguiinstall.bat"]
    input("Press enter to restart and apply chnges")
    exit()
try:
    import tkinter
    from tkinter import *
    from tkinter import messagebox
    
except:
        print("\033[91m {}\033[00m".format("404 Tkinter not found"))
        subprocess.call[r"gengine\Installers\tkinstall.bat"]

l = Tk()

screen_width = l.winfo_screenwidth()
screen_height = l.winfo_screenheight()
str_screen_height = str(screen_height)
str_screen_width = str(screen_width)
print(str_screen_height)
print(str_screen_width)
print(type(str_screen_height))
print(type(str_screen_width))

l.geometry(str_screen_width + "x" + str_screen_height)
l.config(background="#222222")
l.title("G-Engine")
l.iconbitmap("gengine\Logos\Logo_that_one_that_you_cant_see_in_fullscreen.ico")

loading_logo = PhotoImage(file = "gengine\Logos\Logo-destine.png")
Label1 = Label(l, wraplength = 230, fg="white",image=loading_logo,borderwidth=0,compound="center",highlightthickness = 0,padx=0,pady=0)
Label1.place(relx=0.5,rely=0.5, anchor="c")





import requests

print('Checking version')

url = 'https://raw.githubusercontent.com/ItzFimes/ProjectG/main/test.txt'
try:
    r = requests.get(url)
except:
    print("Error 11001 No conection")
try:    
    if r.content == b"69":
        print("Version is up to date")
        print(r.content)
except:
    print("No internet")

filename = url.split('/')[-1] # this will take only -1 splitted part of the url
print(filename)

f = open("gengine\ver.dat", "r+")
ver = f.read()


if  r.content == ver:
    print("'Version is up to date")
if r.content != ver:
    print("New version avivable would you like to download it?")
    print("Y/N")
    yndownload = input()
    if yndownload == "Y":
        print("Downloading")
        

 

l.mainloop()