
#  FLOOR DIVISON

a=-5.0//2
print(a)

a=5.0//2
print(a)

a=9//4
print(a)

a=-5.0/2
print(a)

w=int(input('Enter the dividend : '))
o=int(input('Enter the divisor : '))
m=w//o
print('The floor value is : ', m)

#  LOGICAL OPERATORS
    #1 logical operator : and

i=2<3 and 4>3
print(i)

u=7<99 and 8>1
print(u)

t=631>23 and 98<1
print(t)

    #2 logical operator : or

i=2<3 or 4>3
print(i)

u=7>99 or 8>1
print(u)

t=631<23 or 98<1
print(t)

    #3 logical operator : and not

i=2<3 and not 4>3
print(i)

u=7<99 and not 8<1
print(u)

t=631<23 and not 98>1
print(t)

n=17>99 and not 8<1
print(n)

#  COMPARISON OPERATORS
    # == , != , < , > , <= , >=

k=2==3
print(k)

k=2!=3
print(k)

k=2<3
print(k)

k=2>3
print(k)

k=2<=3
print(k)

k=2>=3
print(k)

#   AREA OF CIRCLE

r=float(input('Enter the radius of the circle (in cm) : '))
ar=3.14*r*r
print("The area of the circle with radius, r = ",r,", is : ", ar, "sq.cm")
