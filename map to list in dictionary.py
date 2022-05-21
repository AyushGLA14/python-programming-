name = []
age = []
name = list(map(str,input().split()))
age = list(map(int,input().split()))
dictionary = dict(zip(name,age))
print(dictionary)
