f=open("t.txt", "w")
f.write("우빈님! 안녕하세요?")
f.close()

f.open("t.txt", "r")
s = f.read()
print(s)
f.close()
