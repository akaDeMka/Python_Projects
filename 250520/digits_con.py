import os 
from datetime import datetime
#import time
import tkinter
import watch

root=tkinter.Tk()
while True:
    os.system('cls' if os.name == 'nt' else 'clear') 
    watch.print_watch(int(datetime.now().hour),int(datetime.now().minute),int(datetime.now().second))
    print('To exit press Ctrl+C buttons')
    root.after(100)
    #time.sleep(0.1)