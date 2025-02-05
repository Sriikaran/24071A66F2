def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return abs(a*b)//gcd(a,b)

print(gcd(12,15))
print(lcm(12,15))