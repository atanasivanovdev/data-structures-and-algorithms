class HashTable:
    def __init__(self, size) -> None:
        self.data = [None] * size

    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value
    
    def set(self, key, value):
        index = self._hash(key)
        if not self.data[index]:
            self.data[index] = []

        if len(self.data[index]) >= 1:
            for item in self.data[index]:
                if item[0] == key:
                    raise KeyError("The key already exists in the hash table")
                
        self.data[index].append([key, value])
        return self.data
    
    def get(self, key):
        index = self._hash(key)
        if self.data[index] and len(self.data[index]) >= 1:
            for item in self.data[index]:
                if item[0] == key:
                    return item[1] 
        elif self.data[index]:
            return self.data[index][0][1]
        return None
    
    def __getitem__(self, key): 
        return self.get(key)
    
    def __setitem__(self, key, value):
        return self.set(key, value)

myHashTable = HashTable(10)
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))
myHashTable['apples'] = 9
print(myHashTable['apples'])