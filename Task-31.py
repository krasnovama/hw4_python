# 31 Задайте натуральное число N. Напишите программу, которая составит список простых
# множителей числа N.

my_list = []
numb = int(input())
delitel = 2
if numb == 1:
    print("Простой множитель: 1")
    exit()
for i in range(numb):
    if numb % delitel == 0:
        my_list.append(delitel)
        numb = numb / delitel
    else:
        delitel = delitel + 1
print("Простые множители: ", my_list)
