for i in range(1,11):
    a=i%2
    if(i<2 and a==1):
        print('10')
    elif(a==0):
        print(i-1)
    else:
        print(11-i)

print("Therefore, the values of x,y are : 2,9 respectively.")


"""
ALGORITHM:

STEP 1: Start
STEP 2: n = position of no. in sequence
STEP 3: determine whether 'n' is odd or even
STEP 4: If 'n' is odd, the number is: (11-n)
        If 'n' is even, the number is: (n-1)
STEP 5: End

"""
