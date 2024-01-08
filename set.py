#s={2,231,3456}
#rint (type(s))

'''s1={3,5,656,32,656,46,986,32}

add
update
pop
remove

#print(s1)
s1.add(123)
print(s1)

s1.update({21,37,56,656})
s1.pop()
s1.pop()
s1.remove(21)
print(s1)
'''

'''
union
intersection
difference
issubset
issuperset'''

s1={1,2,3,4,5,6}
s2={4,5,6,3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))