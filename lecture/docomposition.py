# case: bulild a yielp like app to search restaurants

def search(qury, ranking=lambda r: -r.stars):
    result = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)  # asending ording, so -r
# creat a Class call Restarurant:


def reviewed_both(r, s):
    return len(x for x in r.reviwers if x in s.reviwers)


class Restaurant:
    all = []

    def __init__(self, name, stars, reviewers):
        self.name, self.stars = name, stars
        self.reviewers = reviewers
        # puts what ever instance creat into all list
        Restaurant.all.append(self)

    def similar(self, k, similarity=reviewd_both):
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: -similarity(self, r))[:k]

    def __repr__(self):
        return '<' + self.name + ">"

# Linear -Time intersection of sorted list


def fast_overlap(s, t):
    i, j, count = 0, 0, 0
    while i < len(s) and t < len(t):  # either of these reach to the end the loop ends
        if s[i] == t[j]:
            i, j, count += 1, 1, 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count
