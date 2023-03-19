list = []
def list_name():
    for n in range(141):
        year = 1880+n
        list.append('/Users/dengqiaoyin/臺灣大學/五234計算機程式設計/報告/names/yob%d.txt'%(year))
def open_file():
    year = 1879
    for txt_name in list:
        boy_count = 0
        girl_count = 0
        year += 1
        file = open(txt_name)
        for baby_name in file:
            information = baby_name.split(',')
            if information[1] == 'F':
                girl_count += int(information[2])
                continue
            if information[1] == 'M':
                boy_count += int(information[2])
        if girl_count > boy_count:
            print('year %d: more girls - %d > %d' %(year,girl_count,boy_count))
        if boy_count > girl_count:
            print('year %d: more boys - %d > %d' %(year,boy_count,girl_count))        
list_name()
open_file()
