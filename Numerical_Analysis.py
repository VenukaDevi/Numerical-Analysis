#Bisection method
def f(x):
    return(x*x*x)-x-1
for i in range(1,6):
    print(f(i)+ +i)
print("root lies between")
for i in range(1,6):
    if((f(i)<0) and (f(i+1)>0)):
        a=i
        b=i+1
        print(a)
        print(b)
while(round(a,4)!=round(b,4)):
    x=(a+b)/2
    if(f(x)<0):
        a=x
    else:
        b=x
print("success")
print("the root is",round(x,5))
