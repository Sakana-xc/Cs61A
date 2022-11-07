# List can contain list as elements
pair = [1, 2]

nested_list = [[1, 2], [], [[3, False, None], [4, lambda:5]]]
# slice eg odd[1:3]

# implementing the tree Abstraction


def tree(lable, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [lable]+list(branches)


def lable(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    # leaf is a tree with a lable and an empty branch
    return not branches(tree)

# case when tree recursive themselves


def count_leaves(t):
    if is_leaf(t):
        return 1
    return sum([count_leaves(b) for b in branches(t)])


def fib_tree(n):
    if n <= 1:
        return tree(n)
    left, right = fib_tree(n-2), fib_tree(n-1)
    return tree(lable(left)+lable(right), [left, right])


# case to build an increamental tree


def increment_tree(t):
    if is_leaf(t):
        return tree(lable(t)+1)
    else:
        # assume increment_tree(t)solves this somehow
        bs = [increment_tree(b) for b in branches(t)]
        # lable is the same cuz function only increase the leaves
        return tree(lable(t))+bs


def increment(t):
    return tree(lable(t)+1, [increment(b)for b in branches(t)])

# print lables use indentations


def print_tree(t, indent=0):
    print(''*indent, lable(t))
    for b in branches(t):
        print_tree(b, ''*indent+1)


numbers = tree(3, [tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])


def sum_leaves(t, so_far):
    so_far = so_far+lable(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            sum_leaves(b, so_far)


# case when try to sum up list
sum([1],[2,3]) #will return an erorr since python do 0+[1]+[2,3]
sum([1], [2, 3], []) #solves this 
