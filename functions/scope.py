def fun1(num):
    def fun2(x):
        return x ** num
    return fun2

f1 = fun1(2)
f2 = fun1(3)

print(f1(2))
print(f2(2))