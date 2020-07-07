class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = None

    def __str__(self):
        return(self.data)

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        count = 0
        for x in self.data:
            if x is not None:
                count += 1
        return count / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # Magic Constant: 5381
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Find the index in the hash table for the key
        i = self.hash_index(key)
        lst = self.data[i]
        # Search the list at that index for the key
        # If it exists:
        if lst is not None:
            newItem = HashTableEntry(key, value)
            cur = lst
            while cur is not None:
                if cur.key == key:
                    cur.value = value
                    return
                cur = cur.next
            newItem.next = lst
            self.data[i] = newItem
            # print(self.data[i].value)

        # Else it doesn't exist:
        else:
            # Make a new record (`HashTableEntry` class) with the key and value
            lst = HashTableEntry(key, value)
            # Insert it anywhere in the list
            self.data[i] = lst

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Find the index in the hash table for the key
        i = self.hash_index(key)
        # Search the list at that index for the key
        lst = self.data[i]
        # If it exists:
        if lst is not None:
            # Delete the entry from the linked list
            removed = lst.value
            lst.value = None
            # Politely return the deleted value
            return removed
        else:
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Find the index in the hash table for the key
        i = self.hash_index(key)
        # Search the list at that index for the key
        lst = self.data[i]
        # If it exists:
        if lst is not None:
            cur = lst
            while cur is not None:
                if cur.key == key:
                    #  Return the value
                    return cur.value
                cur = cur.next
            return None
        # Else it doesn't exist:
        else:
            #  Return `None`
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
