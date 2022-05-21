y = {'A':{'age':16,'year':2000},

     'B':{'age':18,'year':1998}}
for x in y:
    print(x)
    for z in y[x]:
         print(z,':',y[x][z])