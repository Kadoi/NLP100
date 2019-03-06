# coding: utf-8

#自分の実装
def reversing(word):
    hanten = []
    parts = list(word)
    for i in reversed(parts):
        hanten.append(i)
    return "".join(hanten)

word = "stressed"

print(reversing(word))

#もっとマシな実装
alpha = "stressed"
alpha = alpha[::-1]
print(alpha)
