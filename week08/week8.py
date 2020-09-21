作业一:区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
容器序列 ： list, tuple, collections.deque
扁平序列 : str
可变序列 : list,dict,collections.deque
不可变序列 : str, tuple


作业二:自定义一个 python 函数，实现 map() 函数的功能
def my_map(func,*iterable):
    if hasattr(func,'__call__') == False:
        raise TypeError('the first arg must be function')
    for i in iterable:
        if hasattr(i,'__iter__') == False:
            raise TypeError('arg must be iterable')
    for args in zip(*iterable):
        yield func(*args)

def add(*args):
    return sum(args)

result = my_map(add,range(5),[5,6,2,4,8])
print(list(result))


作业三：实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        start = time.time()
        print(f'开始时间:{start}')
        result = func(*args,**kwargs)
        end = time.time()
        print(f'结束时间:{end}')
        total = f'{func.__name__}的运行时间:{end - start}'
        print(total)
        return result  
    return inner

@timer
def add(*args):
    return sum(args)
print(add(2,8,6))
