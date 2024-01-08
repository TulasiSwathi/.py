'''def functionname():
    print("This is a function declaration in python")
functionname() # calling function'''
'''def functionname(name): # name is a parameter here
    print("It displays name",name)
functionname("tulasi") # calling function'''
'''def functionnameadd(a,b):
 return a+b
c= functionnameadd(3,1)
print(c)'''
'''def functionnamemul(a):
    return a*3
print(functionnamemul(4))'''
'''def functionname(a):
    for i in a:
        print(i)
functionname([1,2,3,4,5])'''
'''def functionname(*a): #arbitary argument
    print(a)
functionname(1,2,767,5,43,98)#calling it will store complete data in tuple
'''
def functionname(**a):# keyword argument
    print(a)
functionname(name='tulasi',age='32') #output will save in digital format  and to store it will take key and value