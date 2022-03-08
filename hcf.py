a= int(input("enter the first no."))
b=int(input("enter the second no."))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        r=i
        print("gcd",r)

