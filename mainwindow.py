from tkinter import Label, Button, Checkbutton, Entry
import settingswindow
import feedtasks

class MainWindow:

    def __init__(self, root,interval_var, total_feed_var, exit_to_main_var, discord_id, discord_url):
        self.root = root
        self.total_feed_var = total_feed_var
        self.interval_var = interval_var
        self.exit_to_main_var = exit_to_main_var
        self.settings_window = settingswindow.SettingsWindow(root, discord_url, discord_id)
        self.feedtasks = feedtasks.FeedTasks(interval_var, total_feed_var, exit_to_main_var, discord_id, discord_url)
        self.settings_window.load_settings()

    def build_root_window(self):
        interval_label = Label(self.root, text="Feed Interval(Minutes)")
        interval_label.grid(column=0, row=2)
        interval_textbox = Entry(self.root, textvariable=self.interval_var)
        interval_textbox.grid(column=1, row=2, columnspan=2)


        app_timer_label = Label(self.root, text="How long to feed in total(Minutes)")
        app_timer_label.grid(column=0, row=1)
        app_timer_textbox = Entry(self.root, textvariable=self.total_feed_var)
        app_timer_textbox.grid(column=1, row=1, columnspan=2)

        exit_to_main_checkbutton = Checkbutton(self.root, text="Exit to Main Menu when finished", variable=self.exit_to_main_var, onvalue=1, offvalue=0 )
        exit_to_main_checkbutton.grid(column=0, row=9, columnspan=2)

        start_button = Button(self.root, text="Start", command=self.feedtasks.start_transfer_thread)
        start_button.grid(column=1, row=10)

        open_settings_button = Button(self.root, text="Settings", command=self.settings_window.open_settings_window)
        open_settings_button.grid(column=0, row=10)