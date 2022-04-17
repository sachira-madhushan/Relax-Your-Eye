from tkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
import time
from plyer import notification
import pyautogui
import webbrowser
from threading import Thread
from multiprocessing import Process
import sys

win=Tk()
win.resizable(False,False)
win.title("Relax Your Eye")

# Set the size of the window
win.geometry("700x350")

#Quit the window
def quit_window(icon, item):
	sys.exit()
	icon.stop()
	win.destroy()

#Show the window again
def show_window(icon, item):
	icon.stop()
	win.after(0,win.deiconify())
	sys.exit()

#Run the tray icon
def iconRun(icon):
    icon.run()

#Show notification loop  
def loop():
    while True:
    	time.sleep(5)
    	send_notification()

# Hide the window and show on the system taskbar
def hide_window():
   win.withdraw()
   image=Image.open("eye.png")
   menu=(item('Show The Program', show_window),item('Quit The Program', quit_window))
   icon=pystray.Icon("name", image, "Relax Your Eye", menu)

   #Run these two functions same time
   p1 = Thread(target = iconRun,args=(icon,))
   p2 = Thread(target = loop)
   p1.start()
   p2.start()
   p1.join()
   p2.join()

#Set notidication
def send_notification():
	notification.notify(title = "Time To Relax Your Eye",message="Plz Follow The 20-20-20 Rule.It Will Care Your Eyes.",timeout=2)

#How to use url
def howToUse():
	webbrowser.open('https://github.com/sachira-madhushan/Relax-Your-Eye/', new=2)

#About me url
def me():
	webbrowser.open('https://github.com/sachira-madhushan/', new=2)

#GUI Area
force = IntVar()
argent = IntVar()
img = PhotoImage(file = r"G:\Python Projects\EYE\eye.png") 
img1 = img.subsample(2, 2)
Label(win, image = img1).grid(row = 0, column = 0,columnspan = 2, rowspan = 3, padx = 5, pady = 5)

c1 = Button(win, text ="start", command = hide_window)
c2 = Button(win, text ="How To Use", command = howToUse)
c3 = Button(win, text ="About Me", command = me)
L=Label(win,text="   D  e  v  e  l  o  p  e  d     B y     S  a  c  h  i  r  a     M  a  d  h  u  s  h  a  n   ",bg="aqua")
c1.grid(row = 0, column = 2, sticky = W, pady = 2)
c2.grid(row = 2, column = 2, sticky = W, pady = 2)
c3.grid(row = 1, column = 2, sticky = W, pady = 2)
L.grid(row = 3, column = 0, sticky = W, pady = 2,columnspan=3)
#GUI End


win.protocol('WM_DELETE_WINDOW', hide_window)
win.mainloop()


