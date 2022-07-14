x = 0
y = 1
z = 1
for z in range(1, 44):
    x = y
    y = z
    z = z + y + x +1
    print(z)