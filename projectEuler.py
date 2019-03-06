def fibonacci(f):
    a = 1
    b = 2
    c = 3
    d = []
    e = 0
    g = 5
    while True:
        d.append(a)
        if g <= 4000000:
            c = a+b
            g = c+b
            a = b
            b = c
            c = g
        else:
            for x in range(len(d)):
                if d[x]%2==0:
                    print(d[x])
                    e=e+d[x]
            break
    return e
