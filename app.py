import pyautogui
import time, threading
from tkinter import *
root = Tk()

total_feed_var = IntVar()
interval_var = IntVar()
exit_to_main_var = IntVar()
start_time = 0.0
feed_time = 0.0

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
        screen_size = pyautogui.size()
        print(screen_size)
        raw_meat_in_inventory = pyautogui.locateCenterOnScreen('images/rawmeat.png', confidence = 0.6, region = (0,0,round(screen_size[0]/2),screen_size[1]))
        if raw_meat_in_inventory == None:
            failure_count_on_item += 1
        print(raw_meat_in_inventory)
        if raw_meat_in_inventory != None:
            pyautogui.click(raw_meat_in_inventory.x, raw_meat_in_inventory.y)
        time.sleep(3)
        pyautogui.press('t')
        time.sleep(1)

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
    
    


    

#script area




interval_label = Label(root, text="Feed Interval(Minutes)")
interval_label.grid(column=0, row=2)
interval_textbox = Entry(root, textvariable=interval_var)
interval_textbox.grid(column=1, row=2, columnspan=2)


app_timer_label = Label(root, text="How long to feed in total(Minutes)")
app_timer_label.grid(column=0, row=1)
app_timer_textbox = Entry(root, textvariable=total_feed_var)
app_timer_textbox.grid(column=1, row=1, columnspan=2)


exit_to_main_checkbutton = Checkbutton(root, text="Exit to Main Menu", variable=exit_to_main_var, onvalue=1, offvalue=0 )
exit_to_main_checkbutton.grid(column=1, row=3)

start_button = Button(root, text="Start", command=start_transfer_thread)
start_button.grid(column=1, row=10)


    

root.mainloop()




    
    




