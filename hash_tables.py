class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        idx = None
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                idx = index
                break
    
        if found_key:
            bucket[idx] = (key, val)
        else:
            bucket.append((key, val))
    
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            return record_val
        else:
            return 'key not found'
        
    def del_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        idx = None
        for index, record in enumerate(bucket):
            record_key, reocrd_val = record
            if record_key == key:
                found_key = True
                idx = index
                break
            
        if found_key:
            bucket.pop(idx)

    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)
    
if __name__ == "__main__":
    hash_table = HashTable(50)

    hash_table.set_val('example.com', 99)
    print(hash_table)

    hash_table.set_val('second.example.com', '100')
    print(hash_table)

    hash_table.get_val('example.com')
    hash_table.del_val('example.com')
    print(hash_table)


# Time Complexity get: O(1) insert: O(1)
