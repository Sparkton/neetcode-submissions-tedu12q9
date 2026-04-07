class MyHashMap:

    def __init__(self):
        self.ls = []

    def contains(self, key: int) -> (bool, int):
        for idx in range(len(self.ls)):
            if self.ls[idx][0] == key:
                return (True,idx)
        return (False, -1)
    
    def put(self, key: int, value: int) -> None:
        check = self.contains(key)
        if not check[0]:
            self.ls.append([key, value])
        else:
            self.ls[check[1]] = [key, value]

    def get(self, key: int) -> int:
        check = self.contains(key)
        if check[0]:
            return self.ls[check[1]][1]
        return check[1]

    def remove(self, key: int) -> None:
        check = self.contains(key)
        if check[0]:
            del self.ls[check[1]]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)