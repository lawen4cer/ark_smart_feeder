import pyautogui
import os
import time, threading
import json
from tkinter import *
from discord_webhook import DiscordWebhook, DiscordEmbed
data = {}
def load_settings():
    if os.path.exists('settings.json'):
        with open('settings.json') as f:
            global data
            data = json.load(f)

screen_size = pyautogui.size()
root = Tk()
root.geometry('400x400+{0}+{1}'.format((int(screen_size[0]/2) - 200), (int(screen_size[1]/2) - 200)))
root.title("Ark Smart Feeder")

total_feed_var = IntVar()
interval_var = IntVar()
exit_to_main_var = IntVar()
discord_id_var = StringVar()
discord_url_var = StringVar()
start_time = 0.0
feed_time = 0.0

def load_settings():
    if os.path.exists('settings.json'):
        with open('settings.json') as f:
            global data
            data = json.load(f)
            discord_id_var.set(data['discord_id'])
            discord_url_var.set(data['webhook_url'])
            print('Settings loaded successfully')

#function area
def exit_to_main_menu():
    pyautogui.press('esc')
    exit_button_coords = pyautogui.locateCenterOnScreen('images/exittomenu.png', confidence = 0.5)
    print(exit_button_coords)
    print("outside loop")
    while exit_button_coords == None:
        pyautogui.press('esc')
        time.sleep(1)
        exit_button_coords = pyautogui.locateCenterOnScreen('images/exittomenu.png', confidence = 0.5)
        print(exit_button_coords)
        print('inside loop')
    pyautogui.click(exit_button_coords.x, exit_button_coords.y)

def transfer_item():
    print(start_time)
    print(feed_time)
    while time.time() < feed_time:
        failure_count_on_item = 0
        print(screen_size)
        raw_meat_in_inventory = pyautogui.locateCenterOnScreen('images/rawmeat.png', confidence = 0.6, region = (0,0,round(screen_size[0]/2),screen_size[1]))
        if raw_meat_in_inventory == None:
            failure_count_on_item += 1
        print(raw_meat_in_inventory)
        if raw_meat_in_inventory != None:
            pyautogui.click(raw_meat_in_inventory.x, raw_meat_in_inventory.y)
            time.sleep(1)
            pyautogui.press('t')
            time.sleep(1)
        if failure_count_on_item > 0:
            send_webhook_for_image_notfound_error()
        WAIT_TIME_SECONDS = int(interval_var.get()) * 60
        ticker = threading.Event()
        while not ticker.wait(WAIT_TIME_SECONDS):
            transfer_item()


    print(exit_to_main_var)
    if exit_to_main_var.get() == 1:
        exit_to_main_menu()
    print("Done with transfers")

def start_transfer_thread():
    print("t thread started")
    global start_time 
    start_time = time.time()
    timeout = total_feed_var.get()
    global feed_time 
    feed_time = start_time + (timeout * 60)
    t = threading.Thread(target=transfer_item)
    t.daemon = True
    t.start()

def send_webhook_for_image_notfound_error():
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/820512914887933952/BvLOOoYQfm7Wo_oymWBeOGxZFujrrNXHfyeCjwHcQL2GqVnh167eeApEAadPvH0ZhfSK", content= "<@{0}>".format(discord_id_var.get()))
    embed = DiscordEmbed(title="Ark Smart Feeder", description = "I can't find anything to feed your baby, check your inventory", color= "03b2f8")
    webhook.add_embed(embed)
    response = webhook.execute()

def save_settings():
    settings_dict = {
        "webhook_url": discord_url_var.get(),
        "discord_id": discord_id_var.get()
    }
    with open("settings.json", 'w') as json_file:
        json.dump(settings_dict, json_file)

def open_settings_window():
    settings_window = Toplevel(root)

    discord_name_label = Label(settings_window, text="Discord Id",justify=LEFT, anchor='w')
    discord_name_label.grid(column=0, row=0)
    discord_name_textbox = Entry(settings_window, textvariable=discord_id_var)
    discord_name_textbox.grid(column=1, row=0, columnspan=2)

    discord_url_label = Label(settings_window, text="Discord Webhook Url",justify=LEFT, anchor='w')
    discord_url_label.grid(column=0, row=1)
    discord_url_textbox = Entry(settings_window, textvariable=discord_url_var)
    discord_url_textbox.grid(column=1, row=1, columnspan=2)

    settings_save_button = Button(settings_window, text="Save", command=save_settings)
    settings_save_button.grid(column=1, row = 10)        
 

#script area


load_settings()



interval_label = Label(root, text="Feed Interval(Minutes)",justify=LEFT, anchor='w')
interval_label.grid(column=0, row=2)
interval_textbox = Entry(root, textvariable=interval_var)
interval_textbox.grid(column=1, row=2, columnspan=2)


app_timer_label = Label(root, text="How long to feed in total(Minutes)",justify=LEFT,anchor='w')
app_timer_label.grid(column=0, row=1)
app_timer_textbox = Entry(root, textvariable=total_feed_var)
app_timer_textbox.grid(column=1, row=1, columnspan=2)

exit_to_main_checkbutton = Checkbutton(root, text="Exit to Main Menu when finished", variable=exit_to_main_var, onvalue=1, offvalue=0 )
exit_to_main_checkbutton.grid(column=0, row=9, columnspan=2)

start_button = Button(root, text="Start", command=start_transfer_thread)
start_button.grid(column=1, row=10)

open_settings_button = Button(root, text="Settings", command=open_settings_window)
open_settings_button.grid(column=0, row=10)


    

root.mainloop()




    
    




