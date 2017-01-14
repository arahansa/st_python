class  Foo:
    def func1():
        print("func1")
    def func2(self):
        print(id(self))
        print("func2")


f = Foo()
f2 = Foo()
print(id(f))
print("== func1 == ")
print(Foo.func1())
print("== func2 == ")
print(f.func2())

print("== 클래스 직접 호출 ==")
print(id(f2))
print(Foo.func2(f2))