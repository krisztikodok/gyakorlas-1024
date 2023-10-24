import random

#create a list of random numbers
x=[]
for _ in range(10): # _ is a placeholder
  x.append(random.randint(0,100)) #a random nr between 0 and 100 

print(x)
print("Első elem:",x[0])
print("Utolsó előtti elem:",x[-2])

for i in x:
  print(i)
n=len(x)
for i in range(5,n):
  print(x[i])