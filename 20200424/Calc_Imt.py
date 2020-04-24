from decimal import Decimal                                 #Импортируем для нормальных расчетов с дробными числами
imt_list = [
    [16, 'выраженный дефицит массы тела'],
    [18, 'недостаточная (дефицит) масса тела'],
    [25, 'норма'],
    [30, 'избыточная масса тела (предожирение)'],
    [35, 'ожирение'],
    [40, 'ожирение резкое'],
    [41, 'очень резкое ожирение']
]
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
imt=int(imt.quantize(Decimal("1")))                         #Округление и приведение типов
print('0 '+(imt-1)*'-'+'|'+(100-imt)*'-'+' 100')  
key=0          #Вывод строки качества :)
while imt>imt_list[key][0]:                                 #Вывод интерпритации индекса массы тела
    key +=1
else:
    print('У вас ',imt_list[key][1])
