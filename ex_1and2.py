from random import randint

def Filist():
    length=randint(5, 10)
    yourlist = [randint(0, 20) for i in range(length)]
    return(yourlist)

def oddChecking(yourlist):
    res = 0
    for i in range(len(yourlist)):
        if i % 2 != 0: 
            res += yourlist[i]
    return res

def multСouple(yourlist):
    multlist=[]
    j = (len(yourlist)+1)//2
    for i in range(j):
        multlist.append(yourlist[i]*yourlist[len(yourlist)-1-i])
    return(multlist)

mylist=Filist()
print(f'Список элементов : {mylist}')
print(f'Cумма элементов списка, стоящих на нечётной идексах : {oddChecking(mylist)}')
print(f'Произведение пар чисел списка : {multСouple(mylist)}')