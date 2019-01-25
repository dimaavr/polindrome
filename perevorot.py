a = int(input())
n = 1
b = 0
while (a // (10 ** n)) >= 1:
    n = n + 1
for i in range(n):
    b += int((10 ** i) * ((a // (10 ** (n - (i + 1)))) - (a // (10 ** (n - i)) * 10)))
if a == b:
    print("sasatb")
else:
    print("ne syd'ba")
