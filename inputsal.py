''' sal= 2000
TA= 400.0
DA =600.0
HRA= 200.0
gross income =3200.0
tax=384.0
salary in hand= 2816.0'''
sal = int(input("enter salary of an employee"))
hra = 0.1 * sal
ta=0.2*sal
da=0.3*sal
gi=sal+hra+da+ta
tax=0.12*gi
netsal= gi-tax
print("****salary sheet****","\n","salary =", "\t",sal)
print("TA","\t",ta)
print("DA","\t",da)
print("HRA","\t",hra)
print("GROSS INCOME","\t",gi)
print("TAX","\t",tax)
print("SALARY IN HAND","\t",netsal)