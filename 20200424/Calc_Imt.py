from decimal import Decimal                                 #Импортируем для нормальных расчетов с дробными числами
user_weight=input("Введите ваш вес, кг: ")
user_height=input("Введите ваш рост, см: ")
try:                                                        #Исключае некорректно введенные денные
    user_height=Decimal(user_height)/100                    
    user_weight=Decimal(user_weight)
except: 
    print("Вы ввели неверные значения параметров тела")
    exit()
imt=user_weight/(user_height*user_height)                   #Расчеты
imt=imt.quantize(Decimal("1.00"))
print("Ваш индекс тела -",imt)
print("Схема")
imt=int(imt)
print('0 '+(imt-1)*'-'+'|'+(100-imt)*'-'+' 100')            #Вывод строки качества :)