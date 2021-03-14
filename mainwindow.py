from tkinter import Frame, Label, Button, Checkbutton, Entry, OptionMenu
from tkinter.constants import DISABLED, NORMAL
import settingswindow
import feedtasks

class MainWindow:

    def __init__(self, root, run_var, status_var, interval_var, total_feed_var, exit_to_main_var, discord_id, discord_url, auto_focus_window, key_for_food, key_for_water, food_type, food_image_uri, time_remaining, stacks_var):
        self.root = root
        self.total_feed_var = total_feed_var
        self.interval_var = interval_var
        self.exit_to_main_var = exit_to_main_var
        self.status_var = status_var
        self.food_type_var = food_type
        self.time_remaining_var = time_remaining
        self.stacks_var = stacks_var
        self.settings_window = settingswindow.SettingsWindow(root, discord_url, discord_id, auto_focus_window, key_for_food, key_for_water)
        self.feedtasks = feedtasks.FeedTasks(run_var, status_var, interval_var, total_feed_var, exit_to_main_var, discord_id, discord_url, auto_focus_window, key_for_food, key_for_water, food_type, food_image_uri, time_remaining, stacks_var)
        self.settings_window.load_settings()

    def build_root_window(self):
        food_options = ["Raw Meat", "Cooked Prime Meat"]

        interval_label = Label(self.root, text="Feed Interval(Minutes)")
        interval_label.grid(column=0, row=2)
        interval_textbox = Entry(self.root, textvariable=self.interval_var)
        interval_textbox.grid(column=1, row=2, columnspan=2)


        app_timer_label = Label(self.root, text="How long to feed in total(Minutes)")
        app_timer_label.grid(column=0, row=1)
        app_timer_textbox = Entry(self.root, textvariable=self.total_feed_var)
        app_timer_textbox.grid(column=1, row=1, columnspan=2)

        stacks_label = Label(self.root, text="How many stacks to transfer per feed interval?")
        stacks_label.grid(column=0, row=3)
        stacks_textbox = Entry(self.root, textvariable=self.stacks_var)
        stacks_textbox.grid(column=1, row=3, columnspan=2)

        food_type_label = Label(self.root, text="What are you using for food? ")
        food_type_label.grid(column=0, row=8)

        food_type_optionmenu = OptionMenu(self.root, self.food_type_var, *food_options)
        food_type_optionmenu.grid(column=1, row=8)

        exit_to_main_checkbutton = Checkbutton(self.root, text="Exit to Main Menu when finished", variable=self.exit_to_main_var, onvalue=1, offvalue=0 )
        exit_to_main_checkbutton.grid(column=0, row=9, columnspan=2)

        status_label = Label(self.root, textvariable=self.status_var)
        status_label.grid(column=3, row=10)

        start_button = Button(self.root, text="Start", command=self.feedtasks.start_transfer_thread)
        start_button.grid(column=1, row=10)

        stop_button = Button(self.root, text="Stop", command=self.feedtasks.stop_transfer_thread)
        stop_button.grid(column=2, row=10)

        open_settings_button = Button(self.root, text="Settings", command=self.settings_window.open_settings_window)
        open_settings_button.grid(column=0, row=10)

        data_container = Frame(self.root)
        data_container.grid(columnspan=3, row=20)

        time_remaining_label = Label(data_container, text="Time remaining = ")
        time_remaining_label.grid(column=0, row=0)

        time_remaining_data_label = Label(data_container, textvariable=self.time_remaining_var)
        time_remaining_data_label.grid(column=1, row=0)

        