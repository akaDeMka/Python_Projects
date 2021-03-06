import os                         #как вариант переделать с использованием генератора - чтобы уменьшить объем памяти

def count_records():
    global log_records
    print('Всего записей - ',len(log_records) )

def uniq_ips():
    global log_records
    ip_list=[]
    for element in log_records:
        ip_list.append(element[0])
    ip_list=set(ip_list)
    print('Количество уникальных IP адресов -',len(ip_list))

def load_data(file_path):
    global log_records
    while not os.path.exists(file_path):
        file_path=input('Файл не найден. Введите путь до файла или нажмите q: ')
        if file_path=='q' or file_path=='й':
            exit()
    with open(file_path, 'r') as f:
        for line in f.readlines():
            log_records.append(str(line).split(' '))

def check_browser(browser):
    count=0
    global log_records
    for record in log_records:
        if record[len(record)-1].find(browser)!=-1:
            count+=1
    print('Всего записей с браузером ',browser,' - ',count)

def main():
    os.system('cls' if os.name == 'nt' else 'clear') 
    #load_data(input('Текущая диектория '+os.path.abspath(".")+'\nВведите путь к файлу: '))      #Можно ввести вручную - но лень
    load_data('150520/apache_logs.txt') #Тут в зависимостьи от стартовой директории - я запускаю так
    os.system('cls' if os.name == 'nt' else 'clear') 
    count_records()
    uniq_ips()
    check_browser("Safari")
    check_browser('Firefox')

log_records=[]
if __name__ == "__main__":
    main()
