import itertools

a = int(input("Ввидите количество чисел Фибоначчи для вывода значений: "))

s = [0, 1]
s += [(s := [s[1], s[0] + s[1]]) and s[1] for k in range(a)]

m = [0, 1]
m += [(m := [m[1], m[0] - m[1]]) and m[1] for k in range(a)]
m.reverse()
m.pop(-1)

res = m + s

print(res)
