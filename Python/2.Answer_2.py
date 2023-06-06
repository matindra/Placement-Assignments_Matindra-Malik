def is_valid_string(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    values = list(freq.values())
    values.sort()
    unique_values = set(values)
    
    if len(unique_values) == 1:
        return "YES"
    elif len(unique_values) == 2:
        if values.count(values[0]) == 1 and values[0] == 1:
            return "YES"
        elif values.count(values[-1]) == 1 and values[-2] == values[-1] - 1:
            return "NO"  
    
    return "NO"

# Test Case 1

s = "xyz"
print(is_valid_string(s))  

# Explaination: Output in this case is - YES. 
# This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }


# Test Case 2

s = "xyzz"
print(is_valid_string(s))  

# Explaination: Output in this case is - YES. 
# This is not a valid string because the occurrence of “z” is 2.
# That leaves character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }


# Test Case 2
s = "xxyyzz"
print(is_valid_string(s))  

# Explaination: Output in this case is - YES. 
# In this case, the string "xxyyzz" has three distinct characters: 'a', 'b', and 'c'. 
# The frequencies of these characters are [2, 2, 2], which are all equal.
# Therefore, the output is "YES" since the string is already valid.