import pyautogui
import time
from tkinter import *



#function area
def exit_to_main_menu():
    pyautogui.press('esc')
    exit_button_coords = pyautogui.locateCenterOnScreen('exittomenu.png', confidence = 0.5)
    print(exit_button_coords)
    print("outside loop")
    while exit_button_coords == None:
        pyautogui.press('esc')
        time.sleep(1)
        exit_button_coords = pyautogui.locateCenterOnScreen('exittomenu.png', confidence = 0.5)
        print(exit_button_coords)
        print('inside loop')
    pyautogui.click(exit_button_coords.x, exit_button_coords.y)

def transfer_items():
    for i in range(4):
        screen_size = pyautogui.size()
        print(screen_size)
        raw_meat_in_inventory = pyautogui.locateCenterOnScreen('rawmeat.png', confidence = 0.6, region = (0,0,round(screen_size[0]/2),screen_size[1]))
        print(raw_meat_in_inventory)
        pyautogui.click(raw_meat_in_inventory.x, raw_meat_in_inventory.y)
        time.sleep(3)
        pyautogui.press('t')
        time.sleep(1)
    print(exit_to_main_var)
    if exit_to_main_var.get() == 1:
        exit_to_main_menu()

time.sleep(6)

#script area
root = Tk()
start_button = Button(root, text="Start", command=transfer_items)
start_button.grid(column=1, row=0)
exit_to_main_var = IntVar()
exit_to_main_checkbutton = Checkbutton(root, text="Exit to Main Menu", variable=exit_to_main_var, onvalue=1, offvalue=0 )
exit_to_main_checkbutton.grid(column=1, row=1)


    

root.mainloop()




    
    




