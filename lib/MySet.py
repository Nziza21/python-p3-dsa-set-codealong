class MySet:
    def __init__(self, initial_list=None):
        self.dictionary = {}
        if initial_list:
            for item in initial_list:
                self.dictionary[item] = True

    def add(self, item):
        self.dictionary[item] = True

    def delete(self, item):
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        return item in self.dictionary

    def size(self):
        return len(self.dictionary)


    def clear(self):
        self.dictionary = {}

    def __str__(self):
        items_str = ', '.join(map(str, self.dictionary.keys()))
        return f'MySet: {{{items_str}}}'