"""
Question:
    Design a HashMap without using any built-in hash table libraries.
    Implement the MyHashMap class:
        * MyHashMap() initializes the object with an empty map
        * void put(int key, int value) inserts (key, value) pair into the HashMap. if the key already exists in the map,
            update the corresponding value
        * int (get key) returns the value to which the specific key is mapped , or -1 if this map contains no mapping for
         the key.
        * void remove(key) removes key and its corresponding value if the map contains the mapping for the key.
"""


class MyHashMap:
    def __init__(self):
        self.my_map = [[] for _ in range(1000)]

    def put(self, key: int, value: int):
        bucket = self.my_map[self._hash(key)]

        for idx in range(len(bucket)):
            if bucket[idx][0] == key:
                bucket[idx][1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        bucket = self.my_map[self._hash(key)]

        for idx in range(len(bucket)):
            if bucket[idx][0] == key:
                return bucket[idx][1]

        return -1

    def remove(self, key):
        bucket = self.my_map[self._hash(key)]

        for idx in range(len(bucket)):
            if bucket[idx][0] == key:
                bucket.pop(idx)
                return

    def _hash(self, key):
        return key % 1000


if __name__ == "__main__":
    my_hash_map = MyHashMap()
    print(my_hash_map.remove(2))
    print(my_hash_map.put(3, 11))
    print(my_hash_map.put(4, 13))
    print(my_hash_map.put(15, 6))
    print(my_hash_map.put(6, 15))
    print(my_hash_map.put(8, 8))
    print(my_hash_map.put(11, 0))
    print(my_hash_map.get(11))
    print(my_hash_map.put(1, 10))
    print(my_hash_map.put(12, 14))
    print(my_hash_map.get(11))
    print(my_hash_map.get(10))