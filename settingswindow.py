import json
import os
from tkinter import Toplevel, Label, Entry, Button

class SettingsWindow:
    def __init__(self, root, discord_webhook_url, discord_id):
        self.root = root
        self.discord_url_var = discord_webhook_url
        self.discord_id_var = discord_id

    def save_settings(self):
        settings_dict = {
            "webhook_url": self.discord_url_var.get(),
            "discord_id": self.discord_id_var.get()
        }
        with open("settings.json", 'w') as json_file:
            json.dump(settings_dict, json_file)

    def load_settings(self):
        if os.path.exists('settings.json'):
            with open('settings.json') as f:
                global data
                data = json.load(f)
                self.discord_id_var.set(data['discord_id'])
                self.discord_url_var.set(data['webhook_url'])
                print('Settings loaded successfully')

    def open_settings_window(self):
        settings_window = Toplevel(self.root)

        discord_name_label = Label(settings_window, text="Discord Id")
        discord_name_label.grid(column=0, row=0)
        discord_name_textbox = Entry(settings_window, textvariable=self.discord_id_var)
        discord_name_textbox.grid(column=1, row=0, columnspan=2)

        discord_url_label = Label(settings_window, text="Discord Webhook Url")
        discord_url_label.grid(column=0, row=1)
        discord_url_textbox = Entry(settings_window, textvariable=self.discord_url_var)
        discord_url_textbox.grid(column=1, row=1, columnspan=2)

        settings_save_button = Button(settings_window, text="Save", command=self.save_settings)
        settings_save_button.grid(column=1, row = 10)