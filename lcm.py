a= int(input("enter the first no."))
b=int(input("enter the second no."))
for i in range(max(a,b),a*b+1):
    if i%a==0 and i%b==0:
        print("lcm",i)