p = int(input("enter value for the original amount invested\n"))
n = int(input("enter value for number of years\n"))
r = 0.07
a = p * (1 + r) ** n
print( "amount deposit for ", n )
print( "amount deposit is", a )
