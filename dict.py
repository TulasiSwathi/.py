'''d={}
print(type(d))
d={1:'ROOT HOOT',2:'PYTHON',3:'DevOps'}
print(d.get(1))
print(d.keys())
print(d.values())
print(d.items())
print(d.update({4:'Tableau'}))
print(d)

'''

for i in ({1:'ROOT HOOT',2:'PYTHON',3:'DevOps'}):
    print(i)
for i in ({1:'ROOT HOOT',2:'PYTHON',3:'DevOps'}).values():
    print(i)
for i in ({1:'ROOT HOOT',2:'PYTHON',3:'DevOps'}).items():
    print(i)
for i in ({1:'ROOT HOOT',2:'PYTHON',3:'DevOps'}).keys():
    print(i)