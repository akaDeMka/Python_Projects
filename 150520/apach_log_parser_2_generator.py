import os                         #как вариант переделать с использованием генератора - чтобы уменьшить объем памяти

def uniq_ips(record):
    global ip_list
    ip_list.add(record[0])

def get_file_path(file_path):
    while not os.path.exists(file_path):
        file_path=input('Файл не найден. Введите путь до файла или нажмите q: ')
        if file_path=='q' or file_path=='й':
            exit()
    return file_path

def load_data(file_path):
    with open(file_path, 'r') as f:
        for line in f.readlines():
            yield str(line).split(' ')

def check_browser(record, browser):
        if record[len(record)-1].find(browser)!=-1:
            return 1
        else:
            return 0

def main():
    safari=0
    firefox=0
    count=0
    os.system('cls' if os.name == 'nt' else 'clear') 
    path_to_file='150520/apache_logs.txt'
    for i in load_data(get_file_path(path_to_file)):
        count+=1
        uniq_ips(i)
        safari+=check_browser(i,"Safari")
        firefox+=check_browser(i,"Firefox")

    os.system('cls' if os.name == 'nt' else 'clear') 
    print('Всего записей - ',count)
    print('Количество уникальных IP адресов -',len(ip_list))
    print('Всего записей с браузером Safari - ',safari)
    print('Всего записей с браузером Firefox - ',firefox)

ip_list=set()
if __name__ == "__main__":
    main()
