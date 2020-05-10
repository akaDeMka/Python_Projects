from decimal import Decimal                                 #Импортируем для нормальных расчетов с дробными числами
import os                                                   #Модуль для функции очистки экрана терминала
users_database=[{}]                                         #База данных

def print_users():                                          #Процедура для вывода пользователей
    global users_database                                   
    for i in range(0,len(users_database)-1,1):
        print(i+1,' '+users_database[i]['ФИО'])

def print_user_data(list_opt):                              #Вывод информации о пользователе
    print("1. ФИО: ",list_opt['ФИО'])
    print("2. Пол: ",list_opt['Пол'])
    print("3. Возраст: ",list_opt['Возраст'],' лет')
    print("4. Вес: ",list_opt['Вес'],' кг')
    print("5. Рост: ",list_opt['Рост'], ' см')

def get_user():                                             #Функция для выбора пользователя из списка
    global users_database
    print_users()
    while True:
        key=input('Введите номер пользователя: ')
        try:
            key=int(key)
        except:
            print('Вы ввели неверное значение')
        else:
            if int(key) in range(1,len(users_database),1):
                return int(key)-1
                break
            else:
                print('Вы ввели неверное значение')

def get_user_data(user_data,position=0):                    #Вводим данные пользователя
    if not position or position==1:
        user_data['ФИО']=input('\nВведите ФИО: ')
    if not position or position==2:
        while True:
            user_data['Пол']=input('Введите Пол (М/Ж): ')
            if user_data['Пол']!='M' and user_data['Пол']!='Ж' and user_data['Пол']!='м' and user_data['Пол']!='ж':
                print('Вы ввели неверное значение. Попробуйте снова')
            else:
                break
    if not position or position==3:
        while True:
            user_data['Возраст']=input('Введите Возраст, полных лет: ')
            try:
                int(user_data['Возраст'])
            except:
                print('Вы ввели неверное значение. Попробуйте снова')
            else:
                break
    if not position or position==4:
        while True:
            user_data['Вес']=input('Введите Вес, кг: ')
            try: 
                Decimal(user_data['Вес'])
            except:
                print('Вы ввели неверное значение. Попробуйте снова')
            else:
                break
    if not position or position==5:
        while True:
            user_data['Рост']=input('Введите Рост, см: ')
            try:
                Decimal(user_data['Рост'])
            except:
                print('Вы ввели неверное значение. Попробуйте снова')
            else:
                break
    return user_data

def imt_calc(list):                                                     #Рассчитываем ИМТ
    imt_list = [                                                                        #Расшифровка ИМТ
    [16, 'выраженный дефицит массы тела.', 'Пора начинать кушать или боюсь скоро вы окажетесь в больнице! Прекращаем голодать!'],
    [18, 'недостаточная (дефицит) масса тела', 'Питайтесь больше! Все еще недостаточное питание '],
    [25, 'норма', 'Все хорошо! Так держать!'],
    [30, 'избыточная масса тела (предожирение)', 'Пора задуматься о том, что вы едите'],
    [35, 'ожирение', 'Пора урезать рацион. Многовато калорий!'],
    [40, 'ожирение резкое', 'Снижение калорий в 2-3 раза строго рекомендуется!'],
    [100, 'очень резкое ожирение', 'Если вы еще можете ходить - срочно к врачу! Ну и кушаем в основном воду (хлеб отменяется)']
    ]
    user_height=Decimal(list['Рост'])/100                    
    user_weight=Decimal(list['Вес'])            
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
                print('\n    У вас',key[1],'\n', '   Наш совет: ',key[2])
                break

def delete_user(position):                                              #Удаление пользователя
    global users_database
    key=input("\nВы уверены? (y)")
    if key=='y' or key=='н':
        del users_database[position]
        print("\nПользователь удален\n\nТекущий список пользователей")
        print_users()
    else:
        print("\nУдаление отменено")

def change_user_data(list):                                             #Изменение данных пользователя
    print("\nВыберите какие данные вы хотите изменить:")
    print_user_data(list)
    key=input("\nВведите номер записи, которую хотите изменить. Для выхода введите любую другую клавишу: ")
    try:
        key=int(key)
    except:
        print("Выход без изменений")
    else:
        list=get_user_data(list,key)
        print('\nИзмененные данные:')
        print_user_data(list)
    return list

def create_user():                                                      #Удаление пользователя
    global users_database
    users=len(users_database)-1
    print('Создание нового пользователя\nВведите ФИО: ')
    users_database[users]=get_user_data(users_database[users])
    print('\nВведенные данные: ')
    print_user_data(users_database[users])
    users_database.append({}) 

def print_menu(users):                                                  #Меню программы
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
    return key

def main():
    global users_database
    key='y'                                                     
    users=False                                                 #Определяет есть ли пользователи в базе
    while key!='q' and key!='й':                                
        key=print_menu(users)                                   #Вывести меню
        
        if key=="1":                                            #1. Ввести нового пользователя
            create_user()

        elif key=='2' and users:                                #2. Изменить данные пользователя
            user=get_user()                                
            users_database[user]=change_user_data(users_database[user])     
        
        elif key=='3' and users:                                 #3. Рассчитать ИМТ для пользователя
            imt_calc(users_database[get_user()])

        elif key=='4' and users:                                 #4. Вывести список пользователей
            print_user_data(users_database[get_user()])                     

        elif key=='5' and users:                                 #5. Удалить пользователя
            delete_user(get_user())
        
        if len(users_database)>1:                               #Проверка - есть ли пользователи в базе
            users=True
        else:
            users=False

if __name__ == "__main__":
    main()