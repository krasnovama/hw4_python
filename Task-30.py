# 30 Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. *Сохранить словарь в файл users_hobby.txt. Фрагмент файла с данными
# о пользователях (users.txt): Иванов Иван Иванович Петров Петр Петрович Фрагмент файла с данными
# о хобби (hobby.txt): скалолазание, охота горные лыжи
users = []
hobby = []
my_dict = {}
with open('users.txt', 'w', encoding='utf-8') as f:
    f.write("Иванов Иван Иванович\n")
    f.write("Петров Петр Петрович\n")
    f.write("Николаев Николай Николаевич\n")
    f.write("Сергеев Сергей Сергеевич\n")
    f.write("Романов Роман Романович\n")
with open('hobby.txt', 'w', encoding='utf-8') as f:
    f.write("Скалолазанье\n")
    f.write("Охота\n")
    f.write("Горные лыжи\n")
    f.write("Пинг-понг\n")
    f.write("Шахматы\n")
with open('users.txt', 'r', encoding='utf-8') as f:
    users = f.read().splitlines()
with open('hobby.txt', 'r', encoding='utf-8') as f:
    hobby = f.read().splitlines()
for i in range(len(users)):
    my_dict[users[i]] = hobby[i]
with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    for k, v in my_dict.items():
        f.write('{}: {}\n'.format(k, v))