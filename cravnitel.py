while(True):
    a = int(input("Введите число: "))
    
    if(a < 100):
        print(a, end = "")
        print(" меньше 100")
    
    elif(a > 100):
        print(a, end = "")
        print(" больше 100")
    
    else:
        print(a, end = "")
        print(" равно 100")
    yesno = input("Хотите ли ещё раз?\n(Да или Нет)")
    if(yesno == "Нет"):
        break
