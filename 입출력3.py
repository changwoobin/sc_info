a = int(input("반지름"))
b = 2 * 3.14 * a
c = 3.14 * a * a

b = str(b)
c = str(c)

f = open("t.txt", "w")
f.write(b)
f.write(c)
f.close()

f= open("t.txt", "r")
s = f.read()
print(s)
