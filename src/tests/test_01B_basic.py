
import unittest 
from module_one._01B_basic import *


def test_front_back_returns_expected(): 

    assert front_back('code') == 'eodc'
    assert front_back('a') == 'a'
    assert front_back('ab') == 'ba'
    assert front_back('') == ''


def test_count_last2_returns_expected(): 

    assert count_last2('hixxhi') == 1 
    assert count_last2('xaxxaxaxx') == 1 
    assert count_last2('axxxaaxx') == 2
    assert count_last2('bbbbbbbbbbb') == 9
    assert count_last2('bbbbbbbbbyy') == 0
    assert count_last2('z z zzz zc oid jdko k zz') == 2
    assert count_last2(' s    s g   h hh h    ') == 7


def test_array123_returns_expected(): 

    assert array123([1,1,2,3,1]) 
    assert not array123([1,5,2,4,1])
    assert array123([8,5,2,1,2,3,1,5,7]) 
    assert array123([1,1,2,1,1,1,2,2,2,2,3,3,3,2,1,2,3]) 


def test_dict_filter_comp_returns_correct_dictionary(): 

    test_dict = {
        'a': 1, 
        'b': 2, 
        'c': 3, 
        'd': 4
    }
    tc = unittest.TestCase()    
    
    res = dict_filter_comp(test_dict, ['a', 'b']) 
    tc.assertDictEqual(res, {'a': 1, 'b': 2})

    res = dict_filter_comp(test_dict, ['a', 42])
    tc.assertDictEqual(res, {'a': 1})
    
    res = dict_filter_comp(test_dict, [])
    tc.assertDictEqual({}, res)

def test_dict_filter_loop_returns_correct_dictionary(): 

    test_dict = {
        'a': 1, 
        'b': 2, 
        'c': 3, 
        'd': 4
    }
    tc = unittest.TestCase()    
    
    res = dict_filter_loop(test_dict, ['a', 'b']) 
    tc.assertDictEqual(res, {'a': 1, 'b': 2})

    res = dict_filter_loop(test_dict, ['a', 42])
    tc.assertDictEqual(res, {'a': 1})


def test_dict_check_value_returns_true_if_value_present(): 

    assert dict_check_value({'a': 1}, 1) 


def test_dict_check_value_returns_false_if_value_absent(): 

    assert dict_check_value({'a': 1}, 2) is False


def test_dict_merge(): 

    assert dict_merge({'a': 1}, {'b': 2}) ==  {'a': 1, 'b': 2}


def test_dict_key_of_value_comp_returns_expected(): 

    test = {'a': 1, 'b': 2, 'c': 3, 'd': 3}

    res = dict_key_of_value_comp(test, 3)
    assert ['c', 'd'] == sorted(res)

    res = dict_key_of_value_comp(test, 4)
    assert [] == res

    res = dict_key_of_value_comp(test,1)
    assert ['a'] == res


def test_key_of_value_loop_returns_expected(): 

    test = {'a': 1, 'b': 2, 'c': 3, 'd': 3}

    res = dict_key_of_value_loop(test, 3)
    assert ['c', 'd'] == sorted(res)

    res = dict_key_of_value_loop(test, 4)
    assert [] == res

    res = dict_key_of_value_loop(test,1)
    assert ['a'] == res


def test_set_diff_returns_expected(): 

    s1 = {1,2,3}
    s2 = {4,5,6}

    assert set_diff(s1,s2) == {1,2,3}
    assert set_diff(s2, s1) == {4,5,6}



def test_set_symdiff_returns_expected(): 

    s1 = {1,2,3}
    s2 = {4,5,6}

    assert set_symdiff(s1, s2) == {1,2,3,4,5,6}
    assert set_symdiff(s2, s1) == {1,2,3,4,5,6}



def test_set_common_returns_expected(): 

    s1 = {1,2,3,4,5}
    s2 = {4,5,6,7,8,9}
    s3 = {10, 11, 12}

    assert set_common(s1, s2) == {4,5}  
    assert set_common(s1, s3) == set()



def test_set_remove_returns_expected(): 


    s1 = {1,2,3,4,5,6}
    s2 = {4,5,6,7,8,9}

    set_remove(s1, s2)
    assert s1 == {4,5,6}

