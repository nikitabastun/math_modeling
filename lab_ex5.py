for a in range(2, int(input('Input number: '))):
    n = 0
    for b in range(1,a):
        if a%b == 0:
            n += b
            continue
    if n==a:
        print (a)
