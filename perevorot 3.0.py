a = int(input())
c = int()
b = a
while a != 0:
    c += (a % 10)
    c *= 10
    a = a // 10
c = c // 10
if b == c:
    print("sasatb")
else:
    print("ne syd'ba")
