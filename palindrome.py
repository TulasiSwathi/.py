
string1="hema sri"
string1="".join(reversed(string1))
print(string1)



#string2=string1[::-1]
#string2=string1[-5]+string1[-4]+string1[-3]+string1[-2]+string1[-1]
#print(string2)
'''i=len(string1)
for j in range(i-1,-1,-1):
    string2=string2+string1[j]
    '''

'''for i in range(0,len(string1)):
    string2= string1[i]+string2
'''
#
# if(string2== string1):
if string1=="hema sri":
    print("palindrome") 
else:
    print("not a palindrome")
