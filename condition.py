'''Descision making statements
if
else
elif
nestedif
'''
'''
syntax
if condition:
statement
'''
'''if True:
    print("if true")
else:
    print("else if")'''

'''if False:
    print("if true")
elif True:
    print("elif true")
else:
    print("else if")'''
if True:
    print("outer if")
    if True:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer else")