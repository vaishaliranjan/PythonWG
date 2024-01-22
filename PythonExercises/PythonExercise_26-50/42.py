x=[1,2,3]
y=(4,5,6)
for i in range(0,3):
    print(x[i]+y[i])

for i,j in zip(x,y):
    print(i+j)