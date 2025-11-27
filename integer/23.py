N=int(input())
h=N//3600
s=N%3600
m=s//60
s=m%60
print(h,m,s)