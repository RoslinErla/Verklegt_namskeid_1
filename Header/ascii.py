from datetime import datetime
import sys
import os
import time

class Frame:
    def __init__(self): 
        self.get_size_of_screen() # get length of columns and rows of console window
        self.logo = """
_____   __      _____   __         _____        
___  | / /_____ ___  | / /  ______ ___(_)_______
__   |/ /_  __ `/_   |/ /   _  __ `/_  /__  ___/
_  /|  / / /_/ /_  /|  /    / /_/ /_  / _  /    
/_/ |_/  \__,_/ /_/ |_/     \__,_/ /_/  /_/  
"""


    def get_size_of_screen(self):
        if os.name == "nt":
            import shutil
            self.columns, self.rows = shutil.get_terminal_size()
        else:
            self.rows, self.columns = os.popen("stty size", "r").read().split()
    
    def clear_window(self):
        os.system("cls" if os.name == "nt" else "clear")

        #self.delete_last_lines(3) # delete 3 lines to remove the progress bar after it"s finished
    
    def __str__(self):
        """ Print header of application """
        return "{}{}\n\n".format(self.logo,"bold")