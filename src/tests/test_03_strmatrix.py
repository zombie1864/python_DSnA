import pytest

from module_one.tests.conftest import matrix_string
from module_one._03_strmatrix import StrMatrix, StringParseError 



def test_matrix_parser_works_as_expected(matrix_string): 

    result = StrMatrix._parse(StrMatrix, matrix_string) 
    assert result == [[1,2,3], [4,5,6], [7,8,9]]


def test_matrix_parser_raises_stringparseerror_if_row_length_uneven(matrix_string): 

    test = matrix_string[:9]
    with pytest.raises(StringParseError):
        StrMatrix._parse(StrMatrix, test)
    
def test_matrix_parser_raises_stringparseerror_cannot_be_coerced_to_int(matrix_string): 

    test = matrix_string + "\n42.3 41.6 34.4"
    with pytest.raises(StringParseError):
        StrMatrix._parse(StrMatrix, test)


def test_m_property_returns_deep_copy(mocked_strmatrix): 

    assert mocked_strmatrix.m is not mocked_strmatrix._m
    assert mocked_strmatrix.m == mocked_strmatrix._m


def test_matrix_row(mocked_strmatrix): 
    
    assert mocked_strmatrix.row(0) == [1,2,3]
    assert mocked_strmatrix.row(1) == [4,5,6]
    assert mocked_strmatrix.row(2) == [7,8,9]
    assert mocked_strmatrix.row(-1) == [7,8,9]

    with pytest.raises(IndexError): 
        mocked_strmatrix.row(42)

def test_matrix_column(mocked_strmatrix): 
    assert mocked_strmatrix.column(0) == [1,4,7]
    assert mocked_strmatrix.column(1) == [2,5,8]
    assert mocked_strmatrix.column(2) == [3,6,9]
    assert mocked_strmatrix.column(-1) == [3,6,9]

    with pytest.raises(IndexError): 
        mocked_strmatrix.column(100)

def test_matrix_fetch(mocked_strmatrix): 
    assert mocked_strmatrix.fetch(0,0) == 1
    assert mocked_strmatrix.fetch(1,1) == 5
    assert mocked_strmatrix.fetch(2,2) == 9
    assert mocked_strmatrix.fetch(1,2) == 6
    assert mocked_strmatrix.fetch(-1,-2) == 8

    with pytest.raises(IndexError): 
        mocked_strmatrix.fetch(42,42)


def test_matrix_transpose(mocked_strmatrix, mocked_rect_strmatrix): 

    assert mocked_strmatrix.transpose() == [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    
    assert mocked_rect_strmatrix.transpose() == [(1, 4, 7), (2, 5, 8), (3, 6, 9), 
        (5, 7, 10), (6, 8, 11)]

