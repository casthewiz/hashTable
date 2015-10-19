from hashtable import *
from random import randint
testList  =  []

LOW       =  10
STANDARD  =  100
HIGH      =  10000
MEGA      =  100000

h1 = hashTable(LOW)
h2 = hashTable(STANDARD)
h3 = hashTable(HIGH)
h4 = hashTable(MEGA)

testList.append(h1)
testList.append(h2)
testList.append(h3)
# NOTE: below hashTable takes roughly !!80!! seconds to initialize when profiled with cProfile. Not reccomended.
# testList.append(h4)

def fillTest(h):
    i = 0
    while(h.set(i, i) == True):
        i += 1
    return(h.load() == 1.0)

def randSetTest(h):
    i = randint(0,9)
    j = i + 1
    if(h.set(i,j)):
        return(h.get(i) == j)
    else:
        return False

def deleteTest(h):
    i = randint(0,9)
    if (h.delete(i) == None):
        return False
    else:
        return True

def runTests(h):
    print("TEST: Filling all available key slots")
    if(fillTest(h)):
        print("SUCCEEDED")
    else:
        print("FAILED")
        return False

    print("TEST: Setting existing key to different value")
    if(randSetTest(h)):
        print("SUCCEEDED")
    else:
        print("FAILED")
        return False

    print("TEST: Deleting existing key value pair")
    if(deleteTest(h)):
        print("SUCCEEDED")
    else:
        print("FAILED")
        return False

    return True

for h in testList:
    print("Starting new test suite:")
    if((runTests(h))):
        print("TEST SUITE PASSED")
    else:
        print("TEST FAILED, TERMINATING EXECUTION")
        break
    print("")
