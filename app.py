import os
from tkinter import PhotoImage, Tk, IntVar, StringVar, Button
import json
import pyautogui    
import mainwindow


#initial setup
root = Tk()
screen_size = pyautogui.size()
root.geometry('500x500+{0}+{1}'.format((int(screen_size[0]/2) - 200), (int(screen_size[1]/2) - 200)))
root.title("Ark Smart Feeder")
root.iconbitmap('images/giga.ico')

#global vars
total_feed_var = IntVar()
interval_var = IntVar()
stacks_var = IntVar()
exit_to_main_var = IntVar()
auto_focus_window_var = IntVar()
key_for_food = StringVar()
key_for_water = StringVar()
discord_id_var = StringVar()
discord_url_var = StringVar()
food_type_selected_var = StringVar()
food_type_image_uri_var = StringVar()
run_var = IntVar()
status_var = StringVar()
time_remaining = IntVar()
start_time = 0.0
transfer_food_time = 0.0
character_replenish_time = 0.0
data = {}

mainwindow = mainwindow.MainWindow(root, run_var, status_var, interval_var, total_feed_var, exit_to_main_var, discord_id_var, discord_url_var, auto_focus_window_var, key_for_food, key_for_water,food_type_selected_var,food_type_image_uri_var, time_remaining, stacks_var)
mainwindow.build_root_window()
root.mainloop()





    





    
    




