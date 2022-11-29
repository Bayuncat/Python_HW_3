from random import randint
import random

def Filist():
    length=randint(5, 20)
    yourlist = [random.uniform(-20, 20) for i in range(length)]
    yourlist = list(map(lambda x: round(x, ndigits=2), yourlist))
    return(yourlist)

mylist=Filist()
print(f'Список элементов : {mylist}')

def minMax(yourlist):
    res = 0
    minmaxlist=[]
    for i in range(len(yourlist)):
        minmaxlist.append(abs(yourlist[i]-int(yourlist[i])))
    minmaxlist = list(map(lambda x: round(x, ndigits=2), minmaxlist))
    print(f'Список значений  дробной части элементов : {minmaxlist}')

    minmaxlist.sort()
    print(f'Отсортированный список значений  дробной части элементов : {minmaxlist}')
    
    res = minmaxlist[len(minmaxlist)-1] - minmaxlist[0]
    res = round(res, ndigits=2) 
    return res

print(f'Разница между максимальным и минимальным значением дробной части элементов : {minMax(mylist)}')