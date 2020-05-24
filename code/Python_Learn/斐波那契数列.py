"""F(1)=1 
   F(2)=1
   F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
"""
def fib(n):
    a, b=0, 1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b

    print()

def fib2(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a, b=b, a+b

    return result

def add(a,b):
    return a+b

fib(1000)
print(fib2(100))

