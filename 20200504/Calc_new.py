from decimal import Decimal                                                                 #Импортируем для нормальных расчетов с дробными числами
import os                                                                                   #Подключаем для очистки экрана терминала
imt_list = [                                                                                #Расшифровка ИМТ
    [16, 'выраженный дефицит массы тела.', 'Пора начинать кушать или боюсь скоро вы окажетесь в больнице! Прекращаем голодать!'],
    [18, 'недостаточная (дефицит) масса тела', 'Питайтесь больше! Все еще недостаточное питание '],
    [25, 'норма', 'Все хорошо! Так держать!'],
    [30, 'избыточная масса тела (предожирение)', 'Пора задуматься о том, что вы едите'],
    [35, 'ожирение', 'Пора урезать рацион. Многовато калорий!'],
    [40, 'ожирение резкое', 'Снижение калорий в 2-3 раза строго рекомендуется!'],
    [100, 'очень резкое ожирение', 'Если вы еще можете ходить - срочно к врачу! Ну и кушаем в основном воду (хлеб отменяется)']
]

def print_users(list):                                      #Процедура для вывода пользователей
    element=len(list)
    for i in range(0,element,1):
        print(i+1,' '+list[i]['ФИО'])

def print_user_config(list_opt):
    print("1. ФИО: ",list_opt['ФИО'])
    print("2. Пол: ",list_opt['Пол'])
    print("3. Возраст: ",list_opt['Возраст'],' лет')
    print("4. Вес: ",list_opt['Вес'],' кг')
    print("5. Рост: ",list_opt['Рост'], ' см')   

def get_user(list):                                         #Функция для выбора пользователя из списка
    print_users(list)
    element=len(list)
    key=input('Введите номер пользователя: ')
    try:
        key=int(key)
    except:
        print('Вы ввели неверное значение')
        return -1
    else:
        if int(key) in range(1,element+1,1):
            return int(key)-1
        else:
            print('Вы ввели неверное значение')
            return -1

key='y'
users=0                                                     #Счетчик, определяющий количество пользователей в базе
while key!='q' and key!='й':                                #тело программы в цикле
    if users:                                               #чтобы окно сразу не очищалось и было видно результат
        key=input("\nДля продолжения введите любую клавишу ")                                 
    os.system('cls' if os.name == 'nt' else 'clear')        #Очистка экрана
    print("Операции:\n")
    print("1. Ввести нового пользователя")
    if users:                                               #блокируем вывод меню, которое недоступно, пока нет пользователей
        print("2. Изменить данные пользователя")
        print("3. Рассчитать ИМТ для пользователя")
        print("4. Вывести список пользователей")
        print("5. Удалить пользователя")
    print("q - Выход")
    key=input("\nЧто еще хотите сделать? (Введите 'q' для выхода из программы): ") 
    os.system('cls' if os.name == 'nt' else 'clear')        #Очистка экрана

    if key=="1":                                            #1. Ввести нового пользователя
        if users:                                          
            user_list.append({ 'ФИО': '', 'Пол': '', 'Возраст':'', 'Вес':'', 'Рост':''})
        else:
            user_list = [{ 'ФИО': '', 'Пол': '', 'Возраст':'', 'Вес':'', 'Рост':''}]

        user_list[users]['ФИО']=input('Создание нового пользователя\nВведите ФИО: ')
        user_list[users]['Пол']=input('Введите Пол (М/Ж): ')
        user_list[users]['Возраст']=input('Введите Возраст, полных лет: ')
        user_list[users]['Вес']=input('Введите Вес, кг: ')
        user_list[users]['Рост']=input('Введите Рост, см: ')
        print('Введенные данные: ',user_list[users])
        users=len(user_list)

    elif key=='2' and users:                                #2. Изменить данные пользователя
        user_got=get_user(user_list)
        if user_got==-1:
            print('Такого пользователя нет')
        else:
            print("Выберите какие данные вы хотите изменить:")
            print_user_config(user_list[user_got])
            print("6. Для выхода введите любую другую клавишу")
            key=input("\nВведите номер записи, которую хотите изменить (Введите 'q' для выхода без изменений): ")
            try:
                key=int(key)
            except:
                print("Вы ввели неверное значение ключа")
                key=22
            else:
                if key==1:
                    user_list[user_got]['ФИО']=input("Введите новые ФИО: ")
                elif key==2:
                    user_list[user_got]['Пол']=input("Новый пол: ")
                elif key==3:
                    user_list[user_got]['Возраст']=input("Актуальный возраст: ")
                elif key==4:
                    user_list[user_got]['Вес']=input("Введите текущий вес: ")
                elif key==5:
                    user_list[user_got]['Рост']=input("Введите текущий рост: ")
                print('Измененные данные: ',user_list[user_got])
                
        
    elif key=='3'and users:                                 #3. Рассчитать ИМТ для пользователя
        user_got=get_user(user_list)
        try:                                                                                #Исключаем некорректно введенные денные
            user_height=Decimal(user_list[user_got]['Рост'])/100                    
            user_weight=Decimal(user_list[user_got]['Вес'])            
        except: 
            print("\nВы ввели неверные значения параметров тела для пользователя")
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
                        print('\n    У вас',key[1],'\n', '    Наш совет: ',key[2])
                        break

    elif key=='4'and users:                                 #4. Вывести список пользователей
        user_got=get_user(user_list)
        if user_got>-1:
            print_user_config(user_list[user_got])
        else:
            print("Такого пользователя нет")                        

    elif key=='5'and users:                                 #5. Удалить пользователя
        user_got=get_user(user_list)
        key=input("\nВы уверены? (y)")
        if key=='y' or key=='н':
            del user_list[user_got]
            print("\nПользователь удален\n\nТекущий список пользователей")
            print_users(user_list)
        else:
            print("\nУдаление отменено")
            key=11
