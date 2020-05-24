def sum(a,n):
    result,t=0,0
    for i in range(n):
        t=t*10+a
        result+=t
    return result

a=int(input("请输入a值:"))
n=int(input("请输入n值"))
print(sum(a,n))