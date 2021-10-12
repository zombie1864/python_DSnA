import os 
import pytest 
import json 
from module_one._03_strmatrix import StrMatrix
from module_one._05_oscillator import Oscillator
from typing import Dict, List, Tuple, Union

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture 
def stats_scores(): 
    return [4,1,11,2,3,1,5,16,7,2,1,1,5,6,
        7,8,9,2,3,2,1,2,4,5,27,2,5,
        2,1,4,2,1,2,14,5]


@pytest.fixture
def matrix_string(): 
    return "1 2 3\n4 5 6\n7 8 9"


@pytest.fixture
def mocked_strmatrix(mocker): 
    res = [[1,2,3], [4,5,6], [7,8,9]]
    mocker.patch.object(StrMatrix, '_parse', return_value=res)    
    return StrMatrix("")


@pytest.fixture 
def mocked_rect_strmatrix(mocker): 
    res = [[1,2,3,5,6], [4,5,6,7,8,9], [7,8,9,10,11,12]]
    mocker.patch.object(StrMatrix, '_parse', return_value=res)    
    return StrMatrix("")


@pytest.fixture
def identity_oscillator(): 
    """NOTE This returns an Oscillator subclass with a 
    simple _generate_waveform override that produces an Identity.
    This allows us to test the abstract base class which we would otherwise 
    be unable to instantiate
    """
    class IdentityOscillator(Oscillator): 
        def _generate_waveform(self, 
            x: List[float], 
            freq: float, 
            amp: float) -> List[float]:
            return x
    return IdentityOscillator()
# waveform file loaders

@pytest.fixture 
def sine_wave(): 
    fp = os.path.join(BASE_DIR, 'tests','data', 'sine.json')
    with open(fp, 'r') as f: 
        return json.load(f)


@pytest.fixture 
def triangle_wave(): 
    fp = os.path.join(BASE_DIR, 'tests','data', 'triangle.json')
    with open(fp, 'r') as f: 
        return json.load(f)