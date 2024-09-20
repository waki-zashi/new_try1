k = 0
m = 0
for i in range(1000, 10000):
    i = str(i)
    if int(i[0]) % 3 == 0:

@@ -9,5 +13,9 @@ for i in range(1000, 10000):

    if r > 10:
        k += 1
        m += 1

print(m)
