a = int(input())
while a > 1:
    b = 2
    c = 0
    while 1:
        if a % b == 0:
            a = a // b
            print(b, end= ', ')
            c = 1
            break
        else:
            b += 1