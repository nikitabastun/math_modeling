print("Введите число:")
A = int(input("A = "))
B = 0
while A>0:
    B = B*10 + A%10
    A = A//10
print(B)