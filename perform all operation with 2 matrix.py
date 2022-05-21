import numpy as np
r,c = list(map(int,input().split()))
m1 = []
m2 = []
for i in range (r):
    ele = list(map(int,input().split()))
    m1.append(ele)
for i in range(r):
    ele = list(map(float,input().split()))
    m2.append(ele)
m1 = np.array(m1)
m2 = np.array(m2)
out = np.add(m1,m2)
out1 = np.subtract(m1,m2)
out2 = np.floor_divide(m1,m2)
out3 = np.multiply(m1,m2)
out4 = np.power(m1,m2)
out5 = np.mod(m1,m2)
print(out)
print(out1)
print(out2)
print(out3)
print(out4)
print(out5)