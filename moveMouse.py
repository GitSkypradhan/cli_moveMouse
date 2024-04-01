# import pyautogui
# import time
# import random
# from tqdm import tqdm
# import os
# from colorama import init, Fore


# def welcome_message():
#     """Display a colorful welcome message"""
#     clear_screen()
#     init()
#     print(Fore.GREEN + "Welcome to My Awesome Console App!")
#     print()

# def clear_screen():
#     """Clear the console screen"""
#     os.system('cls' if os.name == 'nt' else 'clear')

# def show_progress_bar():
#     """Display a progress bar"""
#     print("\nExiting...")
#     for i in tqdm(range(10)):
#         time.sleep(0.5)

# # Define the main function
# def move_mouse():
#     print("\n\n\nMoveMouse App - Press Ctrl+C to exit")
#     try:
#             while True:
#             # Get current mouse position
#                 scrSize = pyautogui.size()
#                 xcoord = scrSize.width - 100
#                 ycord = scrSize.height - 100
#                 # print(f"The screen Size :{xcoord},{ycord}")

#                 current_pos = pyautogui.position()
#                 print(f"Current mouse position: {current_pos}")
                                    
#                 new_x = random.randrange(0,xcoord)
#                 new_y = random.randrange(0,ycord)
            
#                 # Move the mouse to the new coordinates
#                 pyautogui.moveRel(10,10)
            
#                 # Pause for a moment to let user see the mouse movement
#                 time.sleep(10)
#     except KeyboardInterrupt:
#             show_progress_bar()
#             clear_screen()


# # Call the main function
# if __name__ == "__main__":
#     welcome_message()
#     move_mouse()

import pyautogui
import time
import random
from tqdm import tqdm
import os
from colorama import init, Fore

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    """Display a colorful welcome message with a mouse graphic"""
    clear_screen()
    init()
    print(Fore.GREEN + "Welcome to MoveMouse App!\n")
    print("Press 's' to start moving the mouse.")
    print("Press Ctrl+C to exit.\n")
    print("""
            (`-()_.-=-.
            /66  ,  ,  \\
          =(o_/=//_(   /======`
              ~"` ~"~~`
    """)
 
def exit_message():
    """Display a colorful exit message with a mouse graphic"""
    clear_screen()
    init()
    print(Fore.RED + "Thank You!\n")
    print("""
                "Hey...where's the cheese?"
          o_o /
          (")
         \/'\/
  ____(__(,_,)__________________________________________________________
    """)
def wrong_input_msg():
    print(Fore.RED+"""
                "Oops!...wrong input, Try again."
          o_o /
          (")
         \/'\/
  ____(__(,_,)__________________________________________________________
    """)

 
def show_progress_bar():
    """Display a progress bar"""
    print("\nExiting...")
    for i in tqdm(range(10)):
        time.sleep(0.5)

def loading_bar():
    print(Fore.RED +"\nLoading....")
    for i in tqdm(range((6))):
        time.sleep(0.8)



def move_mouse():
    """Move the mouse randomly"""
    while True:
            # Get screen size
            scr_size = pyautogui.size()
            x_coord = scr_size.width - 100
            y_coord = scr_size.height - 100

            # Get current mouse position
            current_pos = pyautogui.position()
            print(f"Current mouse position: {current_pos}", end="\r")
                                    
            # Generate new random coordinates
            new_x = random.randrange(0, x_coord)
            new_y = random.randrange(0, y_coord)
            
            # Move the mouse to the new coordinates
            pyautogui.moveTo(new_x, new_y)
            
            # Pause for a moment to let user see the mouse movement
            time.sleep(3)

   

# Main function
def main():
    try:
        welcome_message()
        start = input("Press 's' to start moving the mouse: ")
        if start.lower() == 's':
            clear_screen()
            move_mouse()
        else:
            clear_screen()
            wrong_input_msg()
            loading_bar()
            clear_screen()
            main()
    except KeyboardInterrupt:
        show_progress_bar()
        clear_screen()
        exit_message()

if __name__ == "__main__":
    main()
