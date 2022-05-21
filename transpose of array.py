import numpy as np
r,c = list(map(int,input().split()))
ls = []
for i in range(r):
    ele = list(map(int,input().split()))
    ls.append(ele)
mat = np.array(ls)
print(mat)
out1 = np.transpose(mat)
out2 = mat.flatten()
print(out1)
print(out2)