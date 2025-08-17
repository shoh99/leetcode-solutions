"""
Question Description:

Design a HashSet without using any built-in hash table libraries

Implement MyHashSet class:
  * void add(key) Inserts the value key into the HashSet
  * bool contains(key) Returns whether the value key exists in the HashSet or not
  * void remove(key) Removes the value in the HashSet. If key does not exists in
    the HashSet, do nothing.
"""


class MyHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            hash = self.get_hash(key)
            self.buckets[hash].append(key)

    def remove(self, key: int) -> None:
        hash = self.get_hash(key)
        bucket = self.buckets[hash]

        if key in bucket:
            bucket.remove(key)


    def contains(self, key: int) -> bool:
        hash = self.get_hash(key)
        for value in self.buckets[hash]:
            if value == key:
                return True

        return False

    def get_hash(self, key):
        return key % 1000


if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    print(obj.buckets)
    obj.add(2)
    print(obj.buckets)

    print(obj.contains(1))
    print(obj.contains(3))

    obj.add(2)
    print(obj.buckets)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.buckets)
    print(obj.contains(2))
