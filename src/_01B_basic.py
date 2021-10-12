""" More basics that cover string manipulation and operations involving container types.

"""


from typing import Any, Dict, List, Optional, Set


def front_back(string: str) -> str: # _1 [✅]
    """ Given a string, return a new string where the first 
    and last chars have been exchanged. 

    ex. 
    front_back('code') → 'eodc'
    front_back('a') → 'a'
    front_back('ab') → 'ba'
    front_back('') → ''
     

    Args:
        str (str): [description]

    Returns:
        str: [description]
    """
    if len(string) == 0: 
        return string
    chars = list(string)
    chars[0], chars[-1] = chars[-1], chars[0]
    return ''.join(chars)
    # ** write out the steps to solve this before you code 

''' 
1: string.split('') => arr_of_chars 
2: double assign to perform switch 
3: arr_of_chars.join('')
'''



def count_last2(string: str) -> int: # _2 [✅]
    """ Given a string, return the count of the number of times 
    that the last 2 chars appear in the string. 
    Do not count the last substring, use it only as an identifier.

    count_last2('hixxhi') → 1
    count_last2('xaxxaxaxx') → 1
    count_last2('axxxaaxx') → 2


    Args:
        string (str): [description]

    Returns:
        int: [description]
    """
    count = 0
    key = string[-2:]
    for i in range(0, len(string) - 2):
        pair_of_chars = string[ i: i + 2]
        if key == pair_of_chars: count += 1
    return count 
    # ** write out the steps to solve this before you code 

'''
1: count how many times the key = string[-2] appears, count = 0 
2: loop thr str 
3: pair = string[ i : i + 1 ] 
4: if pair == key => count += 1 
'''



def array123(nums: List[int]) -> bool: # _3 [✅]
    """Given an array of ints, return True if the sequence of numbers 
    1, 2, 3 appears anywhere in the array.

    ex. 
        array123([1, 1, 2, 3, 1]) → True
        array123([1, 1, 2, 4, 1]) → False
        array123([1, 1, 2, 1, 2, 3]) → True

    Args:
        nums (List[int]): [description]

    Returns:
        bool: [description]
    """
    seq_of_nums = [1, 2, 3]
    return all(num_in_list in nums for num_in_list in seq_of_nums)
    # ** write out the steps to solve this before you code 

'''
1: have key = seq_of_nums = [1, 2, 3]
2: loop thr in range(1, len(nums) - 1) 
3: if num[i -1] == 1 and num[ i ] == 2 and num[ i + 1 ] == 2 => True 
'''



def dict_merge(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> Dict[Any, Any]: # _4 [✅]   
    """Merge two dictionaries into a new dictionary and return it.

    Args:
        d1 (Dict[str, Any]): first dict 
        d2 (Dict[str, Any]): second dict

    Returns:
        Dict[str, Any]: new dictionary
    """

    # ** do this in exactly one line using syntactical sugar
    return {**d1, **d2}



def dict_filter_comp(d: Dict[str, Any], keys: List[str]) -> Dict[str, Any]: # _5 [✅] 
    """Given a dictionary d return a new dictionary filtered on keys.

    Args:
        d (Dict[str, Any]): [description]
        keys (List[str]): [description]

    Returns:
        Dict[str, Any]: [description]
    """ 

    # ** do this op in one line using a comprehension
    return { key: value for key, value in d.items() for i in range(len(keys)) if key == keys[i] }



def dict_filter_loop(d: Dict[str, Any], keys: List[str]) -> Dict[str, Any]: # _6 [✅]
    """Identical to the above but implement using loops.

    Args:
        d (Dict[str, Any]): [description]
        keys (List[str]): [description]

    Returns:
        Dict[str, Any]: [description]
    """
    # ** do this operation using a loop 
    filtered_dict = dict()
    for key, value in d.items():
        if key in keys: filtered_dict[key] = value
    return filtered_dict



def dict_check_value(d: Dict[str, Any], value: Any) -> bool: # _7 [✅] 
    """ Return True if the value is in the dictionary d.

    Args:
        d (Dict[str, Any]): [description]
        value (Any): [description]

    Returns:
        bool: [description]
    """

    # ** write this operation in one line 
    return value in d.values()



def dict_key_of_value_comp(d: Dict[str, Any], value: Any) -> List[str]: # _8 [✅] 
    """Returns any keys that contain the given value.

    Args:
        d (Dict[str, Any]): [description]
        value (Any): [description]

    Returns:
        List[str]: [description]
    """
    # ** solve this operation in one line using a comprehension
    return [key for key, target_value in d.items() if target_value == value] 



def dict_key_of_value_loop(d: Dict[str, Any], value: Any) -> List[str]: # _9 [✅] 
    """Identical to the above but implemented using loops 

    Args:
        d (Dict[str, Any]): [description]
        value (Any): [description]

    Returns:
        List[str]: [description]
    """
    # ** implment this operation using a loop
    list_of_matching_keys = []
    for key, target_value in d.items():
        if target_value == value: 
            list_of_matching_keys.append(key)
    return list_of_matching_keys



def set_diff(s1: Set[int], s2: Set[int]) -> Set[int]: # _10 [✅] 
    """Return the set difference between 2 sets

    Args:
        s1 (Set[int]): first set
        s2 (Set[int]): second set

    Returns:
        Set[int]: difference between the first and second set.
    """ 

    # ** explain here exactly what a set difference means and give an example
    # ** write the code in one line
    return s1 - s2 

# diff takes the LHS set and takes away common el found in the RHS set 
# s1 = {1, 2, 3}, s2 = {3, 4, 5}, -> s1 - s2 => {1, 2} 
# but s2 - s1 => {4, 5}


def set_symdiff(s1: Set[int], s2: Set[int]) -> Set[int]: # _11 [✅] 
    """Returns the symmetric difference of two sets.

    Args:
        s1 (Set[int]): first set
        s2 (Set[int]): second set

    Returns:
        Set[int]: symmetric difference between the first and second set.
    """
    # ** explain here exactly what a symmetric difference is and give an example
    # ** write the code in one line
    return s1.symmetric_difference(s2)

# symmetric diff is the difference between two sets 
# two circles intersect have a common set, sym diff is everything outside the common area 
# s1 = {1, 2, 3} s2 = {1, 3} -> s1 ^ s2 => {2} 
# sym diff ~ not union 


def set_common(s1: Set[int], s2: Set[int]) -> Set[int]: # _12 [✅] 
    """checks if 2 sets have common values. If they do returns 
    a set of common items. If not then returns an empty set

    Args:
        s1 (Set[int]): [description]
        s2 (Set[int]): [description]

    Returns:
        Set[int]: [description]
    """
    # ** explain what type of set operation is needed here before you write the code
    return s1 & s2

# the & op used to find the common el of two sets 


def set_remove(s1: Set[int], s2: Set[int]) -> None: # _13 [] 
    """Removes items from set 1 that are not common to both 
    set 1 and 2. NOTE that this mutates s1.

    Args:
        s1 (Set[int]): first set to be mutated
        s2 (Set[int]): second set 

    """
    # explain what kind of set operation is needed here before you write the code
    # ** this can be done in one line
    s1.intersection_update(s2)

'''
- find not union of s1 and s2 <=> symmetric diff 
- s1.diff s2 
'''
