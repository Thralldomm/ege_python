
import itertools
alphabet = "ЕГЭ" # весь алфавит
vol = "ЕЭ" # гласные
ar = itertools.product(alphabet, repeat = 5) #Размещение с повторением (5 - длина слова)
# егэээ егээе егээг егэеэ егэег ...

arl = []
for i in ar:
    arl.append(list(i)) # записываем все из itertools (размещений) в нормальный список

count = 0 # счетчик
for e in arl: # проходимся по списку
    if e[0] in vol: # если первая буква элемента списка - гласная, то так уж и быть - считаем
            count += 1
print(count)