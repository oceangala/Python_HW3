s = input('Введите слово: ')
sp = []
sp.extend(s.upper())
# print(sp)
one_list = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two_list = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
three_list = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
four_list = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
five_list = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
eight_list = ['J', 'X', 'Ш', 'Э', 'Ю']
ten_list = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

one_d = dict.fromkeys(one_list, 1)
two_d = dict.fromkeys(two_list, 2)
three_d = dict.fromkeys(three_list, 3)
four_d = dict.fromkeys(four_list, 4)
five_d = dict.fromkeys(five_list, 5)
eight_d = dict.fromkeys(eight_list, 8)
ten_d = dict.fromkeys(ten_list, 10)

scrable_d = {**one_d, **two_d, **three_d, **four_d, **five_d, **eight_d, **ten_d}
# print(scrable_d)
total = 0
for i in sp:
    total += scrable_d[i]
print('Стоимость слова:', total)