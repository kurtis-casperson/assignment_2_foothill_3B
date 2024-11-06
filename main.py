# Question #1 - List 
# A. Write a Python program to convert list to list of dictionaries.

color = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

color_dict = []


def list_to_dict(colors, codes):
    """
    The loop uses the length of the colors list to determine how many iterations to run the loop.
    Range is needed to loop over an integer number of iterations.
    """
  
    for item in range(len(colors)):
        color_dict.append({'color_name': colors[item], 'color_code': codes[item]})
    print(color_dict)
    return color_dict

result = list_to_dict(color, color_code)

# B. Write a Python program to create a dictionary from two lists without losing duplicate
# values.

list_one = ['one', 'two', 'three', 'four', 'five']
list_two = [1, 2, 3, 5, 5] 

new_dict = {}

def add_lists_together(list_one, list_two):
    """
    Turn two lists into a dictionary with multiple duplicate values.
    """
    for item in range(len(list_one)):
        new_dict[list_one[item]] = {list_two[item]}
    print(new_dict)
    return new_dict

add_lists_together(list_one, list_two)


# Question #2 - Dictionary (20pts)
# A. Write a Python program to match key values in two dictionaries.

dict_one = {'key1': 1, 'key2': 3, 'key3': 2}
dict_two = {'key1': 1, 'key2': 2}

no_match = True

def matching_values(dict_one, dict_two):
    for key in dict_one:
        for keys in dict_two:
            if keys == key and dict_one[key] == dict_two[keys]:
                print(f"{key}: {dict_one[key]} is present in both dict_one and dict_two")

matching_values(dict_one, dict_two)

# B. Write a Python program to sort Counter by value.
grades = {'Math':81, 'Physics':83, 'Chemistry':87}
def sort_dict_by_value(input_dict):
    """
    Sorts a dictionary by its values in descending order.

    Parameters:
    input_dict: A dictionary where keys are subjects and values are scores.
    Returns:
    A list of tuples, each containing a subject and its score, sorted by score in descending order.
    """
    # Create a list of tuples from the dictionary
    items = [(key, value) for key, value in input_dict.items()]
    
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j][1] < items[j + 1][1]:  
                # Swap if the current item is less than the next item
                items[j], items[j + 1] = items[j + 1], items[j]

    return items

sorted_output = sort_dict_by_value(grades)
print(sorted_output)


# Question #3 - String Reverse (30pts)
# Given a string, you need to reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order

sentence = "Let's do a coding project"

def reverse(sentence):
    """
    Use slicing to reverse each word in a sentence.  But order each word in reverse.
    """
    list = []
    split_sentence = sentence.split()

    for i in split_sentence:
        list.append(i[::-1])
    
    result = ' '.join(list)
    print(result)
    return result
    

reverse(sentence)

# Question #4 - K-Grammar (30pts)
# On the first row, we write a 0. Now in every subsequent row, we look at the previous
# row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10. Given
# row N and index K, return the K-th indexed symbol in row N.
# (The values of K are 1-indexed.) (1 indexes)

def kGrammar(n_row, k_index):
    k_index -= 1
    symbol = 0

    while n_row > 0:
        # Check if k is odd or even
        if k_index % 2 != 0:
            symbol = 1 - symbol 
        k_index //= 2 
        n_row -= 1  
        print(symbol)
    return symbol

row = 4

index = 5

result = kGrammar(row, index)
print(f"The K-th indexed symbol in row {row} is: {result}")