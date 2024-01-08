s="epa23ez26"
i=0
j=len(s)-1
while( i<j):
    while(str.isdigit(s[i])) :
        i=i+1
    while(str.isdigit(s[j])):
        j =j-1
    if str.isalpha(s[i]) and str.isalpha(s[j]):
        lt=list(s)
        lt[i],lt[j]=lt[j],lt[i]
        s="".join(lt)
        i=i+1
        j-=i
print(s)