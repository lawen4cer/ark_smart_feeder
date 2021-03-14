import pyautogui
import time, threading
import discord_notifications


class FeedTasks:
    def __init__(self, interval_var, total_feed_var, exit_to_main_var, discord_id, discord_url) -> None:
        self.interval_var = interval_var
        self.total_feed_var = total_feed_var
        self.exit_to_main_var = exit_to_main_var
        self.screen_size = pyautogui.size()
        self.discord = discord_notifications.DiscordNotifications(discord_id, discord_url)
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

    def transfer_item(self):
        print(start_time)
        print(feed_time)
        while time.time() < feed_time:
            failure_count_on_item = 0
            print(self.screen_size)
            raw_meat_in_inventory = pyautogui.locateCenterOnScreen('images/rawmeat.png', confidence = 0.6, region = (0,0,round(self.screen_size[0]/2),self.screen_size[1]))
            if raw_meat_in_inventory == None:
                failure_count_on_item += 1
            print(raw_meat_in_inventory)
            if raw_meat_in_inventory != None:
                pyautogui.click(raw_meat_in_inventory.x, raw_meat_in_inventory.y)
                time.sleep(1)
                pyautogui.press('t')
                time.sleep(1)
            if failure_count_on_item > 0:
                self.discord.send_webhook_for_image_notfound_error()
            WAIT_TIME_SECONDS = int(self.interval_var.get()) * 60
            ticker = threading.Event()
            while not ticker.wait(WAIT_TIME_SECONDS):
                self.transfer_item()


        print(self.exit_to_main_var)
        if self.exit_to_main_var.get() == 1:
            self.exit_to_main_menu()
        print("Done with transfers")

    def start_transfer_thread(self):
        print("t thread started")
        global start_time 
        start_time = time.time()
        timeout = self.total_feed_var.get()
        global feed_time 
        feed_time = start_time + (timeout * 60)
        t = threading.Thread(target=self.transfer_item)
        t.daemon = True
        t.start()