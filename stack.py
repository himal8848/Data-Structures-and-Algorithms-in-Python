'''
Stack
Push/Pop element: O(1)
Search element by value:O(n)
Function calling in any programming language is managed by stack
Undo(Ctrl+Z) functionality in any editor uses stack to track down last set of operations
'''

# from collections import deque

# stack = [
#    "http://github.com/8848",
#     "https://www.facebook.com/himal.rawal.71",
#     "https://www.linkedin.com/in/himal-rawal-431030213/"
# ]

# stack.pop()
# print(stack)
#If we want to fetch the data but not remove it we use
# print(stack[-1])
'''
The issue with using a list as a stack is that list uses dymanic array internally and when 
it reaches its capacity it will reallocate a big chunk of memory somewhere else in memory 
area and copy all the elements. For example in below diagram if a list has a capacity of 
10 and we try to insert 11th element, it will not allocate new memory in a different memory 
region, copy all 10 elements and then insert the 11th element. So overhead here is (1) 
allocate new memory plus (2) copy all existing elements in new memory area
'''

# stack = deque()
# stack.append("http://github.com/8848")
# stack.append( "https://www.facebook.com/himal.rawal.71")
# stack.pop()
# print(stack)
# print(dir(stack))



# Implement Stack class using a deque
'''
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self,val):
        # return val[::-1]
        # or
        str = ""
        for i in val:
            str = i + str
        return str
    
    def is_balanced(self,exp):
        

s = Stack()
s.push("http://github.com/8848")
s.push("http://github.com/8848")
print(s.container)
print(s.size())

string = "We will conquere COVID-19"
print(f"The reverse string of {string} is {s.reverse_string(string)}")
'''

'''
Write a function in python that checks if paranthesis in the string are balanced or not.
 Possible parantheses are "{}',"()" or "[]". 
'''
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))