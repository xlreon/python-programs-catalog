"""Author - Sidharth Satapathy"""

# Problem 1
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Implementation of separate chaining hashing technique
# to get uniform distribution we take the size as a prime number

class HashTable:
    def __init__(self):
        self.size = 11   # Setting the size to prime number for uniform distribution
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def put(self,key,data):
        hashValue = self.hasFunction(key,len(self.slots))
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                nextSlot = self.rehash(hashValue,len(self.slots))
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot,len(self.slots))
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data
    def hasFunction(self,key,size):
        return key%size
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    def get(self,key):
        startslot = self.hasFunction(key,len(self.slots))
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data
    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self,key,data):
        self.put(key,data)

h = HashTable()

choice = 1
while choice == 1:
    key = int(input("Enter the key : "))
    data = input("Enter the value for the key : ")
    h[key] = data
    choice = int(input("Want to enter another value (1 - yes 2 - No) : "))