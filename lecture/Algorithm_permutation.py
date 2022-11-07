def permutation(s):
    if len(s) == 0:
        yield []
    for i in range(len(s)):
        start = s[i]
        rest = s[:i] + s[i+1:]
        # rest = s[j] for j in range(len(s)) if j != i
        for rest_permutation in permutation(rest)
        return [start + rest_permutation]


def binary_iter(arr, start, end, target):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < target:
            start = mid+1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

# memory


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

# example of tree recursive, an exchange case:


def count_change(a, kinds=(50, 25, 10, 5, 1)):
    # while amount == 0, there is one way to exchange
    # while amount or cash type < 0, there is no way to exchange
    # so the base case will be :
    if a == 0:
        return 1
    if a < 0 or len(kinds) <= 0:
        return 0
    exchange_with = kinds[0]
    # break into two senario: pay with 50 or not, then bring down to the base case
    return count_change(a, kinds[1:])+count_change((a-exchange_with), kinds)

# algoritum takes less resource:


def square(x):
    return x*x


def fast_exp(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_exp(b, n//2))
    else:
        return b * fast_exp(b, n-1)

# once define a node, define a tree


class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ',{0},{1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)


def fib_tree(n):
    """Return a Tree that represents a recursive Fibonacci calculation."""
    if n == 1:
        return Tree(0)
    if n == 2:
        return Tree(1)
    left = fib_tree(n-2)
    right = fib_tree(n-1)
    return Tree(left.entry + right.entry, left, right)
