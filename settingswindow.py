import json
import os
from tkinter import Toplevel, Label, Entry, Button, Checkbutton, OptionMenu

class SettingsWindow:
    def __init__(self, root, discord_webhook_url, discord_id, auto_focus_window, key_for_food, key_for_water):
        self.root = root
        self.discord_url_var = discord_webhook_url
        self.discord_id_var = discord_id
        self.auto_focus_window_var = auto_focus_window
        self.key_for_food_var = key_for_food
        self.key_for_water_var = key_for_water

    def save_settings(self):
        settings_dict = {
            "webhook_url": self.discord_url_var.get(),
            "discord_id": self.discord_id_var.get(), 
            "auto_focus_window": self.auto_focus_window_var.get(), 
            "hotbar_for_water": self.key_for_water_var.get(), 
            "hotbar_for_food": self.key_for_food_var.get()
        }
        with open("settings.json", 'w') as json_file:
            json.dump(settings_dict, json_file)

    def load_settings(self):
        if os.path.exists('settings.json'):
            with open('settings.json') as f:
                global data
                data = json.load(f)
                try:
                    self.discord_id_var.set(data['discord_id'])
                    self.discord_url_var.set(data['webhook_url'])
                    self.auto_focus_window_var.set(data['auto_focus_window'])
                    self.key_for_food_var.set(data["hotbar_for_food"])
                    self.key_for_water_var.set(data["hotbar_for_water"])
                    print('Settings loaded successfully')
                except:
                    print("Failed to load all settings")

    def open_settings_window(self):
        settings_window = Toplevel(self.root)
        options = ['0','1','2','3','4','5','6','7','8','9']
        discord_name_label = Label(settings_window, text="Discord Id")
        discord_name_label.grid(column=0, row=0)
        discord_name_textbox = Entry(settings_window, textvariable=self.discord_id_var, width=150)
        discord_name_textbox.grid(column=1, row=0, columnspan=3)

        discord_url_label = Label(settings_window, text="Discord Webhook Url")
        discord_url_label.grid(column=0, row=1)
        discord_url_textbox = Entry(settings_window, textvariable=self.discord_url_var, width=150)
        discord_url_textbox.grid(column=1, row=1, columnspan=3)

        food_hotbar_label = Label(settings_window, text="Hotbar slot for food: " )
        food_hotbar_label.grid(column=0, row=2)
        food_hotbar_options = OptionMenu(settings_window, self.key_for_food_var, *options)
        food_hotbar_options.grid(column=1, row=2)

        water_hotbar_label = Label(settings_window, text="Hotbar slot for water: " )
        water_hotbar_label.grid(column=0, row=3)
        water_hotbar_options = OptionMenu(settings_window, self.key_for_water_var, *options)
        water_hotbar_options.grid(column=1, row=3)

        auto_focus_window_checkbutton = Checkbutton(settings_window, text="Auto Focus Ark Window on Start", variable=self.auto_focus_window_var, onvalue=1, offvalue=0 )
        auto_focus_window_checkbutton.grid(column=0, row=9, columnspan=2)

        settings_save_button = Button(settings_window, text="Save", command=self.save_settings)
        settings_save_button.grid(column=1, row = 10)