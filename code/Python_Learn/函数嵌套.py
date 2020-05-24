def func_lib():
    def add(x,y):
        return x+y
    return add

fadd=func_lib()
print(fadd(1,2))
'''python中一切皆是对象'''