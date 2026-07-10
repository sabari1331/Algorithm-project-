'''
#number
for i in range (0,100,1):
  if(i%3==0):
    continue
  print(i)
  '''
'''
#divisible by 9
for i in range (1,30):
 if (i%9==0):
   break
 print(i)
 '''
'''
#pass exactly 5
for i in range(1,6):
    if i==5:
     pass
    print(i)
'''
'''
#less than 1
for i in range(1,6):
    if(i>4):
     break
    print(i)
'''
'''
#print the PYTHON word except "H"
word="PYTHON"
for a in word:
    if a=="H":
      continue
    print(a,end="")
'''
'''
#PALINDROME
a=int(input("enter a number:"))
t=a
r=0
m=1
while t>0:
    d=t%10
    r=(r*10)+d
    t=t//10
if r==a:
 print(f"the result of given number (r)is palindrome")
else:
  print (f"the result of given number (r)is not palindrome")
'''