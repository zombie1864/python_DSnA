""" Implement each of the functions below. They are designed to demonstrate fundamental language features
and are mostly concerned with logic, maths and basic parsing. Several focus on manipulating data in 
common container classes (list, dict and tuple).

A few will ask you to `raise` a specific `Exception` based on a given condition.

Reference topics: 
https://docs.python.org/3.9/library/stdtypes.html#truth-value-testing
https://docs.python.org/3.9/library/stdtypes.html#boolean-operations-and-or-not
https://docs.python.org/3.9/library/stdtypes.html#comparisons
https://docs.python.org/3/tutorial/controlflow.html
https://docs.python.org/3/library/exceptions.html
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range


"""

from typing import List, Tuple, Dict

#⚠️ do i define static types for when i decalre variables? 

def truthiness(a: int, b: int, negative: bool=False) -> bool: # _1 [✅]
    """Given 2 integers return True if one is negative and one of them positive or 0. If negative is 
    set to True then return True only if both are negative.

    With negative set to False: 
    two positives 

    Args:
        a (int): An int
        b (int): An int
        negative (bool): A switch to test if numbers are negative. defaults to False.

    Returns:
        bool: True or False
    """
    if a < 0 and b < 0 and not negative or a >= 0 and b >= 0 and not negative:
        return negative 
    elif a < 0 and b >= 0 or a >= 0 and b < 0 and not negative:
        return True 
    elif a >= 0 and b >= 0 and negative: 
        return not negative
    elif a >= 0 and b < 0 and negative or a < 0 and b >= 0 and negative:
        return not negative
    else:
        return negative

"""
describe how you will apprach this before you code
if a < 0 and b < 0 => negative = True 
if a < 0 and b >=0 => negative = True 
"""


def near(n: int, target: int=100, threshold: int=10) -> bool: # _2 [✅] 
    """Given an int n, return True if it is within threshold of the target value or 
    twice the target value 
    ex. 
    near(93) → True
    near(90) → True
    near(89) → False

    Args:
        n (int): number to check
        target (int, optional): The target value. Defaults to 100.
        threshold (int, optional): The threshold value. Defaults to 10.

    Returns:
        bool: True or False
    """
    return n in range(target - threshold, target + threshold + 1) or n == target * 2 

"""
describe how you will apprach this before you code
if n == target * 2 return true 
upper_limit = target + threshold 
lower_limit = target - threshold 
if n in range(lower_limit, upper_limit + 1 ) return true 
else return false 
"""

def str_remove(string: str, index: int) -> str: # _3 [✅] 
    """Given a non-zero length string, return a new string with the given index removed. 

    Args:
        string (str): String without the 
        idx (int): [description]

    Raises:
        ValueError: If string is of len zero.

    Returns:
        str: The new string 
    """
    if len(string) == 0:
        raise ValueError # put the msg inside here - refer to the doc 
    else:
        return string.replace(string[index], '')
'''
describe how you will apprach this before you code
return a new string 
@ string[index] replace with nothing 
'''

def heptiptup(n: int) -> str: # _4 [✅] 
    """Given an integer n return a string given the following rules:
        * If n is a factor of 3 the string should contain `Hep` 
        * If n is a factor of 5 the string should contain `Tip` 
        * If n is a factor of 7 the string should contain `Tup`
        * If all of these conditions fail return the original value as a string 
    
    The order of the statements Hep Tip and Tup should be preserved in the resulting string

    Args:
        n (int):  Any integer

    Returns:
        str: The result string
    """
    msg = ''
    if n == 0:
        return '0'
    if n % 3 == 0: 
        msg += 'Hep'
    if n % 5 == 0:
        msg += 'Tip'
    if n % 7 == 0:
        msg += 'Tup'
    if n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        return str(n)
    return msg
'''
describe how you will apprach this before you code
if num is divisable by the condition without remainder then return one of the three strings  
'''

def calculate_slope_between_two_points(point_a: Dict[str,float], point_b: Dict[str, float]) -> float: # _5 [✅] 
    """Given two dictionaries representing points that contain the keys x and y, calculate the 
    slope between the two points. If points are equal return float type infinity. Will raise a 
    ValueError if x or y are not present in the either point.

    Args:
        point_a (Dict[str,float]):  The first point. Must contain the keys 'x' and 'y'
        point_b (Dict[str, float]): The second point. Must contain the keys 'x' and 'y'

    Raises:
        ValueError: If x and y are not present in either point_a or point_b

    Returns:
        float: The slope or float('inf')
    """ 
    if len(point_a) == len(point_b) == 0: raise ValueError
    if set(point_a).symmetric_difference(set(point_b)) == set():
        return float('inf') if int(point_b['x'] - point_a['x']) == 0 else int((int(point_b['y'] - point_a['y']) / int(point_b['x'] - point_a['x'])))
    elif set(point_a).symmetric_difference(set(point_b)) != set(): raise ValueError
    elif point_a['x'] == point_b['x'] and point_b['y'] == point_a['y']: return float('inf')

'''
describe how you will apprach this before you code
⚠️each arg is dict with DS ~ {'x': num_1, 'y': num_2} [ why not a tuple ~ ('x', num_1, 'y', num_2) ]
    ⮑ dict are mutable
⚠️Dict why not dict as type  
slope formula = ∆y / ∆x
if point_a['y'] == point_b['y'] and point_a['x'] == point_b['y'] return float type infinity 
try catch flow -> try calculate slope and check if 'x' or 'y' in point_a or point_b <=> True or False flow 
'''

def custom_heptiptup(number: int, rules: Dict[str, int]) -> str: # _6 [✅]
    """ Based on the above function, we want to make a function that will handle custom input. 
    It will check if a number is divisible by three different
    random natural numbers: x, y, and z, with x < y < z. 
    
    Given an integer n and a mapping (dictionary), return a string given the following rules:
        * If n is a factor of x the string should contain `A` 
        * If n is a factor of y the string should contain `B` 
        * If n is a factor of z the string should contain `C`
        * If all of these conditions fail return the original value as a string 
        * Rules should only contain 3 values and those values must be positive integers.

    NOTE that what the string values are do not matter... it should work with anything.

    ex. 
        rules = {'Bleep': 5, 'Blip': 10, 'Bloop': 11}

        custom_heptiptup(5, rules) -> 'Bleep' 
        custom_heptiptup(1, rules) -> '1'
        custom_heptiptup(550, rules) -> 'BleepBlipBloop'

    Args:
        n (int):  Any integer
        rules [Dict[str,int]]: A dictionary mapping containing the 3 rules.

    Raises: 
        ValueError: If exactly 3 rules are not given.
        ValueError: If any rule values are not ints 
        ValueError: If any rule value is not positive

    Returns:
        str: The result string 

    """
    err_code_list = [] # 1 = 1st cond, 2 = 2nd cond, 3 = rd cond 
    if len(rules) < 3: 
        err_code_list.append(1) 
    if any( True for value in rules.values() if type(value) != int ): 
        err_code_list.append(2)
    if any( True for value in rules.values() if int(value) < 0 ): 
        err_code_list.append(3)
    if len(err_code_list) > 0: 
        raise ValueError 
    custom_str = ''
    values = tuple(rules.values())
    str_keys = list( rules.keys() )
    if all( number % value != 0 for value in values ): 
        return str(number)
    if number % values[0] == 0:
        custom_str += str_keys[0] 
    if number % values[1] == 0:
        custom_str += str_keys[1]
    if number % values[2] == 0:
        custom_str += str_keys[2]
    return custom_str

'''
describe how you will apprach this before you code
rules = {'A': x, 'B': y, 'C': z} ⚠️ assuming that always x < y < z [ param condition ]
_1: raise execption if len(rules) < 3 or type(x,y,z) != int or x, y, z < 0 [ logical condition ]
    ⮑ provide a useful msg to user 
_2: custom_str = ''
_3: if n % x == 0 =>custom_str += 'A' -> if n % y == 0 =>custom_str += 'B' -> if n % z == 0 =>custom_str += 'Z'
_4: if neither x or y or z is factor of n return str(n)
'''

def filter_out_even_numbers(numbers: List[int]) -> List[int]: # _7 [✅] 
    """without using if statement filter out a list of integers of 
    even values and return a list of integers.
        
    Examples: 
        * [2,6,1,4,5] --> [1,5]
        * [] --> []
        * [2,4] --> []

    Args: 
        numbers (List[int]): The list of numbers 
    
    Returns: 
        List[int]: A list of filtered ints

    """

    # ** solve this in one line using a lambda function
    return list( filter(lambda number: number % 2 != 0, numbers) )

def total2d(arr: List[List[int]]) -> int: # _8 [✅] 
    """Flatten and get total of 2d array using listcomp

    Args:
        arr (List[List[int]]): A list of list of ints

    Returns:
        int: the total
    """
    # ** try to solve this in one line using a list comprehension
    return sum( [sum(sub_arr) for sub_arr in arr ] )
'''
_1: DS ~ [[ 1, 2 ], [3, 4, 5], [7]] each sub arr having any len 
_2: iterate thr outer_arr and take sum of sub_arr -> add total += sum 
'''

def list_of_records(rows: List[List[int]], colnames: Tuple[str]) -> List[Dict[str, int]]: # _9 [✅]
    """Given list of list of integers and a tuple of colnames, return a list of dictionaries, where 
    each value is associated with a given colname. 

    ex. 
    Given: 
        rows = [[1,2,3], [4,5,6], [7,8,9]]
        colnames = ('a', 'b', 'c')

    Returns:  
        [
            {'a': 1, 'b': 2, 'c': 3},
            {'a': 4, 'b': 5, 'c': 6},
            {'a': 7, 'b': 8, 'c': 9},
        ]

    Args:
        rows (List[List[int]]): The row values
        colnames (Tuple[str]): The colnames 

    Raises:
        ValueError: If rows are of unequal length
        ValueError: If column names are not equal to the length of each row

    Returns:
        List[Dict[str, int]]: [description]
    """
    if any( True for sub_rows in rows if len(sub_rows) != len(colnames) ): raise ValueError 
    dictionary = dict()
    list_of_dict = list()
    for i in range(len(rows)):
        for j in range(len(colnames)):
            dictionary[colnames[j]] = rows[i][j]
        list_of_dict.append(dictionary)
        dictionary = dict()
    return list_of_dict
'''
_1: check if the len of sub_rows == len(col_names)
    ⮑ via if comprehension maybe ?? 
_2: iterate thr col_names and iterate thr sub_arr and assign col_name to value from sub_arr 
'''