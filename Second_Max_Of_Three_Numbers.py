n= int(input())
d={}
for x in range(n):
    d[x] = (input())
for x in range(len(d)):
    l=[int(y) for y in d[x].split(" ")]
    l.sort()
    print(l[1])
    
