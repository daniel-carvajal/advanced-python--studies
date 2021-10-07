'''

source: https://towardsdatascience.com/5-advanced-features-of-python-and-how-to-use-them-73bffa373c84

(1) Lambda functions

A Lambda Function is a small, anonymous function — anonymous in the sense that it doesn’t actually have a name.

Python functions are typically defined using the style of def a_function_name() , but with lambda functions we don’t give it a name at all. We do this because the purpose of a lambda function is to perform some kind of simple expression or operation without the need for fully defining a function.

A lambda function can take any number of arguments, but must always have only one expression:

'''

x = lambda a, b : a * b
print(x(5, 6)) # prints '30'

x = lambda a : a*3 + 3
print(x(3)) # prints '12'


'''
See how easy that was! We performed a bit of basic math without the need for defining a full-on function. This is one of the many features of Python that makes it a clean and simplistic programming language to use.



(2) Maps

Map() is a built-in Python function used to apply a function to a sequence of elements like a list or dictionary. It’s a very clean and most importantly readable way to perform such an operation.


'''

def square_it_func(a):
    return a * a

x = map(square_it_func, [1, 4, 7])
print(x) # prints '[1, 16, 49]'

def multiplier_func(a, b):
    return a * b

x = map(multiplier_func, [1, 4, 7], [2, 5, 8])
print(x) # prints '[2, 20, 56]'


'''
Check out the example above! We can apply our function to a single list or multiple lists. In fact, you can use a map with any python function you can think of, as long as it’s compatible with the sequence elements you are operating on.

Check out the example below for an illustration:

'''

# Our numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Function that filters out all numbers which are odd
def filter_odd_numbers(num):

    if num % 2 == 0:
        return True
    else:
        return False

filtered_numbers = filter(filter_odd_numbers, numbers)

print(filtered_numbers)
# filtered_numbers = [2, 4, 6, 8, 10, 12, 14]    
    

 '''
 Not only did we evaluate True or False for each list element, the filter() function also made sure to only return the elements which matched as True. Very convenient for handling to two steps of checking an expression and building a return list.


 (4) Itertools

The Python Itertools module is a collection of tools for handling iterators. An iterator is a data type that can be used in a for loop including lists, tuples, and dictionaries.

Using the functions in the Itertools module will allow you to perform many iterator operations that would normally require multi-line functions and complicated list comprehension. Check out the examples below for an awesome illustration of the magic of Itertools!

'''



from itertools import *

# Easy joining of two lists into a list of tuples
for i in izip([1, 2, 3], ['a', 'b', 'c']):
    print i
# ('a', 1)
# ('b', 2)
# ('c', 3)

# The count() function returns an interator that 
# produces consecutive integers, forever. This 
# one is great for adding indices next to your list 
# elements for readability and convenience
for i in izip(count(1), ['Bob', 'Emily', 'Joe']):
    print i
# (1, 'Bob')
# (2, 'Emily')
# (3, 'Joe')    

# The dropwhile() function returns an iterator that returns 
# all the elements of the input which come after a certain 
# condition becomes false for the first time. 
def check_for_drop(x):
    print 'Checking: ', x
    return (x > 5)

for i in dropwhile(should_drop, [2, 4, 6, 8, 10, 12]):
    print 'Result: ', i

# Checking: 2
# Checking: 4
# Result: 6
# Result: 8
# Result: 10
# Result: 12


# The groupby() function is great for retrieving bunches
# of iterator elements which are the same or have similar 
# properties

a = sorted([1, 2, 1, 3, 2, 1, 2, 3, 4, 5])
for key, value in groupby(a):
    print(key, value), end=' ')
    
# (1, [1, 1, 1])
# (2, [2, 2, 2]) 
# (3, [3, 3]) 
# (4, [4]) 
# (5, [5])




'''
(5) Generators

Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. This greatly simplifies your code and is much more memory efficient than a simple for loop.

Consider an example where we want to add up all of the numbers from 1 to 1000. The first part of the code below illustrates how you would do this using a for loop.

Now that’s all fine and dandy if the list is small, say a length of 1000. The problem arises when you want to do this with a huge list, say 1 billion float numbers. With a for loop, that massive memory chewing list is created in memory — not everyone has unlimited RAM to store such a thing! The range() function in Python does the same thing, it builds the list in memory

Section (2) of the code illustrates the summing of the list of numbers using a Python generator. A generator will create elements and store them in memory only as it needs them i.e one at a time. That means, if you have to create 1 billion floating point numbers, you’ll only be storing them in memory one at a time! The xrange() function in Python uses generators to build lists.

Moral of the story: If you have a large range that you’d like to generate a list for, use a generator or the xrange function. This is especially true if you have a really memory sensitive system such as mobile or at-the-edge computing.

That being said, if you’d like to iterate over the list multiple times and it’s small enough to fit into memory, it will be better to use for loops and the range function. This is because generators and xrange will be freshly generating the list values every time you access them, whereas range is a static list and the integers already exist in memory for quick access.
'''



# (1) Using a for loop
numbers = list()

for i in range(1000):
    numbers.append(i+1)
    
total = sum(numbers)

# (2) Using a generator
 def generate_numbers(n):
     num = 0
     while num < n:
         yield num
         num += 1
 total = sum(generate_numbers(1000))
 
 # (3) range() vs xrange()
 total = sum(range(1000 + 1))
 total = sum(xrange(1000 + 1))

 







