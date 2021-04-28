# coding: utf-8


class Queue:
    def __init__(self):
        self.data = []

    def put(self, elem):
        self.data.append(elem)

    def get(self):
        res = self.data[0]
        del self.data[0]
        return res

    def is_empty(self):
        return len(self.data) == 0

    def clear(self):
        self.data.clear()
