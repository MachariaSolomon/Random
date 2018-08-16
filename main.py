import re

def check_password(*args):
    #check the password against criteria
    #password criteria
    criteria = re.compile(r'[\sa-zA-Z0-9]+[$|#|@]+')
    matching_passwords = []
    #use a for loop to iterate through the provided arguments
    for item in args:
        if 6 <= len(item) <= 12:
            if re.search(criteria, item):
                matching_passwords.append(item)
    # return a comma separated list of valid passwords
    return ','.join(matching_passwords)

# result = check_password('ABd1234@1', 'A1234@1', 'a F1#', '2w3E*', '2We3345')
# print(result)

def input_output_string(s1, s2):
    #compare the length of both strings to get the one with maximum length
    if len(s1) > len(s2):
        return s1
    elif len(s2) > len(s1):
        return s2
    else:
    # if both equal in length, return each
      return s1
      return s2


# output1 = input_output_string("Solomon", "Macharia")
# output2 = input_output_string("Solomon", "Solomon")

# print(output1)
# print(output2)



def reverse_or_uppercase(itemslist):
    # Iterate through the list to check if all items are integers
    if  all([isinstance(n, int) for n in itemslist]):
        return list(reversed(itemslist))
    # Iterate through the list to check if all items are strings
    if all([isinstance(n, str) for n in itemslist]):
        return [n.upper() for n in itemslist]
    # If not int, or string, return the list
    return itemslist


# print(reverse_or_uppercase([1, 2, 3]))

def first_vowel(word):
    criteria = re.compile('^[aeiouAEIOU]')
    pos = 0
    # loop through the word to get the first vowel
    while pos < len(word):
        if re.match(criteria, word[pos]):
            return pos
        pos = pos + 1

def pig_latin(word):
    pos = first_vowel(word)     
    if pos == 0:
        return word[0:] + 'way'
    else:
        return word[pos:] + word[0:pos] + 'ay'

# # def return_true_or_false(*args):
#     criteria = re.compile('[a-zA-Z0-9]+[\?\?\?]')
#     for item in args:
#         if 
    
#     return True