# hashTable
A basic hashTable with linear probing, implemented in Python 3.

## Premise
This hashtable implementation was built for the KPCB Fellows 2015 application. 

In its current form, this implementation is a fixed-size hashtable implemented in python via primitive types,
using linear probing and the native __hash__() function. 

## Properties

hashTable.bucket //The list containing the mapped nodes of our table

hashTable.keys //A set containing all keys initialized and active within the table

hashTable.size //An int value of how many elements exist within the table


hashTable.get(key) //Retrieves value stored in key

hashTable.set(key, value) //Sets value at key, if key exists updates destructively, if not then we create a new entry.

hashTable.delete(key) //Returns the value at key and deletes key from our table.

hashTable.load() //Returns the load factor as a decimal value e.g. .05 for 5% load.

