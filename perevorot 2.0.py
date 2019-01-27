a = int(input())
z = int()
n = 0
g = 1
b = a
while (a // g) >= 1:
    g = g * 10
    n = n + 1
g = g // 10
for i in range(n):
    z += (b % 10) * g
    b = b // 10
    g = g // 10
if a == z:
    print("sasatb")
else:
    print("ne syd'ba")
