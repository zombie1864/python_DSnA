""" This class below is a simple string parser designed around a specific protocol. Parsing 
strings/bytes from one format into another is a very common practice when using python for data 
science or other backend work. 

The detail of the protocol is specified below in the StrMatrix constructor. I have implemented the constructor 
for you and exposed a `property` decorator. This is a best practice way of writing "getter" methods for 
class properties that are common in other languages. 
The python convention for protected/private variables are to underscore them and then only if you want 
to provide access, expose a property. This is often done in such as a way in order to protect or internally alter the
data in some way.

You might notice that unlike the previous scoreboard object, we are passing in a value 
to the constructor itself and validating it. What we are saying here is that this object cannot 
exist without the exact correct input. Often you will see patterns where the constructor is 
essentially used for configuration or takes some combination of data that it may or may not validate 
as well as configuration. It is entirely a design decision and certain patterns work better then 
others for certain situations.

"""

from typing import List
import copy


class StringParseError(ValueError): 
    """ Raised if a string cannot be parsed into integers"""


class StrMatrix(object):
    

    def __init__(self, matrix_string: str):
        """ Given a string of integers seperated by space and rows by newlines

        example: 
            1 2 3 
            4 5 6 
            7 8 9 
        
        Will parse into a row/col matrix of integers.
        [[1,2,3], [4,5,6], [7,8,9]]

        Exposes a public API to return rows, indices or individual values.
        
        """
        self._m = self._parse(matrix_string)


    @property 
    def m(self) -> List[List[int]]: 
        """Returns a deep copy of the internal matrix
        Returns:
            List[List[int]]: The matrix
        """
        # ** explain in detail what the difference is between a copy and deep copy 
        # ** why might we not want to return a reference here? 
        '''
        @property: 
            1. shallow copy creates only a variable referencing to the original 
            2. deepcopy makes a clone of the reference and stores the copy to a vraiable on another memory space 
            3. no reference returned so to not mutate the reference stored on the constructor ( self._m is untouched )
        '''
        matrix_deep_copy = copy.deepcopy(self._m)
        return matrix_deep_copy
        
    
    def _parse(self, mstr: str) -> List[List[int]]:
        """Parses the string protocol into a List of List of integers. Will 
        raise a StringParseError if row lengths are uneven 
        Args:
            mstr (str): [description]
        Raises:
            StringParseError: If a row is uneven length 
        Returns:
            [type]: [description]
        """
        # ** this should be handled with a try-except handler. Our custom exception should be raised from builtin exceptions
        try:
            if not isinstance(mstr, str):
                raise TypeError('A string type must be provided')
            matrix = [[int(num) for num in str_nums.split(' ')] for str_nums in mstr.split('\n')]
            if any(len(matrix[i]) != len(matrix[i+1]) for i in range(len(matrix)-1)):
                raise ValueError('A row contains an uneven length')
            else:
                return matrix
        except (ValueError, TypeError) as err:
            raise StringParseError(str(err)) from err 


    def row(self, i: int) -> List[int]: 
        """Return the ith row of the matrix
        Args:
            i (int): The ith row
        Returns:
            List[int]: A column
        """ 
        return self._m[i]
  

    def column(self, j: int) -> List[int]:
        """Return the jth column of the matrix. 
        Args:
            j (int): The jth column
        Returns:
            List[int]: A column
        """
        col = []
        for row in self._m:
            col.append(row[j])
        return col 


    def fetch(self, i: int, j: int) -> int:
        """Retrieve a specifc value from the matrix. 
        Args:
            i (int): The row index
            j (int): The column index
        Returns:
            int: The value
        """
        return self._m[i][j]


    def transpose(self): 
        """Returns a new matrix that is the transpose of the this 
        matrix.
        Returns:
            List[Tuple[int]]: The transposed matrix as a tuple of integers.
        """
        # implement this in 1 line using a builtin method
        return list(zip(*self._m))
