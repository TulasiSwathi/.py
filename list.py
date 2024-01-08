a=[1,2,3]
print(a)
'''b = a  # both a & b points to same list.
print (b)
a[0]=12 # modifying list as both a & b pointing to same both will change.
print(a ,'\n' ,b)

# data slicing

print(a[1:2])
for num in a :
 print(num )
print(2 in a)
print(14 in b)'''
#del a
a=[6,3,9,2]
print(a)
print(sorted(a)) # sorts from small to big
print(sorted(a, reverse=True))# reverse
