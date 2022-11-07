# view of a Dictionary
d = {'one': 1, 'two': 2, 'three': 3}
d['zero'] = 0
k = iter(d.keys())
z = iter(d.values())
i = iter(d.items())

# use an iterator in a for loop, eg print i in ri (range(3,6)), can only excuted once,
# next time it print nothing

bcd = ['b', 'c', 'd']
map(lambda x: x.upper(), bcd)
m = map(lambda x: x.upper(), bcd)


def double(x):
    print('**', x, '=>', x*2, '**')
    return 2*x

# A generator function is a function that yields values instead of
# returning them


def a_then_b(a, b):
    yield from a
    yield from b


def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)

# or
# def countdown(k):
#     if k > 0:
#         yield k
#         for x in countdown(k-1):
#             yield x


def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s


def factorial(x):
    if x == 1:
        return 1
    return x*factorial(x-1)

# a very powerful summation function


def summation(n, term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total
# last element always at index -1

# slice [start:stop:step]


s = 'abcdefgh'
s[::-1]  # the other way around

#  Newton's method
# Find f'(x) and define the newtons method
# Guess an initial value of x for the first iteration
# Substitute x in the NR equation and calculate x'
# If abs(x'-x)< tolerance, stop iteration and output the root: x,
# If the number of iterations reaches an assumed maximun,stop iteration


def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta)-f(x)
    return df/delta


def newton_update(f):
    def update(x):
        return x - f(x)/approx_derivative(f, x)
    return update  # this is how to get x where y close 0 within tolerence


def sum_even_fibs(n):
    """Sum the first n even Fibonacci numbers."""
    return sum(filter(iseven, map(fib, range(1, n+1))))


def iseven(x):
    return x % 2 == 0


def fib(k):

    if k in range(2):
        return k
    else:
        return fib(k-1)+fib(k-2)


# def acronym(name):
#     return tuple(map(first, filter(is_cap, name.split())))

def acronym(w):
    return tuple(w[0] for w in w.split() if is_cap(w))


def first(s):
    return s[0]


def is_cap(s):
    return len(s) > 0 and s[0].isupper()

# The reduce(fun,seq) function is used to apply a particular function passed in its argument
# Passed in the sequence. reduce is listed in functool (from functool import reduce)

# Mutable objects can change throughout the execution of a program

# <expression> . <name>
# 为了求解点表达式：

# 求出点左边的<expression>，会产生点运算符的对象。
# <name>会和对象的实例属性匹配；如果该名称的属性存在，会返回它的值。
# 如果<name>不存在于实例属性，那么会在类中查找<name>，这会产生类的属性值。
# 这个值会被返回，如果它是个函数，则会返回绑定方法。
# just like account_tom and account_jim


class CheckingAccount(account):

    withdraw_charge = 1  # this is called class attribute
    interest = 0.01

    def withdraw(self, amount):
        return account.withdraw(self, amount + self.withdraw_charge)
        # the class(account) is not defined
