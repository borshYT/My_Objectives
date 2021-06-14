import json as js

data = dict()

print( 'MY OBJECTIVES by NIKITA RECHKIN' )

def get_test_jFile():
    return {
        'Монитор': {
            'price': 12000,
            'deposit': 2000,
            'balance': 6000,
        }
    }
def save():
    global data
    with open( 'base.json', 'w', encoding = 'utf-8' ) as file:
        js.dump( data, file, ensure_ascii = False )
def load():
    global data
    with open( 'base.json', 'r', encoding = 'utf-8' ) as file:
        data = js.load( file )
def start():
    while True:
        try:
            result = int(input( '''Выберите действие: 
    1 - Мои цели,
    2 - Полный сброс,
    3 - Выход\n''' ))
            break
        except:
            print( 'Введите номер!' )
    if result == 1:
        objs()
    elif result == 2:
        pass
    elif result == 3:
        exit()
def create_obj():
    global data
    obj_name = input( 'Введите имя цели: ' )
    while True:
        try:
            obj_price = int( input( 'Введите сумму на которую копите(цифрами без букв): ' ) )
            break
        except:
            print( 'Введите цифрами!!' )
    while True:
        try:
            obj_deposit = int( input( 'Введите сумму которую вы будете вносить каждый месяц(цифрами без букв): ' ) )
            break
        except:
            print( 'Введите цифрами!!' )
    data[obj_name] = {
        'price': obj_price,
        'deposit': obj_deposit,
        'balance': 0
    }
    save()
    start()
def del_obj():
    global data
    try:
        data_keyList = list(data.keys())
        for i in range( len( data_keyList ) ):
            print( f'{i} - {data_keyList[i]}' )
        while True:
            try:
                result = int( input( 'Выберите номер для удаления: ' ) )
                break
            except:
                print( 'Введите номер!!' )
        while True:
            if result <= len( data_keyList ):
                for i in range( len( data_keyList ) ):
                    if result == i:
                        del data[ data_keyList[ i ] ]
                        save()
                        break
            else:
                print( 'Такого номера нет!!' )
    except:
        res = input( 'Целей пока нет:( Создать?\n(да/нет): ' )
        res = res.lower()
        if res == 'да':
            create_obj()
        else:
            start()
def objs():
    while True:
        try:
            result = int( input( '''Выберите действие: 
1 - Список целей,
2 - Добавить цель,
3 - Удалить цель,
4 - Выйти в главное меню.
Введите номер: ''' ) )
            break
        except:
            print( 'Введите номер действия!!!' )
    if result == 1:
        try:
            data_keyList = list(data.keys())
            while True:
                for i in range( len( data_keyList ) ):
                    print( f'{i} - {data_keyList[i]}' )
                result = int( input( 'Введите номер: ' ) )
                if result <= (len( data_keyList ) - 1):
                    break
                else:
                    print( 'Такого номера нет!' )
            for i in range( len( data_keyList ) ):
                if result == i:
                    menu( data_keyList[i] )
                    start()
        except:
            res = input( 'Целей пока нет!! Создать цель?\n(да/нет): ' )
            res = res.lower()
            if res == 'да':
                result = 2
    if result == 2:
        create_obj()
    elif result == 3:
        del_obj()
    elif result == 4:
        start()
    else:
        print('Такого номера нет!')
        objs()
def menu( key ):
    global data
    ost = data[key]['price'] - data[key]['balance']
    print( f'''------------------------------------
Имя: {key},
Стоимость: {data[key]['price']},                  
Количество денег в месяц: {data[key]['deposit']}, 
Осталось накопить: {ost}                          
---------------------------------------------------''' )
    while True:
        try:
            result = int( input( '''Выберите действие: 
1 - Пополнить баланс,
2 - Снять деньги с баланса,
3 - Настройки цели,
4 - Выйти в главное меню\n''' ) )
            break
        except:
            print( 'Впишите номер!!' )
    if result == 1:
        while True:
            try:
                result = int( input( 'Пополнение баланса, введите сумму: ' ) )
                break
            except:
                print( 'Впишите только числами!!!' )
        balance = data[key]['balance'] + result
        data[key]['balance'] = balance
        save()
        menu( key )
    elif result == 2:
        while True:
            try:
                result = int( input( 'Снять с баланса, введите сумму: ' ) )
                break
            except:
                print( 'Впишите номер!!!' )
        balance = data[key]['balance'] - result
        data[key]['balance'] = balance
        save()
        menu( key )
    elif result == 3:
        settings( key )
    elif result == 4:
        start()
def settings( key ):
    while True:
        try:
            result = int( input( '''Настройки цели:
1 - Изменить имя,
2 - Изменить цену,
3 - Изиенить плату в месяц,
4 - Выйти в меню цели.
Введите номер: ''' ) )
            break
        except:
            print( 'Введите номер!!!' )
    if result == 1:
        res = input( 'Введите новое имя цели: ' )
        dct = data[key]
        data[res] = dct
        del data[key]
        key = res
        save()
        print( 'Имя изменено!' )
        settings( key )
    elif result == 2:
        while True:
            try:
                res = int( input( 'Введите цену цели: ' ) )
                break
            except:
                print( 'Введите цифрами: ' )
        data[key]['price'] = res
        save()
        print( 'Цена изменена!' )
        settings( key )
    elif result == 3:
        while True:
            try:
                res = int( input( 'Введите сумму которую будете платить каждый месяц: ' ) )
                break
            except:
                print( 'Введите цифрами: ' )
        data[key]['deposit'] = res
        save()
        print( 'Платёж в месяц изменён!' )
        settings( key )
    elif result == 4:
        menu( key )

#data = get_test_jFile()
#save()
try:
    load()
except:
    #data = get_test_jFile()
    save()
start()
