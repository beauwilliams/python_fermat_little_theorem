import sys

a_in = input ("Enter a number for a: ")
p_in = input ("Enter a number for p: ")

a = int(a_in)
p = int(p_in)

def gcd(a, b):
    '''This function computes fermats little theorem'''
    while b:
        a, b = b, a%b
    return a

print ("a=",a)
print ("p=",p)
print ("GCD(a,p)=",gcd(a,p))
print ("Result: ",(a**(p-1)) % p)
