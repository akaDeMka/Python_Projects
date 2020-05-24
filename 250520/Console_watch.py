import os 
from datetime import datetime
#import time
import tkinter
import watch

def main():
    root=tkinter.Tk()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        date=datetime.now()
        watch.print_watch(date.hour, date.minute, date.second)
        print('To exit press Ctrl+C buttons')
        root.after(100)
        #time.sleep(0.1)

if __name__ == "__main__":
    main()