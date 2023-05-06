#!/usr/bin/env python
# coding: utf-8

# Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.

# In[1]:


def equal(a, b, c):
    if a == b == c:
        return 3
    elif a ==b or a == c or b ==c:
        return 2
    else:
        return 0


# In[2]:


equal(3, 4, 3) 


# In[3]:


equal(1, 1, 1)


# In[4]:


equal(3, 4, 1)


# Write a function that converts a dictionary into a list of keys-values tuples.
# 

# In[5]:


def dict_to_list(d):
    return sorted(d.items())


# In[7]:


dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3})


# In[8]:


dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10})


# Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
# 

# In[3]:


def mapping(lst):
    result = {}
    for letter in lst:
        result[letter.lower()] = letter.upper()
    return result


# In[4]:


mapping(["p", "s"])


# In[5]:


mapping(["a", "b", "c"])


# In[6]:


mapping(["a", "v", "y", "z"])


# Write a function, that replaces all vowels in a string with a specified vowel.

# In[13]:


def vow_replace(txt, vowel):
    vowels = 'aeiouAEIOU'
    new_txt = ''
    for char in txt:
        if char in txt:
            if char in vowels:
                new_txt += vowel
            else:
                new_txt += char
    return new_txt


# In[14]:


vow_replace("apples and bananas", "u")


# In[15]:


vow_replace("cheese casserole", "o")


# In[18]:


vow_replace("stuffed jalapeno poppers", "e")


# Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.

# In[19]:


def ascii_capitalize(txt):
    capitalized_txt = ""
    for char in txt:
        ascii_code = ord(char)
        if ascii_code % 2 == 0:
            capitalized_txt += char.upper()
        else:
            capitalized_txt += char.lower()
    return capitalized_txt


# In[20]:


ascii_capitalize("to be or not to be!")


# In[21]:


ascii_capitalize("THE LITTLE MERMAID")


# In[22]:


ascii_capitalize("Oh what a beautiful morning.")


# In[ ]:




