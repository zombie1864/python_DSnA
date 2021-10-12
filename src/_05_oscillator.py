""" For this module you need to implement an API for producting waveforms common in audio signal processing. 
It is designed to show how you can use object oriented program to make your APIs extensible and minimize repetition. 
Sometimes this is called the DRY principle (Don't Repeat Yourself). In our case we want to be able to implement a family 
of objects with identical interfaces but different implementations.  

The Oscillator is an example of how one might implement an abstract base class in python using the `abc` 
builtin module. This is a class that provides one or more methods that are meant to only be 
implemented in a child class via override. 
"""

import abc
import math
from typing import Dict, List, Tuple, Union
import copy 




# a helper to scale an array between two vals
#https://stats.stackexchange.com/questions/178626/how-to-normalize-data-between-1-and-1
def normalize(x: List[float], a: float, b: float) -> List[float]:
    """Scales the value x between the range [a,b]

    Args:
        x (List[float]): The value to be normalized
        a (float): The min value
        b (float): The max value

    Returns:
        float: normalized value 
    """
    assert a < b, 'a must be less then b'
    min_x = min(x)
    max_x = max(x)
    return [(b - a) * ( (xval-min_x ) / (max_x - min_x) ) + a for xval in x]


def assure_positive(*args: Union[float, int]) -> Tuple[Union[float, int]]:
    """Assures that any inbound float or ints are returned as positive

    Returns:
        Tuple[Union[float, int]]: A tuple of the results. 
    """
    return tuple(abs(num) for num in args)
    

class Point(object): 

    def __init__(self, x: float, y: float):
        """A container object that holds a point as a coordinate pair 
        and allows the caller to create various python objects.

        Args:
            x (float): the x coord
            y (float): the y coord
        """
        self._x = x 
        self._y = y 

    @property 
    def x(self): 
        return self._x 
    

    @property 
    def y(self): 
        return self._y 


    def as_tuple(self) -> Tuple[float]: 
        """Converts point data to a tuple

        Returns:
            Tuple[float]: the tuple x,y
        """
        return (self._x, self._y)

    def as_dict(self) -> Dict[str,float]: 
        """Converts point data to dictionary format

        Returns:
            Dict[str, float]: A dictionary with keys x and y
        """
        return {'x': self._x, 'y': self._y}



class Oscillator(abc.ABC): 
    """This is an Abstract base class. We force the developer to implement 
    the actual waveform generation in subclasses. This is the DRY approach as described in 
    the module doc. The abstract method interface for _generate_waveform provides a hook to 
    change the resulting data based on what type of waveform is desired.
    """

    def __init__(self, sr: int=44100):
        """An oscillator that generates a waveform.

        Args:
            sr (int, optional): The sample rate as a positive integer. Defaults to 44100.
        """
        #** implement this in terms of another method in this class
        
        self._sr = self.set_samplerate(sr)
    

    def _make_points(self, x: List[float], y: List[float]) -> List[Point]:
        """Generate a list of Points.

        Args:
            x (List[float]): The x data
            y (List[float]): The y data

        Returns:
            List[Point]: A list of point objects.
        """

        # ** solve this in one line using a comprehension 

        return [Point(pair[0], pair[1]) for pair in list(zip(x, [round(y_i, 5) for y_i in y]))]


    def _calculate_sampling_index(self, dur: float) -> List[float]:
        """Calculate the sampling index for the wave table for the specified duration. Essentially 
        this creates a uniform index of the samplerate points for the specified index 
        
        ex. 
        >>> s = Sine(sr=10) 
        >>> s._calculate_sampling_index(1)   # calculates 1 second of sample indices at sr 10
        ... [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

        Args:
            dur (float): The durations in seconds.

        Returns:
            List[float]: The sampling index 
        """
        # ** solve this in one line using a comprehension 

        return [num / self._sr for num in range(0, int(self._sr * dur))]
    

    @abc.abstractmethod
    def _generate_waveform(self, x: List[float],  freq: float, amp: float) -> List[float]:
        """This method generates the waveform. It is a hook that should be overridden in concrete 
        subclasses with the specific formula.

        Args:
            x (List[float]): The x array with the calculated sampling index.
            freq (float): The frequency (Hz)
            amp (float): [description]. The amplitude

        Returns:
            List[float]: The generated waveform as a 1d array of floats.
        """       
        # NOTE this is an abstract method and should be implemented in a child class
        

    def set_samplerate(self, sr: int) -> None:
        """A public method that validates and sets the sample rate of the Oscillator.

        Args:
            sr (int): The sample rate. 

        Raises:
            ValueError: Raised if the sample rate is less then 1.
        """
        if sr < 1:
            raise ValueError('samplerate cannot be negative')
        else:
            self._sr = sr 
            return self._sr


    def calc(self, freq: float=1.0, dur: float=1.0, amp: float=1.0) -> List[Point]:
        """Generate a waveform as a list of points. 
        
        NOTE that negative values should work as inputs and amp > 1 the waveform is normalized.

        Args:
            freq (float, optional): The frequency of the waveform. Defaults to 1.0.
            dur (float, optional): The duration of the waveform. Defaults to 1.0.
            amp (float, optional): The amplitude of the waveform. Defaults to 1.0.

        Returns:
            List[Point]: The waveform as a list of Points.
        """
        # ** this public method should be composed of other methods and module level functions.
        pos_freq, pos_dur, pos_amp = assure_positive(freq, dur, amp)
        x = self._calculate_sampling_index(pos_dur)
        y = self._generate_waveform(x, pos_freq, pos_amp)
        out_of_bound_y_values = any(value > 1 for value in y)
        if  amp > 1 or out_of_bound_y_values:
            x = normalize(y, -1.0, 1.0)
        return self._make_points(x, y)


class Sine(Oscillator): 

    def _generate_waveform(self, x: List[float],  freq: float, amp: float) -> List[float]:
        """Generate the y values of a sine wave. Uses the formula found here: 
        https://en.wikipedia.org/wiki/Sine_wave

        Args:
            x (List[float]): The x values to use for the calculation. 
            freq (float): The frequency of the waveform.
            amp (float): The amplitude of the waveform.

        Returns:
            List[float]: The y values of the waveform.
        """
        return [amp * math.sin(2 * math.pi * freq * x_i) for x_i in x]


class Triangle(Oscillator): 

    def _generate_waveform(self, x: List[float], freq: float, amp: float=1.0) -> List[float]: 
        """ Generate the y values of triangle wave. Uses the formula found here:
        https://en.wikipedia.org/wiki/Triangle_wave

        Args:
            x (List[float]): The x values to use for the calculation. 
            freq (float): The frequency of the waveform.
            amp (float): The amplitude of the waveform.

        Returns:
            List[float]: The y values of the waveform.
        """
        return [(2 * amp / math.pi) * math.asin(math.sin((2 * math.pi * freq) * x_i)) for x_i in x]


class Waveform(object):
    """Waveform's job is to interface with the 
    Point API to deliver the correct list of specified objects to the user in a
    straightforward and simplfied manner. This could be considered as a type of proxy 
    or wrapper class to the Point API.
    """


    def __init__(self, points: List[Point]): 
        """A container class that holds points. 

        Args:
            points (List[Point]): A list of Points from an Oscillator
        """
        self._points = points 
    

    def points(self, as_type: str='objects') -> List[Union[Point, Tuple, Dict]]:
        """Returns a new set of points based on the given type. Options are 'objects' 
        to return a list of Points, 'tuples' to return a list of tuples, and 'records' to 
        return a list of dicts. 

        Args:
            as_type (str, optional): The type to return. Defaults to 'objects'.

        Raises:
            ValueError: If an incorrect type string is given.

        Returns:
            List[Union[Point, Tuple, Dict]]: The Waveform as a list of Points, tuples or dicts.
        """

        # ** we can implement this as an if-else block
        new_points =  copy.copy(self._points)
        if as_type == 'objects': 
            return new_points
        elif as_type == 'tuples':
            return [point.as_tuple() for point in new_points]
        elif as_type == 'records':
            return [point.as_dict() for point in new_points]
        else:
            raise ValueError('Incorrect type string given')



class WaveFactory(object): 
    """Responsible for creating a single Waveform given the osc and config. 
    This is an example of a factory pattern where one class is responsible for the complex 
    construction of a desired object or set of object.. 

    The `create` method is an example of what's called the Liskov Substituion Principle and is a
    very important concept in object oriented design. Basically we must guarantee that the public interface 
    of derived classes is identical for any subclass and that they can be used interchangeably.

    In this case any subclass of Oscillator should be able to be used in this factory.
    """

    def create(self, 
        sr: int=44100, 
        freq: float=1.0, 
        dur: float=1.0, 
        amp: float=1.0, 
        osc: Oscillator=Sine()) -> Waveform:
        """Produce a waveform of the given oscillator type.

        Args:
            sr (int, optional): The samplerate. Defaults to 44100.
            freq (float, optional): The frequency. Defaults to 1.0.
            dur (float, optional): The duration. Defaults to 1.0.
            amp (float, optional): The amplitude. Defaults to 1.0.
            osc (int, optional): An instance of an oscilator class. Defaults to Sine().

        Raises:
            WaveFactoryError: If an in

        Returns:
            Waveform: [description]
        """
        osc.set_samplerate(sr)
        return Waveform(osc.calc(freq, dur, amp))

