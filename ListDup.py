a=[1,2,3,3,4,5,6,7,8,5,5,4,4]
b=set(a)
print (b)
for c in b:
	print(c,a.count(c))
