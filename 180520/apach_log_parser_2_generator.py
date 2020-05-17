import os                         #как вариант переделать с использованием генератора - чтобы уменьшить объем памяти
from datetime import datetime

def uniq_ips(record):
    global ip_list
    global ip_list_full
    ip_list.add(record[0])
    ip_list_full.add(record[0])

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

def get_statistics(date,count,safari,firefox):
    global ip_list
    global statistics
    statistics[len(statistics)-1]['Дата']=date
    statistics[len(statistics)-1]['Количество']=count
    statistics[len(statistics)-1]['Уникальных IP']=len(ip_list)
    statistics[len(statistics)-1]['Safari']=safari
    statistics[len(statistics)-1]['Firefox']=firefox
    statistics.append({})
    ip_list=set()

def print_statistics():
    global statistics, ip_list_full
    statistics[len(statistics)-1]={
    'Дата':"Итого: ",
    'Количество': 0,
    'Уникальных IP':len(ip_list_full),
    'Safari':0,
    'Firefox':0
    }
    for record in statistics:
        try:
            print('Дата:',record['Дата'].date(), ' Записей: ',record['Количество'],' Уникальных IP: ',record['Уникальных IP'],' Safari: ',record['Safari'],' Firefox: ',record['Firefox'])
        except:
            print(record['Дата'], ' Записей: ',record['Количество'],' Уникальных IP: ',record['Уникальных IP'],' Safari: ',record['Safari'],' Firefox: ',record['Firefox'])
        statistics[len(statistics)-1]['Количество']=statistics[len(statistics)-1]['Количество']+int(record['Количество'])
        statistics[len(statistics)-1]['Safari']=statistics[len(statistics)-1]['Safari']+int(record['Safari'])
        statistics[len(statistics)-1]['Firefox']=statistics[len(statistics)-1]['Firefox']+int(record['Firefox'])

def main():
    global ip_list
    global ip_list_full
    safari=0
    firefox=0
    count=0
    os.system('cls' if os.name == 'nt' else 'clear') 
    path_to_file='150520/apache_logs.txt'
    for i in load_data(get_file_path(path_to_file)):    #Использование генератора позволит сократить расход памяти
        count+=1
        if count==1:
            date=datetime.strptime(i[3],"[%d/%b/%Y:%H:%M:%S")
        if date.date()!=datetime.strptime(i[3],"[%d/%b/%Y:%H:%M:%S").date():  
            get_statistics(date,count,safari,firefox)         
            count=0
            safari=0
            firefox=0
        uniq_ips(i)
        safari+=check_browser(i,"Safari")
        firefox+=check_browser(i,"Firefox")
    get_statistics(date,count,safari,firefox)

    #os.system('cls' if os.name == 'nt' else 'clear') 
    print_statistics()
    #print('Всего записей - ',count)
    #print('Количество уникальных IP адресов -',len(ip_list))
    #print('Всего записей с браузером Safari - ',safari)
    #print('Всего записей с браузером Firefox - ',firefox)

ip_list = set()
ip_list_full = set()
statistics=[{
    'Дата':"",
    'Количество': "",
    'Уникальных IP':"",
    'Safari':"",
    'Firefox':""
}]
if __name__ == "__main__":
    main()
