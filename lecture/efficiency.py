# Time efficiency
# It's extremely important to write memorized functions especially in a tree recursion

def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        else:
            return cache[n]
    return memoized

# Common Orders of Growth
# Exponential growth. e.g., recursive fib  note that square(exp(b,n//2)) if b is even, when the case b is odd:exp(b,n-1)
# O(b^n)
# saves half of the computation
# Quadratic growth  e.g., overlap  O(n^2)
# Linear growth e.g., slow exp  O(n)
# Logarithmic growth e.g, exp_fast O(log n)
# Constant growth. Increasing n doesn't affect time  O(1)

# Space efficiency


def count_frames(f):
    counted.open_count, counted.max_count = 0, 0

    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    return counted
