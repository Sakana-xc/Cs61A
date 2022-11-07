# example of using data abstractor barrier, extremely important for large project
# layer of abstraction
def rational(n, d):
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select


def numer(x):
    return x('n')


def denom(x):
    return x('d')


# example of dictionary
numerals = {'I': 5, 'V': 5, 'X': 10}
