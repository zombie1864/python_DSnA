import pytest
import unittest
from module_one._01A_basic import *

tc = unittest.TestCase()


def test_truthiness_pos_pos_default_returns_false(): 
    res = truthiness(1,1)
    assert res == False

def test_truthiness_pos_zero_default_returns_false():
    res = truthiness(1,0)
    assert res == False


def test_truthiness_pos_neg_default_returns_true():
    res = truthiness(1,-1)
    assert res == True


def test_truthiness_neg_neg_default_returns_false():
    res = truthiness(-1,-1)
    assert res == False


def test_truthiness_zero_zero_default_returns_false(): 
    res = truthiness(0,0)
    assert res == False


def test_truthiness_pos_pos_true_returns_false(): 
    res = truthiness(1,1, True)
    assert res == False


def test_truthiness_pos_zero_true_returns_false():
    res = truthiness(1,0, True)
    assert res == False


def test_truthiness_pos_neg_true_returns_false():
    res = truthiness(1,-1, True)
    assert res == False


def test_truthiness_neg_neg_true_returns_false():
    res = truthiness(-1,-1, True)
    assert res == True


def test_truthiness_zero_zero_true_returns_false(): 
    res = truthiness(0,0, True)
    assert res == False


def test_near_93_defaults(): 
    res = near(93)
    assert res 


def test_near_90_defaults():
    res = near(90)
    assert res  


def test_near_89_defaults():
    res = near(89)
    assert res == False 


def test_near_93_threshold_5(): 
    res = near(93, threshold=5)
    assert res == False  


def test_near_90_target_95_threshold_5():
    res = near(90,target=95, threshold=5)
    assert res == True


def test_near_200_target_100_threshold_99():
    res = near(200, 100, 99)
    assert res == True



def test_str_remove_works_as_expected():

    string = "hello"
    res = str_remove(string, 1)
    assert res == "hllo"

    res = str_remove(string, 4)
    assert res == "hell"


def test_str_remove_raises_valueerror_if_string_len_is_zero():
    with tc.assertRaises(ValueError):
        str_remove('', 1)



def test_heptiptup_n_factor_of_three_returns_hep():

    res = heptiptup(3)
    assert res == "Hep"

    res = heptiptup(6)
    assert res == "Hep"


def test_heptiptup_n_factor_of_five_returns_tip(): 
    res = heptiptup(5)
    assert res == "Tip"

    res = heptiptup(10)
    assert res == "Tip"

def test_heptiptup_n_factor_of_seven_returns_tup(): 
    res = heptiptup(7)
    assert res == "Tup"

    res = heptiptup(49)
    assert res == "Tup"

def test_heptiptup_n_factor_of_3_and_5_returns_heptip():
    res = heptiptup(15)
    assert res == "HepTip"


def test_hetiptup_n_factor_of_3_7_returns_heptup():
    res = heptiptup(21)
    assert res == "HepTup"

def test_heptiptup_n_factor_of_3_5_7_returns_heptiptup(): 

    res = heptiptup(105)
    assert res == "HepTipTup"

def test_heptiptup_n_factor_fails_condition_returns_n():
    res = heptiptup(4)
    assert res == "4"


def test_calculate_slope_between_two_points():

    m = calculate_slope_between_two_points({'x': 0, 'y': 1}, {'x':1, 'y':1})
    assert m == 0

    m = calculate_slope_between_two_points({'x': 1, 'y': 1}, {'x':2, 'y':2})
    assert m == 1

    m = calculate_slope_between_two_points({'x': 1, 'y': 3}, {'x':2, 'y':6})
    assert m == 3


def test_calculate_slope_between_two_points_returns_inf_if_same():
    m = calculate_slope_between_two_points({'x': 0, 'y': 1}, {'x':0, 'y':2})
    assert m == float('inf')


def test_calculate_slope_between_two_points_checks_schema(): 
    
    p1, p2 = {'x': 0,}, {'x':1, 'y':1}
    with pytest.raises(ValueError): 
        calculate_slope_between_two_points(p1, p2)
    
    p1, p2 = {'x': 0, 'y': 1}, {'y': 1}
    with pytest.raises(ValueError): 
        calculate_slope_between_two_points(p1, p2)
    


def test_custom_heptiptup_works_as_expected():

    custom_dict = {'A': 5, 'B': 10, 'C': 11}
    
    res = custom_heptiptup(5, custom_dict)
    assert res == 'A'

    res = custom_heptiptup(1, custom_dict)
    assert res == '1'

    res = custom_heptiptup(550, custom_dict)
    assert res == 'ABC'


def test_custom_heptiptup_raises_valuerror_if_rules_not_three(): 

    with pytest.raises(ValueError): 
        custom_heptiptup(5, {'a': 1})


def test_custom_heptiptup_raises_valuerror_if_rules_not_contain_ints(): 

    with pytest.raises(ValueError): 
        custom_heptiptup(5, {'a': 1, 'b': 2, 'c': '42'})


def test_custom_heptiptup_raises_valueerror_if_ints_not_positive(): 

    with pytest.raises(ValueError): 
        custom_heptiptup(5, {'a': 1, 'b': 2, 'c': -3})


def test_filter_out_even_numbers():

    ls = [1,2,3]
    res = filter_out_even_numbers(ls)
    assert res == [1,3]

    ls = []
    res = filter_out_even_numbers(ls)
    assert res == []

    ls = [2]
    res = filter_out_even_numbers(ls)
    assert res == []

    ls = [1]
    res = filter_out_even_numbers(ls)
    assert res == [1]


def test_total2d():

    ls = [[1,2,3],[1,2,3,4]]
    res = total2d(ls)
    assert res == 16

    ls = [[1,2]]
    res = total2d(ls)
    assert res == 3

    ls = [[1,2], [1,2,3], [1,2,3]]
    res = total2d(ls)
    assert res == 15


def test_list_of_records_works_as_expected():
    columns = ('x', 'y')

    rows = [[1,2], [2,3], [3,4]]
    res = list_of_records(rows, columns)

    exp = [{'x':i[0], 'y': i[1]} for i in rows]
    for i in range(len(rows)):
        assert res[i] == exp[i]


def test_list_of_records_raises_value_error_on_unequal_row_length(): 

    rows = [[1,2],[1]]
    columns = ('x', 'y')
    with tc.assertRaises(ValueError):
        list_of_records(rows,columns)


def test_list_of_records_raises_error_if_colnames_not_equal_to_row_length():
    
    columns = ('x', 'y')
    rows = [[1,2,3],[3,4,3]]
    with tc.assertRaises(ValueError):
        list_of_records(rows,columns)