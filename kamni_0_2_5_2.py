import random

def inp_ut(ma_xod):                                                 #проверка ввода числа (взять камней в игре)
    while True:
        try:
            text = '{} {} '.format("Введите число",'>>')
            a = int(input(text))
            if (a<=ma_xod and a != 0):
                return a
            else:
                print("слишком большое число,либо 0. Введите другое")
        except ValueError:
            print("слишком большое число, введите другое")


def int_vvod(s,trig):                                                    #проверка на ввод двух первых чисел(возможно можно объединить с верхним, но пока так
    arr = "123"
    if trig == "T":
        print("Введите число:")
        while s.isnumeric() != True:
            s = str(input())
            if (s.isnumeric() != True): print("Число не подходит")
        
    else:
        print("Введите число:")
        while s.isnumeric() != True:
            s = str(input())
            if (s.isnumeric() != True): print("Число не подходит")
        while (s not in arr):
            s = str(input())
            if (s not in arr): print("Число не подходит")
    return s

def logic(tok,ma_xod,ma,xod1):                                           # типа логика компьютера и выбор сложности. На легком числа рандомные,а на среднем, если комп за 1 ход может выиграть                   
    if tok == 1:                                                    #он это делает
        comp = random.randint(1, ma_xod)
    if tok == 2:
        if (ma_xod>=ma):
            comp = ma
        else:
            comp = random.randint(1, ma_xod)
    if tok == 3:
        match ma_xod:
            case 1:
                if (xod1 == 1) and (ma % 2 == 0):
                    print("Пользователь выиграл")
                    comp = ma+1
                if (xod1 == 1) and (ma % 2 != 0):
                    print("Выиграл компьютер")
                    comp = ma+1
                if (xod1 == 2) and (ma % 2 == 0):
                    print("Выиграл компьютер")
                    comp = ma+1
                if (xod1 == 2) and (ma % 2 != 0):
                    print("Пользователь выиграл")
                    comp = ma+1
            #case 2:
                
                    
                
                    
    return comp




def game_one(ma,ma_xod,cou,tok,xod1):
    xod2 = xod1
    print("Ход ",cou)                                             #считает количество ходов(просто для красоты)
    cou+=1
    comp = logic(tok,ma_xod,ma,xod2)
    if (comp == ma+1):
        return 0
    if xod1 == 1:
        if (ma_xod>=ma):                                              #уменьшает количество допустимых камней, которые можно взять, если в куче столько уже нет
            ma_xod = ma
            print(ma_xod,ma)                               
        ma-=comp
        if (ma == 0):
            print('Выиграл компьютер')
            return
        print("Компьютер взял",comp,"осталось",ma)                  #а тут пользователь
    xod1 = 1
    if (ma_xod>=ma):                                              
        ma_xod = ma
    kk = inp_ut(ma_xod)
    ma-=kk
    if ma == 0:
            print('Вы выиграли, поздравляю!')
            return
    else:
        game_one(ma,ma_xod,cou,tok,xod1)

        
s="q"
trig = "T"
print("сколько в основной куче будет камней?")    
ma = int(int_vvod(s,trig))
print("Сколько за ход можно  взять камней?")                 
ma_xod = int(int_vvod(s,trig))
print("Введите уровень сложности: 1 - легкий 2 - средний 3 - тяжёлый")
cou =1
trig = "F"
xod1 = 0

tok = int(int_vvod(s,trig))

print("кто ходит первый? компьютер - 1 человек - 2")
xod1 = int(input())
game_one(ma,ma_xod,cou,tok,xod1)
