#Funksiyalar 

def f(x):
    if x < 0:
        return
    if x > 100:
        return
    print(x)


f(-3)
f(105)
f(64)
64


#Funksiya hər şey return edə bilər
def f():
    return ['foo', 'bar', 'baz', 'qux']
 

f()

f()[2]

f()[::-1]


# Python dict as an argument
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
            print(key, '->', val)


f(foo=1, bar=2, baz=3)



# Gonderilme tipi
def f(a, b, c):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'c = {c}')


d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f(**d)



# Hem *args hem *kwargs

"""
>>> def f(a, b, *args, **kwargs):
...     print(F'a = {a}')
...     print(F'b = {b}')
...     print(F'args = {args}')
...     print(F'kwargs = {kwargs}')
...

>>> f(1, 2, 'foo', 'bar', 'baz', 'qux', x=100, y=200, z=300)
a = 1
b = 2
args = ('foo', 'bar', 'baz', 'qux')
kwargs = {'x': 100, 'y': 200, 'z': 300}

"""




# Multi list sending
def f(*args):
    for i in args:
            print(i)


a = [1, 2, 3]
t = (4, 5, 6)
s = {7, 8, 9}

f(*a, *t, *s)



# Numune Concat
def concat(prefix, *args):
    print(f'{prefix}{".".join(args)}')


concat('//', 'a', 'b', 'c')

concat('... ', 'foo', 'bar', 'baz', 'qux')




# Canculyator funksiyasi yazin

#Docstring



def foo(bar=0, baz=1):
    """Perform a foo transformation.

    Keyword arguments:
    bar -- magnitude along the bar axis (default=0)
    baz -- magnitude along the baz axis (default=1)
    """
    return 5 * 6
 
 
print(foo.__doc__)   