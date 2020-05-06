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
user_data = {                                               #Структура пользовательских данных
        'ФИО': '',
        'Пол': '',
        'Возраст':'',
        'Вес':'',
        'Рост':''
}

def print_users(list):                                      #Процедура для вывода пользователей
    element=len(list)
    for i in range(0,element,1):
        print(i+1,' '+list[i]['ФИО'])

def get_user(list):                                         #Функция для выбора пользователя из списка
    print_users(list)
    element=len(list)
    key=input('Введите номер пользователя: ')
    if int(key) in range(1,element+1,1):
        return int(key)
    else:
        print('Вы ввели неверное значение')
        return 0

key='y'
users=False                                                 #Счетчик, определяющий есть ли пользователи в базе
while key!='q' and key!='й':                                #тело программы в цикле 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Операции:\n")
    print("1. Ввести нового пользователя")
    if users:                                               #блокируем вывод меню, которое недоступно, пока нет пользователей
        print("2. Изменить данные пользователя")
        print("3. Рассчитать ИМТ для пользователя")
        print("4. Вывести список пользователей")
        print("5. Удалить пользователя")
    print("q - Выход")
    key=input("\nЧто еще хотите сделать? (Введите 'q' для выхода из программы): ") 
    if key=="1":                                            #1. Ввести нового пользователя
        user_data['ФИО']=input('Создание нового пользователя\nВведите ФИО: ')
        user_data['Пол']=input('Введите Пол: ')
        user_data['Возраст']=input('Введите Возраст: ')
        user_data['Вес']=input('Введите Вес: ')
        user_data['Рост']=input('Введите Рост: ')
        if users:
            user_list[len(user_list)]=user_data
        else:
            user_list[0]=user_data
            user=True
            
    elif key=='2' and users:                                #Изменить данные пользователя
        os.system('cls' if os.name == 'nt' else 'clear')
        user_got=get_user(user_list)-1
        if user_got==0:
            print('Такого пользователя нет')
        else:
            #user_data=user_list[user_got]
            print("Выберите какие данные вы хотите изменить:")
            print("1. ФИО: ",user_list[user_got]['ФИО'])
            print("2. Пол: ",user_list[user_got]['Пол'])
            print("3. Возраст: ",user_list[user_got]['Возраст'])
            print("4. Вес: ",user_list[user_got]['Вес'])
            print("5. Рост: ",user_list[user_got]['Рост'])
            print("6. Для выхода введите любую другую клавишу")
            key=input("\nВведите номер записи, которую хотите изменить (Введите 'q' для выхода без изменений): ")
            try:
                key=int(key)
            except:
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
                
        
    elif key=='3'and users:
        continue
    elif key=='4'and users:
        continue
    elif key=='5'and users:
        continue

        
        