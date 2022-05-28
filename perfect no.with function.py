def perfect(x):
    s = 0
    for i in range(1,x):
        if x%i==0:
          s = s+i
    if x==s:
        print('perfect')
    else:
        print('not perfect')
x = int(input())
perfect(x)