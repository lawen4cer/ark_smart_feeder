import os
from tkinter import Tk, IntVar, StringVar
import json
import pyautogui    
import mainwindow


#initial setup
root = Tk()
screen_size = pyautogui.size()
root.geometry('400x400+{0}+{1}'.format((int(screen_size[0]/2) - 200), (int(screen_size[1]/2) - 200)))
root.title("Ark Smart Feeder")

#global vars
total_feed_var = IntVar()
interval_var = IntVar()
exit_to_main_var = IntVar()
discord_id_var = StringVar()
discord_url_var = StringVar()
start_time = 0.0
feed_time = 0.0
data = {}

mainwindow = mainwindow.MainWindow(root, interval_var, total_feed_var, exit_to_main_var, discord_id_var, discord_url_var)
mainwindow.build_root_window()
root.mainloop()





    





    
    




