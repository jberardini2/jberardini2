#!/usr/bin/env python
# coding: utf-8

# ### Problem 1

# In[22]:


print ("Listing numbers 0-9 using for loop and range function:")
for myRange in list(range(10)):
    print (myRange)


print ("Listing numbers 0-9 and dividing by 3:")
for divRange in list(range(10)):
    print (str(divRange) + " / 3 = " + str(divRange // 3) )


# ### Problem 2
# 

# In[23]:


# Print 0-9 and if it is odd or even.  Use the modulo calculation. Also, consider zero when it's not odd or even.
for OddOrEven in range(10):
    if OddOrEven == 0:
        print (str(OddOrEven) + " is Zero")
    elif OddOrEven % 2 == 0:
        print (str(OddOrEven) + " is Even")
    else:
        print (str(OddOrEven) + " is Odd")


# ### Problem 3

# In[2]:


# Use a while loop and multiply my_var by 1.65. Add the total and go through
# while loop again until my_var is > 100 then print it.
my_var = 2
while my_var < 100:
    my_var = my_var * 1.65
    print (my_var)

print ("Value of final my_var: " + str(my_var))


# ### Problem 4

# In[21]:


# Check weight and determine price
# weight <= 5 cost is 3
# weight > 5 and <= 10 cost is 7
# weight > 10 cost is 15
package_weight = 25

if package_weight <= 5:
    shipping_cost = 3
elif package_weight > 5 and package_weight <= 10:
    shipping_cost = 7
else:
    shipping_cost = 15
    
print ("Package Weight is " + str(package_weight))
print ("Shipping Cost is " + str(shipping_cost))


# ### Problem 5

# In[53]:


# myListofDictionaries = [{'animal_name': 'Ranger', 'age': 3}, {'animal_name': 'Chloe', 'age': 5}, {'animal_name': 'Morticia', 'age': 7}, {'animal_name': 'Bean','age': 4}  ]

# You can't list the name in a list of dictionaries until you get them
# in the right for loop. This fails for a list of dictionaries.
# print (myListofDictionaries['animal_name'])


# Write a For Loop that loops through dictionaries. Check for key name, if found
# print the value of the name. 
print ('****************')        
myListofDictionaries = [{'animal_name': 'Ranger', 'age': 3}, {'animal_name': 'Chloe', 'age': 5}, {'animal_name': 'Morticia', 'age': 7}, {'animal_name': 'Bean','age': 4}  ]
for dictionary in myListofDictionaries:
    for key_name in dictionary.keys():
        if key_name == 'animal_name':
            print (dictionary['animal_name'])
            


# ### My Notes and Code completed from Module 3

# In[67]:


print (4 % 2)
for val in range(5):
    if val == 1:
        continue
    print ("Val is:" + str(val))

a = -2
b = -3
if a > 0 and b > 0:
    print ("a and b are positive")
elif a < 0 and b < 0:
    print ("a and b are negative")
else:
    print (" a and b are not both positive or negative")

# removing 0 and 6 from the list.
# This took a good 45 minutes to figure out. I kept thinking, this would be much easier with a "For Loop".
iList = [6, 33, 0, 55, 0, 74, 6, 91, 105]
i = 0 # this is the index value of iList
while i < (len(iList) - 1): # length of list   
    print (iList[i])
    if iList[i] == 0 or iList[i] == 6: # check the value for a 0 or 6.
        del iList[i] # delete 0 or 6 from the list.
    
    i = i + 1 # bump the index by 1
    
print ("Final List without 0 or 6:" + str(iList))




   

    

