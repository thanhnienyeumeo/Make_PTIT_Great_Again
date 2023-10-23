a = [1,2]
b = [3,4]
#a plus b = [4,6]
c = [a[i]+b[i] for i in range(len(a))]
print(c)