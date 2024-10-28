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
    for item in range(len(list_one)):
        new_dict[list_one[item]] = list_two[item]
    print(new_dict)
    return new_dict

add_lists_together(list_one, list_two)