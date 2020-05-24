import os 
from datetime import datetime
#import time
import tkinter
import watch

def main():
    root=tkinter.Tk()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')        #Clear Terminal
        date=datetime.now()                                     #Take curent time
        watch.print_watch(date.hour, date.minute, date.second)  #print current timne in console
        print('\nTo exit press Ctrl+C buttons')                   
        root.after(100)                                         #delay for 0.1 second
        #time.sleep(0.1)

if __name__ == "__main__":
    main()