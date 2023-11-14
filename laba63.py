import random

max_num=0
loop_count=0
multiply=1
while True:
    try:
        n = int(input("Введите размер списка: "))
        if n>=2: break 
    except:
        continue

while True:
    
    zero_count=0
    num_list = [random.randint(-2048, 2048) for i in range(n) ]
    for i in num_list:
        if i == 0:
            zero_count+=1
    if zero_count>=2: break

for i in range(len(num_list)):
    if num_list[i]==0:
        for j in range(len(num_list)):
            if num_list[j]==0 and i!=j:
                for k in range(i+1,j):
                    multiply*=num_list[k]
                    # print(num_list[k])

            

        

for i in num_list:
    if i > max_num:
        max_num = i
print(f"Исходный список: {num_list}")

print(f"максимальное значение: {max_num}")

print(f"Произведение элементов, расположенных между первым и вторым нулевыми элементами: {multiply}")
