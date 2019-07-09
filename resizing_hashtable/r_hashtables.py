

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity

# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hashNum = 5381
    for x in string:
        hashNum = (( hashNum << 5) + hashNum) + ord(x)
    return hashNum % max

# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = LinkedPair(key, value)
    if hash_table.storage[index] is None:
        hash_table.storage[index] = pair
        return
    current = hash_table.storage[index]
    while current.next is not None:
        if current.key != key:
            current = current.next
        else:
            current.value = value
            return
    if current.key == key:
        current.value = value
        return
    current.next = pair
    return

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        print("Error in Remove")
    current = hash_table.storage[index]
    prev = None
    while current is not None:
        if current.key == key:
            if prev:
                prev.next = current.next
                current.next = None
            else:
                hash_table.storage[index] = None
        prev = current
        current = current.next
    
            

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        return None
    current = hash_table.storage[index]
    while current is not None:
        if current.key == key:
            return current.value
        current = current.next
    return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_capacity = hash_table.capacity * 2
    new_storage = [None] * new_capacity

    # copy over elements
    for i in range(0, len(hash_table.storage)):
        new_storage[i] = hash_table.storage[i]

    hash_table.storage = new_storage
    hash_table.capacity = new_capacity


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    hash_t = hash_table_resize(ht)
    new_capacity = len(ht.storage)
    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
