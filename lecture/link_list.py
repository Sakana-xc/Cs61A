# many time it's recursive

class Link:
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


def range_link(start, end):
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start+1, end))


def add(s, v):
    assert s is not List.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    else:
        s.first < v:
        add(s.rest, v)  # recursive

    return s


class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
            self.branches = list(branches)
