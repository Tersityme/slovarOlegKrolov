def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def salvesta_failisse(f,text):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas

def tolkimine():
    pass

rus_list=loe_failist("rus.txt")
eng_list=loe_failist("eng.txt")
print(eng_list)
print(rus_list)

while True:
    v=input("Перевод-1,Новое слово-2,Исправить ошибку-3,Проверка знаний-4: ")
    if v=="1":
        tolkimine()
    elif v=="2":
        rus_sona=input("Введи слово на русском: ")
        eng_sona=input("Введи слово на английском: ")
        rus_list=salvesta_failisse("rus.txt",rus_sona)
        eng_list=salvesta_failisse("eng.txt",eng_sona)
        print=(rus_list)
        print=(eng_list)
    elif v=="3":
        pass
    elif v=="4":
        pass