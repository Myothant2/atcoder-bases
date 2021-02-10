

s = input()
token = s.split()
b = int(token[0])
c = int(token[1])

if b*c % 2 == 1:
    print("odd")
else:
    print("even")