"""
转：https://www.cnblogs.com/xiaozao/p/9594069.html

"""
# 1.值传递和引用传递的问题？
# a = 2
#
#
# def f(x):
#     x = 3
#
#
# f(a)
# print(a)
# 答案是a=2，a的值不会被改变
"""
2.global的作用：
    在函数内部可以访问全局变量
    在函数内部不能修改全局变量的值，会报错
    在函数内部可以重新定义一个变量与全局变量的名字相同，此时会覆盖全局变量，相当于是两个变量，全局变量的值不受影响
    如果用global修饰变量，就可以修改全局变量的值
"""
# variable = 100
#
#
# def function():
#     global variable
#     variable += 100
#     print('inner: %d' % variable)
#
#
# print('outer beforeL: %d' % variable)
# function()
# print('outer after: %d' % variable)
"""
3.连续调用函数4次，每次输出的值都是4，即3+1，这说明每次调用fun函数之后，函数内部定义局部变量num就被销毁了，
没有保存下来，说明函数的局部作用域被销毁了。那如果要保存函数的局部变量，怎么办呢？引入“闭包”。
"""

# def fun(step):
#     num = 1
#     num += step
#     print(num)
#
#
# i = 1
# while i < 5:
#     fun(3)
#     i += 1


"""
4.闭包——装饰器的本质也是闭包
“闭包”的本质就是函数的嵌套定义，即在函数内部再定义函数，如下所示。
“闭包”有两种不同的方式，第一种是在函数内部就“直接调用了”；第二种是“返回一个函数名称”。
"""


# 第一种
# def Maker(name):
#     num = 100
#
#     def func1(weight, height, age):
#         weight += 1
#         height += 1
#         age += 1
#         print(name, weight, height, age)
#
#     # 在内部就直接调用“内部函数”
#     func1(100, 200, 300)
#
#
# # 调用外部函数，输出 feifei 101 201 301
# Maker('feifei')


# 第二种
# def Maker(name):
#     num = 100
#
#     def func1(weight, height, age):
#         weight += 1
#         height += 1
#         age += 1
#         print(name, weight, height, age)
#
#     return func1  # 此处不直接调用，而是返回函数名称（Python中一切皆对象）
#
#
# Maker('feifei')(100, 200, 300)


# “闭包”的作用——保存函数的状态信息，，如下。使函数的局部变量信息依然可以保存下来
def marker(step):  # 包装器

    num = 1

    def fun1():  # 内部函数

        nonlocal num  # nonlocal关键字的作用和前面的local是一样的，如果不使用该关键字，则不能在内部函数改变“外部变量”的值
        num = num + step  # 改变外部变量的值（如果只是访问外部变量，则不需要适用nonlocal）
        print(num)

    return fun1


j = 1
func2 = marker(3)  # 调用外部包装器
while j < 5:
    func2()  # 调用内部函数4次 输出的结果是 4、7、10、13
    j += 1

"""
4.nonlocal关键字的作用
该关键字的作用，就是让“内部函数”可以修改“外部函数（装饰器）”的局部变量值。详细信息这里不做讨论。
"""