# Question #1 - List 
# A. Write a Python program to convert list to list of dictionaries.
# B. Write a Python program to create a dictionary from two lists without losing duplicate
# values.

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
