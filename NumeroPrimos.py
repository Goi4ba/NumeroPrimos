import random
r=random.randint( 4 , 21 )
a=[]
while r>1:
    numero=random.randint( 1 , 100001 )
    for i in [2,3,4,5,6,7,8,9]:
        if numero%i==0:
            r-=1
            a.append(numero)
resu=len(a)
if resu>0:
    print(a)
else:
    print('que não existem números primos nesta lista.')