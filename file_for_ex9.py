k = 0
m = 0
for i in range(1000, 10000):
    i = str(i)
    if int(i[0]) % 3 == 0:
        r = int(i[0]) + int(i[2]) + abs(int(i[1]) - int(i[3]))
    else:
        r = (bin(int(''.join(sorted(i))))[2:]).count('1')

    if r > 10:
        k += 1
        m += 1
print(k + m)
