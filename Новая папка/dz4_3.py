text = input('Введите слова через пробел: ')

upper_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alph = 'abcdefghijklmnopqrstuvwxyz'

lower_text = ''

for i in text:
    if i in upper_alph:
        for index in range(26):
            if i == upper_alph[index]:
                lower_text += lower_alph[index]
    else:
        lower_text += i

slovo = ''
slova = []

for i in lower_text:
    if i == ' ':
        slova.append(slovo)
        slovo = ''
    else:
        slovo += i
if slovo:
    slova.append(slovo)

slovo_dict = {}

for el in slova:
    if el in slovo_dict:
        slovo_dict[el]+=1
    else:
        slovo_dict[el]=1

new_slova = []
a = slovo_dict.items()

for item in a:
    new_slova.append({'слово':item[0],
                      'кол-во вхождений':item[1]})

for i in range(len(new_slova)):
    max_c = i

    for j in range(i+1, len(new_slova)):
        if new_slova[j]['кол-во вхождений'] > new_slova[max_c]['кол-во вхождений']:
            max_c = j

    new_slova[i],new_slova[max_c] = new_slova[max_c],new_slova[i]

print('Самые частые слова')
count = 0

for i in new_slova:
    if count<5:
        print(i['слово'],i['кол-во вхождений'])
    count += 1
