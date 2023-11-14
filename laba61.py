con=0


while con ==0:
    list_num=[]

    count=0
    count_num=0
    m = ''

    text = input("Введите текст: ")

    for i in text:
        if i != " ":
            m += i
        elif m!='': 
            list_num.append(m) 
            m = ''
    if m!=' ':
        list_num.append(m)
        print(list_num)
    for i in list_num:
        count+=1
        if len(list_num)>=2:
            if len(i)>=2:
                count_num+=1
            else: continue
    if count == count_num: con+=1
    else: print("Введите техт, содержащий 2 или более слов, слова в котором не состоят из 1 символа ")

print(*list_num)
for i in list_num:
    if i != list_num[-1]:
        print(i)
    