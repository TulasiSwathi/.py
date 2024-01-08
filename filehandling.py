'''
read
write
open
'''
'''s=open('demo.txt',mode='r')
#print('demo.txt')
print(s.read())
s.close()'''


'''s=open('demo.txt',mode='a')  #a appending for w and w+ data is truncating(replacing) data with new text.
s.write("I am appending somemore text")
s.close()

s=open('demo.txt',mode='r+')
print(s.read())
s.write("\n r+ method")
s.close()'''

s=open('demo1.txt',mode='w+') # truncate
#print('demo.txt')
s.write("w+ mode")
s.seek(0)
print(s.read())
s.close()