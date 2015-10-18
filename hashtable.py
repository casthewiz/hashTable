
class node:
    key = ""
    value = 0

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def set(self, value):
        self.value = value


    def output(self):
        print("'" + self.key + "' : '" + self.value + "'")


class hashTable:
    # bucket is the container for all nodes
    bucket = []
    # we maintain a set of all keys to check for unique vals.
    # this way, we don't have to handle checking
    # at insert during hash function. Spatial tradeoff for speed & convenience.
    keys = set([])
    # cap size of hashTable. Fixed, set at instantiation
    size = 0
    __loadSum = 0
    # load value
    __loadFactor = 0.0

    # takes in size
    def __init__(self, size):
        self.size = size
        self.bucket = [None] * size

    #we recalculate load on every operation
    #this function gets called at set operations and delete operations
    def __loadCalc(self):
        if (self.size == 0):
            __loadFactor = 0
        else:
            self.__load = self.__loadSum/self.size

    # returns value associated with key
    def get(self, k):
        if (k in self.keys):
            i = 1
            hashed = hash(len(k)) % 1
            while(self.bucket[hashed] != None):
                if(self.bucket[hashed].key != k):
                    hashed = hash(len(k)) % i
                    i += 1
                else:
                    return self.bucket[hashed].value
            return None
        else:
            return None

    # sets value at given key. returns boolean indicating success or failure
    # we use linear probing for collision resolution
    def set(self, k, v):
        k = str(k);
        if (self.__loadFactor == 1):
            return False
        elif (k in self.keys):
            i = 1
            hashed = hash(len(k)) % 1
            while(self.bucket[hashed] != None):
                if(self.bucket[hashed].key != k):
                    hashed = hash(len(k)) % i
                    i += 1
                else:
                    self.bucket[hashed].value = v
                    return True
        else:
            newNode = node(k, v)
            i = 1;
            hashed = hash(len(k)) % i;
            while(self.bucket[hashed] != None):
                hashed = hash(len(k)) % i
                i += 1
            self.bucket[hashed] = newNode
            self.keys.add(k)
            self.__loadSum += 1
            self.__loadCalc()
            return True


    # deletes value at given key. returns value.
    def delete(self, k):
        if (k in self.keys):
            i = 1
            hashed = hash(len(k)) % 1
            while(self.bucket[hashed] != None):
                if(self.bucket[hashed].key != k):
                    hashed = hash(len(k)) % i
                    i += 1
                else:
                    tmp = self.bucket[hashed].value
                    self.bucket[hashed] = None
                    self.keys.remove(k)
                    self.__loadSum -= 1
                    self.__loadCalc()
                    return tmp;
            return None
        else:
            return None

    #returns load
    def load(self):
        return self.__load
