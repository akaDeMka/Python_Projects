import os
key_cup='y'
while key_cup!='n' and key_cup!='т':
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("Необходимо ввести 3 int числа")
    a = input("Введи 1 число: ")
    b = input("Введи 2 число: ")
    c = input("Введи 3 число: ")
    try:
        a,b,c=int(a),int(b),int(c)
    except: print ("Вы ввели не int!")
    else:
        if (a != 0) and (b != 0) and (c != 0):                          #Если нет ни ондого нуля - вывести: "Нет нулевых значений!!!"
            print("Нет нулевых значений!!!")

        if a!=0:                                                        #Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" (цикл не использовать)
            print("Первое ненулевое значениа - а = ",a)
        elif b!=0:
            print("Первое ненулевое значениа - b = ",b)
        elif c!=0:
            print("Первое ненулевое значениа - c = ",c)
        else: 
            print("Введены все нули!")
    
        if a>b+c:                                                       #Если первое значение больше чем сумма второго и третьего вывести a - b - c
            print("a - b - c = ",a-b-c)
        elif a<b+c:                                                     #Если первое значение меньше чем сумма второго и третьего вывести b + c - a
            print("b + c - a = ",b+c-a)
    
        if a>50 and (b>a or c>a):                                       #Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
            print("Вася")
    
        if a>5 or b==c==7:                                              #Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"
            print("Петя")

    key_cup=input("\nПроизвести расчет для новых данных? (Введите 'n' для преращения работы программы) ")