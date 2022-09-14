# 33. *Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
import random

k = int(input("Введите степень k многочлена: "))
koef = []
temp1 = []
temp2 = []
rezult = []
for i in range(k + 1):
    koef.append(random.randint(0, 100))
print("Коэффициенты для многочлена: ", koef)
for i in range(len(koef)):
    temp1.append(f"{koef[i]} * x ^ {k} + ")
    k = k - 1
temp2 = "".join(temp1) + "= 0"
rezult = temp2.replace("* x ^ 0 + ", "")
rezult = rezult.replace("x ^ 1", "x")
rezult = rezult.replace(f"0 * x ^ {k} + ", "")  # ЭТИ 2 УСЛОВИЯ НЕ СРАБОТАЛИ, ХОТЕЛОСЬ БЫ ДОПИСАТЬ
rezult = rezult.replace(f"1 * x ^ {k} + ", f"x ^ {k} + ")  # ЧТО БЫ БЫЛ ИДЕАЛЬНЫЙ ВЫВОД ПРИ КОЭФФИЦИЕНТАХ 0 ИЛИ 1
with open('task-33.txt', 'w', encoding='utf-8') as f:
    f.write(rezult)
