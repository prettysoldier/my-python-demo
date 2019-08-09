"""
注解是在闭包的基础上实现的，传入的参数是一个函数
"""


def decorator_func(original_func):
    def wrapper_func():
        print("在执行{}函数之前，先执行wrapper".format(original_func.__name__))
        return original_func()  # 此处的return没有作用，可以去掉，更容易理解

    return wrapper_func


# 1.可以通过装饰函数来包裹
def func():
    print("hello")


# decorated_func = decorator_func(func)
# decorated_func()

# 2.可以通过 @函数名 来装饰其他函数


@decorator_func
def func2():
    print("world")


# func2()

# 2.如果要被注解的函数有参数
# 会报错 TypeError: wrapper_func() takes 0 positional arguments but 2 were given
# 修改装饰函数，如下：

def decorator_func2(original_func):
    def wrapper_func(*args, **kwargs):
        print("在执行{}函数之前，先执行wrapper".format(original_func.__name__))
        original_func(*args, **kwargs)

    return wrapper_func


@decorator_func2
def func3(name, age):
    print("hello {}, age={}".format(name, age))


func3('zhangsan', 5)


# 3.带参数的注解函数，可以装饰不带参数的函数，所以decorator_func2才是注解的完整各写法
@decorator_func2
def func4():
    print("hello")


func4()