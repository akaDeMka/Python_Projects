import os 
from datetime import datetime
import time

digits=[
    ['⬜⬜⬜⬜',
     '⬜⬛⬛⬜',
     '⬜⬛⬛⬜',
     '⬜⬛⬛⬜',
     '⬜⬜⬜⬜',],
    ['⬜⬜⬛⬛',
     '⬛⬜⬛⬛',
     '⬛⬜⬛⬛',
     '⬛⬜⬛⬛',
     '⬜⬜⬜⬛'],
    ['⬜⬜⬜⬜',
     '⬛⬛⬛⬜',
     '⬜⬜⬜⬜',
     '⬜⬛⬛⬛',
     '⬜⬜⬜⬜'],
     ['⬜⬜⬜⬜',
     '⬛⬛⬛⬜',
     '⬜⬜⬜⬜',
     '⬛⬛⬛⬜',
     '⬜⬜⬜⬜'],
    ['⬜⬛⬛⬜',
     '⬜⬛⬛⬜',
     '⬜⬜⬜⬜',
     '⬛⬛⬛⬜',
     '⬛⬛⬛⬜'],
    ['⬜⬜⬜⬜',
     '⬜⬛⬛⬛',
     '⬜⬜⬜⬜',
     '⬛⬛⬛⬜',
     '⬜⬜⬜⬜'],
    ['⬜⬜⬜⬜',
     '⬜⬛⬛⬛',
     '⬜⬜⬜⬜',
     '⬜⬛⬛⬜',
     '⬜⬜⬜⬜'],
    ['⬜⬜⬜⬜',
     '⬛⬛⬛⬜',
     '⬛⬛⬛⬜',
     '⬛⬛⬛⬜',
     '⬛⬛⬛⬜'],
    ['⬜⬜⬜⬜',
     '⬜⬛⬛⬜',
     '⬜⬜⬜⬜',
     '⬜⬛⬛⬜',
     '⬜⬜⬜⬜'],
    ['⬜⬜⬜⬜',
     '⬜⬛⬛⬜',
     '⬜⬜⬜⬜',
     '⬛⬛⬛⬜',
     '⬜⬜⬜⬜'],
]
delimiters=[
    ['⬛⬛⬛',
     '⬛⬛⬛',
     '⬛⬛⬛',
     '⬛⬛⬛',
     '⬛⬛⬛'],
    ['⬛⬛⬛',
     '⬛⬜⬛',
     '⬛⬛⬛',
     '⬛⬜⬛',
     '⬛⬛⬛'],
    ['⬛',
     '⬛',
     '⬛',
     '⬛',
     '⬛'],
]

def print_digits(hours,minutes,seconds):
    global digits,delimiters
    if not seconds%2:
        delim=1
    else:
        delim=0
    if hours>9:
        hour_1=hours//10
    else:
        hour_1=0
    hours=hours%10
    if minutes>9:
        minute_1=minutes//10
    else:
         minute_1=0
    minutes=minutes%10
    if seconds>9:
        second_1=seconds//10
    else:
        second_1=0
    seconds=seconds%10
    for x in range(0,5,1):
        print(digits[hour_1][x]+delimiters[2][x]+digits[hours][x]+delimiters[delim][x]\
        +digits[minute_1][x]+delimiters[2][x]+digits[minutes][x]+delimiters[delim][x]\
        +digits[second_1][x]+delimiters[2][x]+digits[seconds][x])

while True:
    os.system('cls' if os.name == 'nt' else 'clear') 
    print_digits(int(datetime.now().hour),int(datetime.now().minute),int(datetime.now().second))
    print('To exit press Ctrl+C buttons')
    time.sleep(0.1)

