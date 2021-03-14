from tkinter.constants import DISABLED
import pyautogui
from tkinter import messagebox, Button
import time, threading
import discord_notifications
import pygetwindow
from math import floor

class FeedTasks:

    

    def __init__(self, run_var, status_var, interval_var, total_feed_var, exit_to_main_var, discord_id, discord_url, auto_focus_window, key_for_food, key_for_water, food_type, food_image_uri, time_remaining, stacks_var) -> None:
        self.interval_var = interval_var
        self.total_feed_var = total_feed_var
        self.exit_to_main_var = exit_to_main_var
        self.auto_focus_window = auto_focus_window
        self.key_for_food_var = key_for_food
        self.key_for_water_var = key_for_water
        self.status_var = status_var
        self.run_var = run_var
        self.food_type_var = food_type
        self.food_image_uri = food_image_uri
        self.time_remaining_var = time_remaining
        self.stacks_var = stacks_var
        self.character_replenish_minutes = 60
        self.failure_count_on_item = 0
        self.screen_size = pyautogui.size()
        self.discord = discord_notifications.DiscordNotifications(discord_id, discord_url)

    def set_food_image_uri(self):
        if self.food_type_var.get() == "Raw Meat":
            self.food_image_uri.set("images/rawmeat.png")
        if self.food_type_var.get() == "Cooked Prime Meat":
            self.food_image_uri.set("images/cookedprimemeat.png")
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

    def find_and_move_item(self):
        raw_meat_in_inventory = pyautogui.locateCenterOnScreen(self.food_image_uri.get(), confidence = 0.6, region = (0,0,round(self.screen_size[0]/2),self.screen_size[1]))
        if raw_meat_in_inventory == None:
            self.failure_count_on_item += 1
        print(raw_meat_in_inventory)
        if raw_meat_in_inventory != None:
            pyautogui.click(raw_meat_in_inventory.x, raw_meat_in_inventory.y)
            time.sleep(1)
            pyautogui.press('t')
            time.sleep(1)
            self.failure_count_on_item = 0

    def transfer_item(self):
        global start_time
        print("Start time: {}".format(start_time))
        global transfer_food_time 
        print("Transfer time: {0}".format(transfer_food_time))
        global character_replenish_time
        print("Replenish time: {0}".format(character_replenish_time))

        while time.time() < transfer_food_time and self.run_var.get() == 1:
            self.time_remaining_var.set(floor((transfer_food_time - time.time()) / 60))
            try:
                if self.auto_focus_window.get() == 1:
                    self.win = pygetwindow.getWindowsWithTitle('Ark: Survival Evolved')[0]
                    self.win.activate()
            except:
                messagebox.showerror(title="Error", message="You must have Ark running before clicking start")
                break
            
            print(self.screen_size)
            time.sleep(0.5)
            
            for i in range(self.stacks_var.get()):
                self.find_and_move_item()

            if time.time() > character_replenish_time:
                pyautogui.press('{0}'.format(self.key_for_food_var.get()))
                time.sleep(0.5)
                pyautogui.press('{0}'.format(self.key_for_water_var.get()))
                print("character replenished")
                character_replenish_time = time.time() + (self.character_replenish_minutes * 60)
            if self.failure_count_on_item > self.stacks_var.get():
                self.discord.send_webhook_for_image_notfound_error()
                break
            WAIT_TIME_SECONDS = int(self.interval_var.get()) * 60
            ticker = threading.Event()
            while not ticker.wait(WAIT_TIME_SECONDS) and self.run_var.get() == 1:
                self.transfer_item()


        print(self.exit_to_main_var.get())
        if self.exit_to_main_var.get() == 1 and self.run_var.get() == 1:
            self.exit_to_main_menu()
        print("Done with transfers")
        self.run_var.set(0)
        self.status_var.set("Not Active...")
        self.time_remaining_var.set(0)

    def start_transfer_thread(self):
        self.run_var.set(1)
        self.status_var.set("Active...")
        self.set_food_image_uri()
        time.sleep(2)
        print("t thread started")
        global start_time
        start_time = time.time()
        timeout = self.total_feed_var.get()
        global transfer_food_time 
        transfer_food_time = start_time + (timeout * 60)
        global character_replenish_time
        character_replenish_time = start_time + (self.character_replenish_minutes * 60)
        t = threading.Thread(target=self.transfer_item)
        t.daemon = True
        t.start()

    def stop_transfer_thread(self):
        self.status_var.set("Not Active...")
        self.run_var.set(0)
        self.time_remaining_var.set(0)