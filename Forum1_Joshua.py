import math
from fractions import Fraction as frac

Num = int(input("Enter the numerator value(VALUE SHOULD BE > 0): "))
while Num <= 0:
    Num = int(input("Enter the numerator, value MUST be > 0: "))
    if Num > 0:
        break

Den = int(input("Enter the denominator value(VALUE SHOULD BE > 0): "))
while Den <=0 :
    Den = int(input("Enter the denominator, value MUST be > 0: "))
    if Den > 0:
        break

gcd = math.gcd(Num, Den)
a = Num//gcd
b = Den//gcd

if Num < Den:
    print(f"{Num}/{Den} is a proper fraction.")
    if gcd !=1:
        print("This proper fraction can be simplified to: ", frac(a, b))
    else:
        print("This is a proper fraction and cannot be simplified any further.")
elif Num >= Den:
    print(f"{Num}/{Den} is an improper fraction.")
    if gcd != 1:
        print("This improper fraction can be simplified to: ", frac (a, b))
    else: 
        print("This improper fractionn could not be simplified any further. ")
    mixnum = a//b
    if Num%Den == 0 :
        print(f"The whole number is {mixnum}")
    else:
           a = a-(b*mixnum)
           print(f"The mixed number is {mixnum} and", frac (a,b))