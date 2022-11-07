random = [1, 3, 5, 6, 7, 8, 9, 19]
# list used everywhere in python
exp = [2, 7] + random*2


def count(s, value):
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

# sum up function recursively, this is typical how to sum up list


def my_sum(L):
    if L == []:  # base case
        return 0
    # return the first + recursive fuc start from 1(take away current 0)
    return L[0] + my_sum(L[1:])


def sum(L):  # iterate version
    total = 0
    for i in range(len(L)):
        total += L[i]
    return total

# find divisors for a specific integer(elegent), and quite useful


def divisor(n):
    return [1]+[x for x in range(2, n)if n % x == 0]


def reverse(s):
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]
# t[-1] means the last elements in list of t(equivelent t[1:len(t)-1] = t[1:-1])
# common and dif bettween range and list( i actually prefer range since comsumes less memory)
# container is something that contains elements
# recursive function avoid assignment by using function calls
