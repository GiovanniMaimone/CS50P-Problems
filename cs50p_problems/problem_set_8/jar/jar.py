class Jar:
    def __init__(self, capacity=12, cookies=0):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        if cookies < 0 or cookies > capacity:
            raise ValueError
        self._cookies = cookies

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self._cookies += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self._cookies -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
