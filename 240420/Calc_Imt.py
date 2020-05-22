from decimal import Decimal                                                                 #Импортируем для нормальных расчетов с дробными числами
import os                                                                                   #Подключаем для очистки экрана терминала
imt_list = [                                                                                #Расшифровка ИМТ
    [16, 'выраженный дефицит массы тела'],
    [18, 'недостаточная (дефицит) масса тела'],
    [25, 'норма'],
    [30, 'избыточная масса тела (предожирение)'],
    [35, 'ожирение'],
    [40, 'ожирение резкое'],
    [100, 'очень резкое ожирение']
]
key_cup='y'
while key_cup!='n' and key_cup!='т':                                                        #вводим тело программы в цикл до тех пор пока не введут т или n
    os.system('cls' if os.name == 'nt' else 'clear')                                        #очищаем экран терминала
    user_weight=input("\nВведите ваш вес, кг: ")
    user_height=input("Введите ваш рост, см: ")
    try:                                                                                    #Исключаем некорректно введенные денные
        user_height=Decimal(user_height)/100                    
        user_weight=Decimal(user_weight)
    except: 
        print("\nВы ввели неверные значения параметров тела")
    else:
        imt=user_weight/(user_height*user_height)                                           #Расчеты
        imt=imt.quantize(Decimal("1.00"))
        if imt>100 or imt<0:                                                                #Проверяем что значения не выходят за границы 0-100
            print("\nВам срочно стоит обратится к врачу - ваше состояние не нормальное")  
        else:    
            print("\n    Ваш индекс тела -", imt)
            imt=int(imt.quantize(Decimal("1")))                                             #Округление и приведение типов
            print('\n    0 '+(imt-1)*u'―'+'■'+(100-imt)*'―'+' 100')                         #Вывод Визуальной строки :)
            for key in imt_list:                                                            #Вывод интерпритации индекса массы тела
                if imt<=key[0] :
                    print('\n    У вас',key[1],'\n')
                    break
    key_cup=input("\nПроизвести расчет для новых данных? (Введите 'n' для преращения работы программы) ") 