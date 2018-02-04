""" Author - Sidharth Satapathy """
""" This code is in python 2 """

class HashTable(object):

    def __init__(self,size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self,key,data):

        hashvalue = self.makeHash(key,self.size)

        if self.slots[hashvalue] == None :
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else :
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:

                newhash = self.reHash(hashvalue,self.size)

                while self.slots[newhash] != None and self.slots[newhash] != key:
                    newhash = self.reHash(newhash,self.size)

                if self.slots[newhash] == None:
                    self.slots[newhash] = key
                    self.data[newhash] = data
                else: self.data[newhash] = data

    def get(self,key):
        start = self.makeHash(key,self.size)
        data = None
        stop = False
        found = False
        position = start
        
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.reHash(position,self.size)
                if position == start:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self,key,data):
        self.put(key,data)            


    def makeHash(self,key,size):
        return key%size
    def reHash(self,oldhash,size):
        return (oldhash+1)%size            

n = int(raw_input("Enter the size of the Hash table you want to create :"))

h = HashTable(n)

for i in range(n):
    key = int(raw_input("Enter an integer key :"))
    value = raw_input("Enter the value :")
    h[key] = value

getValue = raw_input("Enter the key you want to get value of :")

print "Value for key "+getValue+" is "+h[int(getValue)]

