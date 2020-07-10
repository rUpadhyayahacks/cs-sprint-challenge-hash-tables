#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.key = source # treat as key
        self.value = destination # value


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur
            
            cur = cur.next
        
        return None
    
    def delete(self, key):
        cur = self.head

        if cur.key == key:
            self.head = self.head.next
            return cur

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return cur
            
            else:
                prev = prev.next
                cur = cur.next



class HashTable:
    MIN_CAPACITY = 8
    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [LinkedList()] * self.capacity 
        self.load = 0
        # this gives methods access to the array 


        # print("hello", self.capacity)

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


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        
        return hash


    def hash_index(self, key): # hashing function
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        # create key 
        # self.hash stores it at a specific index within your created array
        # the key now points at an index
        # then add a value to the key to create key/value pair

        # get index of the passed in key
        # Find the slot for the given key
        index = self.hash_index(key) 

        # Search the LinkedList
        current = self.storage[index].find(key)
        if current is not None:
            current.value = value
        else:
            self.storage[index].insert_at_head(Ticket(key, value))
            self.load += 1

        # store the value at the index
        # self.storage[index] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        if not key:
            print("Key does not exist")
        else:
            index = self.hash_index(key)
            self.load -= 1
            return self.storage[index].delete(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        hash_value = self.storage[index]

        if self.storage[index] is not None:
            desired = hash_value.find(key)
            if desired is not None:
                return desired.value
        
        return None



def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []

    ht = HashTable(length)

    # has the tickets
    for each in tickets:
        ht.put(each.key, each.value)
    
    # start where source is NONE
    current = ht.get("NONE")
    # print(current)

    # assign that destination as the first in the route
    route.append(current)

    while current != "NONE":
        for i in range(1, length):
            current = ht.get(current)
            route.append(current)
        
    
    return route
