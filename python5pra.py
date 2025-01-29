#LOGICAL OPERATORS AND BITWISE OPERATORS
#logical-and,or and not 
#&&,!!,!
#and operators
print (True and True )
print (False and False )
print (False and (True and True and False) )
print (True and False )

print ('-----Numbers----')
print(45 and 36)
print(-24 and 45)
print(67 and "")
print("" and 65)
print(-48 and -35)
print( False and 49)

print( True and 399)
print( 78 and 67)
print( None and 49)
print ('-----or operators----')
print(True or False)
print(False or True)
print( False or (False and True))
print(True and ((False or True)and(True or False)))
print(55 or 333)
print(89 or 25)
print("" or True )
print(29 or 3 or 1 or 25)

print ('-----not operators----')

print(not True)
print(not False)
print(not(58 or 39))
print(not("" and 3 and 49))

#bitwise operators - &,|, ^, ~ , >>,<<
print(48 & 59)
print( 99 & 32)
print(38 & 78)
# bitwise or
print( 12 | 14)
print( 89 | 75)


print ('-----Xor operators----')
print(94 ^ 74)
print(87 ^ 45)
print( 39 ^ 33)
#left shift
print( 89<< 1)
print( 34<< 2)
print( 59<< 1)
print( 54<< 2)
print( 768<< 1)
print( 1886<<1)
#right shift
print(4>>54)
print( 3>> 4)
print( 955>> 665)
print( 32364>> 534)
print(0o01011>>0o0101)
# ~
print(~13)
print(~26)
print(~35)