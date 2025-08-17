class MyHashSet:
    def __init__(self):
        self.set = {1, 2, 3}

    def add(self, key: int) -> None:
        self.set.add(key)

    def remove(self, key: int) -> None:
        self.set.remove(key)

    def contains(self, key) -> bool:
        for i in self.set:
            if i == key:
                return True

        return False


if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    obj.remove(2)
    print(obj.contains(2))
