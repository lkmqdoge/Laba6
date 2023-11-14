text = input("Введите текст: ")

delete_this = input("Введите символ для удаления: ") 
text_new =''
for i in text:
    if i != delete_this:
        text_new += i
print(text)
print(text_new)