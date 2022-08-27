def divis(num):
    t=num
    list=[]
    while t!=1:
        
        if num%t ==0:
            #print('divisible by ' +str(t))
            list.append(num)
        t-=1
    return len(list)

c=1
f=int(input('up to what number? '))

while c!=f:
    if divis(c) ==1:
        print(c)
    c+=1    
input()
