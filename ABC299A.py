n = int(input())
s = input()
fi = s.index("|")
se = s.rindex("|")
a = s.index("*")
print("in" if fi<a<se else "out")