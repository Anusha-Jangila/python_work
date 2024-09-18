class Jar:
    def __init__(self, capacity=12):
        if not capacity >= 0:
            raise ValueError("Not a non-negative integer")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        str = ""
        for _ in range(self.size):
            str = str + "🍪"
        return str

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Exceeds the cookie jar capacity")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not that many cookies in the cookie jar")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n


