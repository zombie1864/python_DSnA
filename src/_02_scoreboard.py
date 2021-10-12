"""Implement all the methods this Scoreboard class based on the specs in the docstring. 
Think of it as a component to some larger program where it's job is to track some data about scores and 
give some statistics. Wrapping functionality like this allows us to expose clear APIs to the 
users of our libraries. 

In this case we are exposing a "Stack" like data structure by using a list
to store data within the class but limiting the available operations. 
This is known as "composition over inheritance" and is a key principle of object oriented design.

NOTE that in python there are no "private" methods and variables but it is convention to use 
an underscore in front to denote that those details are internal to the class.
"""

from typing import List, Optional, Tuple, Union
import math
import collections



class ScoreValidationError(Exception): 
    """ raised if scores do not meet requirements"""


class Scoreboard(object): 
    """ A simple class that tracks scores using a stack like API. Allows the user 
    to push and pop from the end of the score list and get some basic metadata and summary 
    statistics.
    """
    def __init__(self) -> None:
        self._scores = []


    def _validate_score(self, score: int) -> int: 
        """ Validates an incoming score assuring that it is an integer and 
        that it is greater then zero
        

        Args:
            score ([int]): A score value

        Raises:
            ScoreValidationError: If not an integer or if a score is greater then zero.

        Returns:
            int: The valid score
        """

        # ** implmentation should re-raise a ScoreValidationError from a TypeError and ValidationError after catching those errors
        try:
            if not isinstance(score,int):
                raise TypeError(f'{type(score)} is not of type int')
            elif score < 0:
                raise ValueError('score is cannot be negative') 
            else:
                return score 
        except (ValueError, TypeError) as err:
            raise ScoreValidationError(str(err)) from err 


    def push_score(self, score: int) -> None:  
        """ Validates and pushes a score onto the end of the Scoreboard.

        Args:
            score (int): [description]
        """

        # ** which internal method should this call first?
        self._scores.append(self._validate_score(score))


    def push_scores(self, scores: List[int]) -> None:  
        """ Validates and pushes multiple scores into the Scoreboard.
        
        Args:
            scores (List[int]): A list of new scores
        """
        # ** which internal method should this use to validate incoming scores?
        self._scores.extend([self._validate_score(score) for score in scores])

    
    def pop_score(self) -> Optional[int]:
        """Removes and returns the last score from the list. 
        If the list is empty returns None

        Returns:
            Optional[int]: [description]
        """

        # ** implement this using try-except for a specific exception type  
        try:
            return self._scores.pop()
        except IndexError:
            return None


    def length(self) -> int:  
        """Return the current length of scores.

        Returns:
            int: [description]
        """
        return len(self._scores)


    def get_score(self, idx: int) -> Optional[int]:  
        """ Return a score given the index or None if the index is
        out of range. This does not modify actual scores but only retrieves 
        the value.

        Args:
            idx (int): The index.

        Returns:
            int: The int.
        """

        # ** implement this using try-except for a specific exception type
        try:
            return self._scores[idx]
        except IndexError:
            return None 


    def total(self) -> int: 
        """ Return the total of all scores in the list.

        Returns:
            int: The total.
        """  
        return sum(self._scores)


    def greater_than(self, value: int) -> List[int]:  
        """Returns a list of scores that are greather then 
        the given value.

        Args:
            value (int): The value to check against.

        Returns:
            List[int]: Values greater then target
        """
        # ** do this in one line with a comprehension 
        return [score for score in self._scores if score > value]


    def less_than(self, value: int) -> List[int]: 
        """Return a list of scores that are less than the given value.

        Args:
            value (int): The target value

        Returns:
            List[int]: Values less then target
        """
        # ** do this in one line with a comprehension 
        return [score for score in self._scores if score < value]


    def best(self) -> Optional[int]:  
        """Return the highest score. If there are no scores 
        returns None 

        Returns:
            Optional[int]: The highest score in the list.
        """
        # implement this with a builtin function 
        # implmenent this with a try-except using a specific expection 
        try:
            return max(self._scores) 
        except ValueError: 
            return None 


    def worst(self) -> Optional[int]:  
        """Return the lowest score. If there are no scores 
        returns None 

        Returns:
            Optional[int]: The lowest score in the list 
        """
        # implement this with a builtin function
        # implmenent this with a try-except using a specific expection 
        try:
            return min(self._scores)
        except ValueError:
            return None


    def top(self, n: int) -> List[int]: 
        """Return the first n scores. These are not the best, just the 
        first that were entered into the scoreboard.

        Args:
            n (int): The number of scores to return 

        Raises: 
            ValueError: if n is negative 

        Returns:
            List[int]: The top n scores 
        """
        # ** implement using a slice 
        if n < 0:
            raise ValueError('n cannot be negative')
        else:
            return self._scores[:n]


    def bottom(self, n: int) -> List[int]: 
        """Return the last n scores. These are not the worst scores, just 
        the last n that were entered into the scoreboard 

        Args:
            n (int):The number of scores to return 

        Raises: 
            ValueError: if n is negative 

        Returns:
            List[int]: The lowest n scores
        """
        # implement using a slice 
        if n < 0:
            raise ValueError('n cannot be negative')
        else: 
            return self._scores[-n:]


    def mean(self) -> Optional[float]: 
        """Calculates the mean score or None if there are no scores.

        Returns:
            Optional[float]: [description]
        """

        # ** implement this by hand without the `statistics` module
        # ** implement this using other methods in this class. 
        # ** implement this using a try-except for a specific exception subclass.
        try:
            return self.total() / self.length()
        except ZeroDivisionError:
            return None 


    def median(self) -> Optional[Union[float, int]]: 
        """ Returns the median value or None if there 
        are no scores.

        Returns:
            Optional[Union[float, int]]: The median or
        """

        # ** implement this by hand without the `statistics` module
        # ** describe how you will implement the algo before writing the code.
        sorted_scores = sorted(self._scores)
        if self.length() == 0:
            return None 
        elif self.length() % 2: 
            return sorted_scores[math.floor(len(sorted_scores)/2)]
        else: # NOTE i have included simple test to check against this arm, see below
            return (sorted_scores[(int(len(sorted_scores)/2)-1)]+sorted_scores[int(len(sorted_scores)/2)])/2 
    '''
    median: 
        1. return none if there are no scores 
        2. if the len(scores) is odd -> return the score in the middile by finding the middle index 
        EX: [1, 2, 3, 4, 5] <=> mid_idx = len(l) / 2 (round down)
        3. if the len(scores) is odd -> return the avg of the two middle nums 
        EX: [1, 2, 3, 4, 5, 6] <=> (3 + 4) / 2 => 3.5 
    ''' 

    def mode(self) -> Optional[Tuple[int]]: 
        """Return the mode of the scores and the number of occurances or 
        None if there are no scores.

        Returns:
            Optional[Tuple[int]]: Returns a tuple of the value
        """

        # ** implement this by hand without the `statistics` module
        # ** use a class from the collections module to complete this instead
        # ** do not use a try-except approach to handle None cases, but instead another method on the class.
        if len(self._scores) == 0:
            return None
        count_container = collections.Counter(self._scores)
        return count_container.most_common(1)[0]

        
    def variance(self, degrees_of_freedom: int=0) -> Optional[float]: 
        """Compute the variance of the scores with degrees of freedom. 
        
        Look here https://www.statisticshowto.com/probability-and-statistics/variance

        Args:
            degrees_of_freedom (int, optional): The degrees of freedom that are subtracted from the 
                total population. Defaults to 0.

        Returns:
            Optional[float]: The variance or None 
        """
        # ** implement this by hand without the `statistics` module 
        # ** calculate this in terms of other methods in this class
        # ** implement this using a try-except for a specific exception subclass.
        try:
            return sum( (score - self.mean())**2 for score in self._scores ) / ( self.length() - degrees_of_freedom )
        except ZeroDivisionError:
            return None


    def stddev(self, degrees_of_freedom: int=1) -> Optional[float]:  
        """Calculate the standard deviation of the scores. 

        Look here https://www.scribbr.com/statistics/standard-deviation/

        Args:
            degrees_of_freedom (int, optional): The degrees of freedom that are subtracted 
                from the total population. Defaults to 1.

        Returns:
            Optional[float]: The stddev or None 
        """
        # ** implement this by hand without the `statistics` module
        # ** calculate this in terms of other methods in this class  
        return math.sqrt(self.variance(degrees_of_freedom)) or None



