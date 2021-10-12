import pytest
import unittest
from module_one._02_scoreboard import *

tc = unittest.TestCase()


def test_scoreboard_validates_score(): 
    sb = Scoreboard()

    with pytest.raises(ScoreValidationError): 
        sb._validate_score(42.3)

    with pytest.raises(ScoreValidationError): 
        sb._validate_score("42")

    with pytest.raises(ScoreValidationError): 
        sb._validate_score(-1)

    
    assert sb._validate_score(1) == 1


def test_scoreboard_push_score_calls_validates_score(mocker): 

    score = 42
    sb = Scoreboard()
    sb._validate_score = mocker.MagicMock(return_value=score)
    sb.push_score(score)

    sb._validate_score.assert_called_with(score)



def test_push_score_works_as_expected(): 

    score = 42 
    sb = Scoreboard()

    sb.push_score(score)
    assert len(sb._scores) == 1 
    assert 42 in sb._scores 

    with pytest.raises(ScoreValidationError):
        sb.push_score("hi")

def test_push_scores_calls_validate_score(mocker): 

    test = [1,4,5,3,2]
    
    sb = Scoreboard()
    sb._validate_score = mocker.MagicMock(return_value=test)
    sb.push_scores(test)

    call_count = sb._validate_score.call_count 
    assert len(test) == call_count 


def test_push_scores_will_append_to_the_scoreboard(mocker): 

    test1 = [1,2,3]
    test2 = [4,5,6]

    sb = Scoreboard()
    
    sb.push_scores(test1)
    sb.push_scores(test2)

    assert sb._scores == test1 + test2


def test_pop_score_returns_last_item_or_none_if_empty(): 

    sb = Scoreboard()
    sb._scores = [1,2,3,4,5]

    assert sb.pop_score() == 5 
    assert len(sb._scores) == 4 

    assert sb.pop_score() == 4 
    assert len(sb._scores) == 3 

    assert sb.pop_score() == 3
    assert len(sb._scores) == 2 
    
    assert sb.pop_score() == 2 
    assert len(sb._scores) == 1

    assert sb.pop_score() == 1 
    assert len(sb._scores) == 0 

    assert sb.pop_score() is None 
    assert sb.pop_score() is None 


def test_get_score_returns_exact_item_or_none(): 

    sb = Scoreboard()   
    sb._scores = [1,2,3,4,5]

    assert sb.get_score(-1) == 5 
    assert sb.get_score(0) == 1
    assert sb.get_score(66) is None 



def test_scoreboard_total_returns_correct_value(): 

    sb = Scoreboard()
    sb._scores = [1,2,3,4,5]

    assert 15 == sb.total()

    sb._scores = []
    assert 0 == sb.total()


def test_scoreboard_greater_than_returns_correct_value(): 

    sb = Scoreboard()
    sb._scores = [1,2,3,4,5,6,7,8,9]

    assert sb.greater_than(5) == [6,7,8,9]
    assert sb.greater_than(9) == []
    assert sb.greater_than(0) == [1,2,3,4,5,6,7,8,9]


def test_scoreboard_less_than_returns_correct_value(): 
    sb = Scoreboard()
    sb._scores = [1,2,3,4,5,6,7,8,9]

    assert sb.less_than(5) == [1,2,3,4]
    assert sb.less_than(10) == [1,2,3,4,5,6,7,8,9]
    assert sb.less_than(0) == []



def test_best_returns_max_value_or_none(): 

    sb = Scoreboard()
    sb._scores = [1,2,3]
    assert sb.best() == 3 

    sb._scores = []
    assert sb.best() is None  

def test_scoreboard_worst_returns_min_value_or_none(): 

    sb = Scoreboard()
    sb._scores = [1,2,3]
    assert sb.worst() == 1 

    sb._scores = []
    assert sb.worst() is None 



def test_scoreboard_top_returns_expected_value(): 

    sb = Scoreboard()
    sb._scores = [5,2,1,6,2,6,8,9]

    assert sb.top(3) == [5,2,1]
    assert sb.top(4) == [5,2,1,6]
    assert sb.top(0) == []
    assert sb.top(42) == sb._scores

    with pytest.raises(ValueError): 
        sb.top(-1)


def test_scoreboard_bottom_returns_expected_value():

    sb = Scoreboard()
    sb._scores = [5,2,1,6,2,6,8,9]

    assert sb.bottom(3) == [6,8,9]
    assert sb.bottom(4) == [2,6,8,9]
    assert sb.bottom(0) == sb._scores
    assert sb.bottom(42) == sb._scores

    with pytest.raises(ValueError): 
        sb.bottom(-1)


def test_scoreboard_mean_returns_expected(stats_scores): 
    sb = Scoreboard()
    sb._scores = stats_scores
    assert round(sb.mean(), 5) == 4.94286


def test_scoreboard_mean_calls_correct_methods(mocker): 
    sb = Scoreboard()
    sb.total = mocker.MagicMock(sb.total, return_value=42)
    sb.length = mocker.MagicMock(sb.length, return_value=42)

    sb.mean()
    sb.total.assert_called_once()
    sb.length.assert_called_once()


def test_scoreboard_mean_returns_none_on_zero_length(): 
    sb = Scoreboard()
    assert sb.mean() is None 


def test_scoreboard_median_returns_expected(stats_scores): 
    sb = Scoreboard()
    sb._scores = stats_scores 
    assert sb.median() == 3 


def test_scoreboard_median_returns_none_on_zero_length(): 
    sb = Scoreboard()
    assert sb.median() is None 


def test_scoreboard_median_calls_correct_methods(mocker): 
    sb = Scoreboard()
    sb.length = mocker.MagicMock(sb.length, return_value=42)

    sb.mean()
    sb.length.assert_called_once()


def test_scoreboard_mode_returns_expected(stats_scores): 
    sb = Scoreboard()
    sb._scores = stats_scores
    #print(sb.mode())
    
    val, occurances = sb.mode()
    
    assert val == 2 
    assert occurances == 9


def test_scoreboard_mode_returns_none_on_zero_length(): 

    sb = Scoreboard()
    assert sb.mode() is None 


def test_scoreboard_variance_returns_expected(stats_scores): 
    sb = Scoreboard()
    sb._scores = stats_scores
    #print(sb.variance())

    assert round(sb.variance(), 5) == 27.42531


def test_scoreboard_variance_calls_correct_methods(mocker): 

    sb = Scoreboard()
    sb._scores = [1,2,3] # we need to add something in here even though we are mocking
    sb.mean = mocker.MagicMock(sb.mean)
    sb.length = mocker.MagicMock(sb.length)

    sb.variance()
    sb.mean.assert_called()
    sb.length.assert_called_once()


def test_scoreboard_variance_returns_none_on_zero_length(mocker):

    sb = Scoreboard()
    assert sb.variance() is None 



def test_scoreboard_stdev_returns_expected(stats_scores): 
    sb = Scoreboard()
    sb._scores = stats_scores
    assert round(sb.stddev(), 5) == 5.31337


def test_scoreboard_stddev_returns_none_on_zero_length(mocker): 
    sb = Scoreboard()
    assert sb.stddev() is None 


def test_scoreboard_calls_correct_methods(mocker): 

    sb = Scoreboard()
    sb.variance = mocker.MagicMock(sb.variance, return_value=42)
    sb.stddev(degrees_of_freedom=1)
    sb.variance.assert_called_once_with(degrees_of_freedom=1)



def test_scoreboard_more_cases():
    s = Scoreboard()

    test_cases = [(3, [1, 2, 3, 4, 5]), 
        (2.5, [1,2,3,4]), 
        (5, [4,2,1,6,3,7,8,3,6,8]), 
        (2, [4,2,10,9,2,0,1,1,7])
    ]

    for t in test_cases:
        solution, case = t
        s._scores = case
        assert s.median() == solution 
