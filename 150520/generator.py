import os

def generator(start,stop):    
    while start<=stop:
        if not start%3:
            yield "Василий"
        else:
            yield start
        start+=1

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    first=int(input("Введите начало диапазона - "))
    last = int(input("Введите конец диапазона - "))
    for i in generator(first,last):
        print(i)

if __name__ == "__main__":
    main()