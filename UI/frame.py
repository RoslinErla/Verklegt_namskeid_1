from datetime import datetime
import sys
import os
import time

class Frame:
    def __init__(self): 
        #self.clearing() # get length of columns and rows of console window
        self.logo = """
 _____   __      _____   __         _____        
___  | / /_____ ___  | / /  ______ ___(_)_______
__   |/ /_  __ `/_   |/ /   _  __ `/_  /__  ___/
_  /|  / / /_/ /_  /|  /    / /_/ /_  / _  /    
/_/ |_/  \__,_/ /_/ |_/     \__,_/ /_/  /_/    
"""

    #def window(self):
        #self.rows, self.columns = os.popen("stty size", "r").read().split()

    #def delete_line(self, n=1):
        #for _ in range(n):
            #sys.stdout.write("\x1b[1A")
            #sys.stdout.write("\x1b[2K")
        #print("{}\n\n\n".format(self.logo)
    def clear_all(self):
        os.system("cls" if os.name == "nt" else "clear")
<<<<<<< HEAD
        print("{}\n\n\n".format(self.logo))
=======
        print("{}\n\n\n".format(self.logo))
    
    def __str__(self):
        return "{}\n\n\n".format(self.logo)
>>>>>>> 31d8db78b4244928e356b1db6f7b65429a37c57c
