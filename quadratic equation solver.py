
import cmath

a=int(input("enter coeffecient of x^2:"))
b=int(input("enter coeffecient of x:"))
c=int(input("enter constant:") ) 

if a==0 :
   print("invalid input")

else :
      d = (b**2) - (4*a*c)
      if d>0 :
       z=print("Discriminant  :",d)

      else :
       print("imaginary roots and Discriminant:",d)

x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

print('The roots are ',x1,'and',x2)

