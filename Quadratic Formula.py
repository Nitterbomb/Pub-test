import cmath
a = float(input("Enter the value of a ="))
b = float(input("Enter the value of b ="))
c = float(input("Enter the value of c ="))
discriminant = b**2 - 4*a*c
solution1 = (-b + cmath.sqrt(discriminant))/(2*a)
solution2 = (-b - cmath.sqrt(discriminant))/(2*a)
print('The solutions are {0} and {1} '.format(solution1,solution2))
