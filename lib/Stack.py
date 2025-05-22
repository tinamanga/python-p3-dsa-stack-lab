class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, value):
        if self.limit is not None and len(self.items) >= self.limit:
            return  
        self.items.append(value)
        
    def pop(self):
        if not self.items:
           return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

   
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return self.limit is not None and len(self.items) >= self.limit

    def search(self, value):
        try:
            index = len(self.items) - 1 - self.items[::-1].index(value)
            return len(self.items) - 1 - index
        except ValueError:
            return -1
