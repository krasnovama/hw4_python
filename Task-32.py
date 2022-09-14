# 32. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

print("Вариант 1")
str = input("Введите последовательность чисел через пробел: ")
my_list = str.split(" ")
my_list_rezult = []
for i in range(len(my_list)):
    if my_list[i] not in my_list_rezult:
        my_list_rezult.append(my_list[i])
print("Список неповторяющихся элементов", my_list_rezult)

'''
Второй вариант хотела решить таким образом, что бы повторяющиеся элементы не выходили вообще, 
решение не получилось по причине ошибки 'list' object has no attribute 'symmetric_difference',
которую побороть не сообразила как
Решение предполагала такое:

print("Вариант 2")
str = input("Введите последовательность чисел через пробел: ")
my_list = str.split(" ")
my_list_rezult = []
temp_list=[]
rezult=[]
for i in range(len(my_list)):
    if my_list[i] not in my_list_rezult:
        my_list_rezult.append(my_list[i])
temp_list=my_list.symmetric_difference(my_list_rezult)  ### ТУТ ОШИБКА ???
rezult=my_list_rezult-rezult                            ### ТУТ ОШИБКА ???
print("Список неповторяющихся элементов", rezult)
'''
