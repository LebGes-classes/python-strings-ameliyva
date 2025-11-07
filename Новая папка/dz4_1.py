vvedenniy_text = input("Введите текст: ")
word = ''

for i in range(len(vvedenniy_text)-1, -1, -1):
    word += vvedenniy_text[i]

dop_spisok = []
words = ''

for i in vvedenniy_text:
    if i == ' ':
        dop_spisok.append(words)
        words = ''
    else:
        words += i

if words:
    w.append(words)

q = ''

for i in range(len(dop_spisok) - 1, -1, -1):
    q += dop_spisok[i] + (' ' if i != 0 else '')

print("Исходный текст: ", vvedenniy_text)
print("Зеркальный порядок: ", q)
print("Отзеркаленная строка: ", word)