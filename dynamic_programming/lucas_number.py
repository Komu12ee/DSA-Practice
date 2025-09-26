def lucas(n) :
  a=2
  b=1
  for i in range(n+1):
    if i==0:
      print(a)
    elif i==1:
      print(b)
    else:
      c=a+b
      print(c)
      a=b
      b=c
n=9
