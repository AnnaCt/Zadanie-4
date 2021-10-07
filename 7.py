try:
        a = int(input("Введите число: ")) 
except ValueError:
        print("Ошибка")
else:
    try:
        base = int(input("Введите основание системы счисления: ")) 
    except ValueError:
        print("Ошибка")
    else:
        if not((base==8) or (base==2)):
           print("Ошибка")
        if base == 8:
            if a == 0:
                print("Вывод:0")
            aa=a
            a=abs(a)
            nA = ''
            while a > 0:
                nA = str(a % base) + nA
                a //= base
            if aa < 0:
                print("Вывод: -" + str(nA))
            elif aa >0:    
                print("Вывод:" + str(nA))
        if base == 2:
            if a == 0:
                print("Вывод:0")
            if a>0:
                r1 = bin(a)[2:]
                res = '0' * (8-len(r1)) + r1
                print("Вывод:" + str(res))    
            if a<0:
                r1 = bin(~(-a))[4:]
                res = '1' * (7-len(r1)) + '0' + r1
                print("Вывод:" + str(res))
                
            
    
