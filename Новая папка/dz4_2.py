text = input('Введите текст')

maximum=0
cnt=0

low_alph = "abcdefghijklmnopqrstuvwxyz"
high_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for a in text:
    if a != " ":
        cnt += 1
    else:
        if cnt > maximum:
            maximum = cnt
        cnt = 0

if cnt > maximum:
    maximum = cnt

new_text = ''

for ch in text:
    if ch in low_alph:
        for i in range(26):
            if ch == low_alph[i]:
                new_text += low_alph[(i + maximum) % 26]

    elif ch in high_alph:
        for i in range(26):
            if ch == high_alph[i]:
                new_text += high_alph[(i + maximum) % 26]

    else:
        new_text += ch

print(maximum)
print(new_text)
