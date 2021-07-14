#!/usr/bin/env python
# coding: utf-8

# # Assignment 4 - Intro to Python - Summer 2021

# ### Problem 1

# In[86]:


# function that divides 2 number together and returns result.  Results are not rounded.
def divide(dividend,divisor):
    # / is for normal division.  // will round off the quotient and not include the remainder.
    answer = dividend / divisor
    return answer

result = divide(1, 7)
print (result)

#result = divide(3,5)
#print (float(result))


# ### Problem 2

# In[87]:


# Function accepts a tuple of numbers and multiples all together. It also accepts a list and set of numbers.
# If it receives and alphanumeric in the list, it will return and error.
def multiplyAll(TupleofNumbers):
    total = 1
    for number in TupleofNumbers:
        total = total * number
    return total

tupleList = (1,2,3,4,5,6,7)
result = multiplyAll(tupleList)
print (result)


# ### Problem 3

# In[88]:


# The function removes a string specified in the item list. Expects a list and string as parameters.
def filter_list(itemList, toRemove):
    
    itemsToKeep = []
    
    for item in itemList:
        if toRemove != item:
            itemsToKeep.append(item)
    
    return itemsToKeep

listToBeFiltered = ['cat','hello','dog','hello','cow','pig','chicken','hello']
removalItem = 'hello'

result = filter_list(listToBeFiltered,removalItem)
print (result)


# ### Problem 4

# In[89]:


# Returns the longest word in a list.  
def longest_word(listOfWords):
    len_word = 0
    for item in listOfWords:
        if len(item) > len_word:
            len_word = len(item)
            longest_word = item 
    
    return longest_word

word_list = ['apple', 'dog', '0','mouse','identification', 'Ranger']
result = longest_word(word_list)
print (result)        


# ### Problem 5

# In[92]:


# Create list_to_unique function that returns unique items only. Items can be string or number. 
# Items should be returned in the same order.
# The list will return item as unique if it has a space before or after.
def list_to_unique(madeUnique):
    uniqueList = []
    
    for item in madeUnique:
        if item not in uniqueList:
            uniqueList.append(item)
    
    return uniqueList

input_list = [5,5,'apple', 'pizza', 'apple']
result = list_to_unique(input_list)
print (result)

input_list = [1,2,3,4,5]
result = list_to_unique(input_list)
print (result)


input_list = [1,2,3,4,1, 723, 'dog', 'cat', 'dog', 'dog', 'dog ', 'mouse', 1,2,3,4,5, 'cat','mouse',723, 'mouse', ' ']
result = list_to_unique(input_list)
print (result)

        
    

