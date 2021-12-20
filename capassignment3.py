# BASIC CALCULATOR

print("Hello! Welcome to Basic Calculator. \n \n Kindly select the desired operation from the following:")

print("""a=add \n
b=sub \n
c=multiply \n
d=obtain quotient \n
e=obtain remainder \n
f=raise to power \n
g=check whether a no. is prime, composite or neither of them \n
h=generate table""")

a=str('a')
b=str('b')
c=str('c')
d=str('d')
e=str('e')
f=str('f')
g=str('g')
h=str('h')

l=str(input("Enter the alphabet corresponding to the desired operation : "))



if (l==a):
    i=float(input('Enter first no. : '))
    j=float(input('Enter second no. : '))
    print(i+j)
elif(l==b):
    i=float(input('Enter first no. : '))
    j=float(input('Enter second no. : '))
    print(i-j)
elif(l==c):
    i=float(input('Enter first no. : '))
    j=float(input('Enter second no. : '))
    print(i*j)
elif(l==d):
    i=float(input('Enter first no. : '))
    j=float(input('Enter second no. : '))
    print(i//j)
elif(l==e):
    i=float(input('Enter first no. : '))
    j=float(input('Enter second no. : '))
    print(i%j)
elif(l==f):
    i=float(input('Enter the no. : '))
    j=float(input('Enter the power no. : '))
    print(i**j)
elif(l==g):
    m=int(input('Enter the no. you wish to check : '))
    print(m)
    if (m==1):
        print('The no. is neither prime nor composite.')
    else:
        n=m-1
        check=0
        for k in range(2,n):
            o=int(m%k)
            if(o==0):
                check=check+1
                break
        if(check==0):
            print('The no. is prime.')
        else:
            print('The no. is composite.')
    
else:
    p=int(input('Enter a no. to generate table : '))
    print('The table of ',p,' is :')
    for q in range(1,11):
        r=p*q
        if(q<10):
            print(p,'  X  ',q,'  =  ',r)
        else:
            print(p,'  X  ',q,' =  ',r)
