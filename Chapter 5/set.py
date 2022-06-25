a = {2,8,3,0,4,1,7,1,1,1}

print(type(a))
print(a)

b = set()
print(type(b))

b.add(4)
b.add(5)
b.add(3)

b = {2,4,9,5,9,4,0,6}

print(b)

#we can not add List or Dictionary in Set Because both are mutable
# But we can add the Tuple  Because it Immutable



print(len(b))
b.remove(9)
print(b)\



print(b.pop())
print(b.pop())