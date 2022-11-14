class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = False
        self.encountered = set()
        self.elems = items
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        it = iter(self.elems)
        while True:
            try:
                curr = next(it)
            except:
                raise StopIteration
            else:
                if self.ignore_case == True and type(curr) == str:
                    curr = curr.lower()
                if curr not in self.encountered:
                    self.encountered.add(curr)
                    return curr

    def __iter__(self):
        return self

if __name__ == '__main__':
    lst2 = ['b', 'A', 'c', 'H', 'e', 'l', 'o', 'r', 'S', 'a', 'b', 'A', 'c', 'H', 'e', 'l', 'o', 'r', 'S', 'a']
    print(list(Unique(lst2, ignore_case=False)))