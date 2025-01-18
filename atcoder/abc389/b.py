x = int(input())

if x == 2:
    print(2)
else:
    m = 1
    for i in range(1, x):
        m = m * i
        if m == x:
            break

    print(i)
