# 34. *Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0  и x² + 5 = 0 => 3x² + 4x + 10 = 0

with open('file-1.txt', 'w') as f:
    f.write("2 * x ^ 2 + 4 * x + 5 = 0")
with open('file-2.txt', 'w') as f:
    f.write("x ^ 2 + 5 = 0")
with open('file-1.txt', 'r') as f:
    mng1=f.readline().split(" ")
with open('file-2.txt', 'r') as f:
    mng2=f.readline().split(" ")
# mng1_r=" ".join(mng1[::-1])
# mng2_r=" ".join(mng2[::-1])
mng1_r=mng1[::-1]
mng2_r=mng2[::-1]
print(mng1_r)
print(mng2_r)
# for i in range(len(mng1_r)):
# Дальше пока не получилось, постараюсь до семинара решить, но пока не поняла как выделить коэффициенты и просуммировать
