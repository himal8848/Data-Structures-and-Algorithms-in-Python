#Hash Table implementation(Internal Working of Dictionary in Python)

stock_prices = []
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])

print(stock_prices)

print(stock_prices[0])

#Find stock price on March 9

for element in stock_prices:
    if element[0] == 'march 9':
        print(element[1])
#Complexity of search using a list is O(n)

#Process using python dictionary

stock_prices = {}
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices['march 9'])

# Complexity of search using dictionary is O(1)
# Implement Hash Table

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100

print(get_hash('march 6'))

#Implementation of Hash Table
class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420

print(t.arr)