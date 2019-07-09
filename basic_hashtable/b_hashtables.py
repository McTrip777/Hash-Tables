

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity

# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hashNum = 5381
    for x in string:
        hashNum = (( hashNum << 5) + hashNum) + ord(x)
    return hashNum % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = hash_table.storage[index]
    if pair is  not None:
        print("Error inserting")
    else:
        hash_table.storage[index] = Pair(key, value)
        
# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        hash_table.storage[index] = None
    else:
        return print("That doesn't exist")
    
    
# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    pair = hash_table.storage[index]
    if pair is None:
       return None 
    return pair.value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
