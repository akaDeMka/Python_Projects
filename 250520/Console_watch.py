import os 
from datetime import datetime
#import time
import tkinter
import watch

def main():
    root=tkinter.Tk()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        watch.print_watch(datetime.now().hour, datetime.now().minute, datetime.now().second)
        print('To exit press Ctrl+C buttons')
        root.after(100)
        #time.sleep(0.1)

if __name__ == "__main__":
    main()