x=[]
print(x)
x=[1,2,3,4,'A',True,[1,2,33]]
print(x)
print(x[2:5])
x[3]=1+2j
print(x)
print(x[2:5])

y=[3,2,False]
print(y)
y.insert(2,100) #insert(index_nr,value)
print(y)
if False in y:
  print('yes')
else:
  print('no')
if 10 in y:
  print('yes')
else:
  print('no')