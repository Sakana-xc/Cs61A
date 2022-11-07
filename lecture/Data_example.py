def max_sum(s):

    for i in range(len(s)-1):
        #     max.append(s[i]+s[i+1])
        #     i += 1
        # list.sort(max)
        # return max[-1]
        max([s[i]+s[i+1] for i in range(len(s)-1)])


def digit_dict(s):
    {d: [x for x in s if x//10 == d]for d in range(10)
     if any([x//10 == d for x in s])}


def all_have_an_equal(s):
    min(s.count(x)for x in s) > 1


def at_least_one_equals(s):
    max(s.count(x) for x in s) > 1


def merge(s, t):  # merge two Linked lists in assending order
    # recursive
    if s is Link.empty:  # Link.first and Link.rest None
        return t
    if t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, (merge(s, t.rest)))


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ',' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ''
            self = self.rest
        return string + str(self.first) + '>'
