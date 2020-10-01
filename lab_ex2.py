a=input('Первый член: ')
a=int(a)
b=input('знаменатель: ')
b=int(b)
nMAX=input('Количество членов: ')
nMAX=int(nMAX)
for n in range(1,nMAX):
    print(a*b**(nMAX-1))
