# lecture 8 Recursive
# It's a loop that calls the function itself
# The can loop without a for/while statement


def split(n):
    return n//10, n % 10


def sum_digits(n):

    if n < 10:
        return n
    # return two integers, the order of variables matters
    all_but_last, last = split(n)
    return sum_digits(all_but_last)+last
    # might be confusing why not return n instead of n+ last in the end
    # if n < 10:
    #     return n
    # else:
    #     all_but_last, last = spit(n)
    # return sum_digits(all_but_last)+last

    # fact exaple


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


# def fact_while(n):
#     k, total = 1, 1
#     while k <= n:
#         total, k = total*k, k+1
#         return total

# The luhn algorithm, used to verify the correctness of creaditcard
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
# since luhn_sum_double called with argument(all_but_last)
# eg luhn_sum(123) -> luhn_sum_double(12) ->  function luhn_digits = sum_digits(2*last), it doubles every other digits of n
# and because if 2* last > 10, sum_digits takes care of it, so it fits the rule of luhn algo


def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

# difference between print and return:
# print just shows the human user a string representing what is going on inside the computer.
# The computer cannot make use of that printing. return is how a function gives back a value.
# This value is often unseen by the human user, but it can be used by the computer in further functions.


# def inverse_cascade(n):
#     if n < 10:
#         print(n)
#     else:
#         print(n % 10)
#         inverse_cascade(n // 10)
#         print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


def grow(n): return f_then_g(grow, print, n//10)
def shrink(n): return f_then_g(print, shrink, n // 10)

# Tree_shaped process arise whenever excuting the body of a recursive
# function makes more than one call to that function


# Tree Recursion eg: computing fib
# Tree sturcture computation can take a while for exaple when do fib(35)
# This is not the efficient way to compute fib


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)


# def fib_all(n):
#     i = 0
#     for i in range(n):
#         print(fib(i))
#         i += 1

def print_fib(n):
    if n == 0:
        return 0
    print(fib(n))
    return print_fib(n-1)
    # the number is inversed

# Countig Partitions
# postive integer, parts up to size m, su of positive integer
# parts up to m in increasing oder
# Tree recursion often involves exploring different choices


def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m


def find_pairs(nums):
    ans = []
    nums.sort()
    l, r = 0, len(nums)-1
    for i in range(len(nums)):
        while l <= r:
            m = l + (r-l)//2
            if nums[m]-nums[i] > 2:
                r = m-1
            elif nums[m]-nums[i] < -2:
                l = m+1
            else:
                ans.append([nums[m], nums[i]])
        return ans
