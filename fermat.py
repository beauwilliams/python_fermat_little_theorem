import sys

print("Input two numbers to test if they are relatively coprime using Fermats Little Theorem")
print("Try the numbers 1763 & 86 for example and see what output we get!")
print("Ask yourself, why might that be?")
a_in = input ("Enter a number for a: ")
p_in = input ("Enter a number for p: ")

a = int(a_in)
p = int(p_in)

def gcd(a, b):
    '''This function computes fermats little theorem'''
    while b:
        a, b = b, a%b
    return a

result = (a**(p-1)) % p
print ("a=",a)
print ("p=",p)
print ("GCD(a,p)=",gcd(a,p))
print ("Result of FMT: ",result)

if result == 1:
    print("Relatively Comprime")
elif result != 1:
    print("NOT Relatively Comprime")
