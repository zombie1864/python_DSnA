import pytest 

from module_one._05_oscillator import normalize, assure_positive,\
    Point, Sine, Triangle, Waveform, WaveFactory

import module_one._05_oscillator

def test_osc_normalize_returns_expected(): 
    x = [1.0, 2.1, 3.2, 4.0, 5.4]

    y = normalize(x, -1, 1)
    assert y == [-1.0, -0.5, 0.0, 0.36363636363636354, 1.0]



def test_osc_assure_positive():

    args = [-1.0, 1.0, -2.0, 2.0]

    assert assure_positive(*args) == (1.0, 1.0, 2.0, 2.0) 
    assert assure_positive() == ()
    assert assure_positive(0) == (0,)


def test_point_converts_to_correct_types(): 

    p = Point(1.0,1.0)

    assert p.as_tuple() == (1.0, 1.0)
    assert p.as_dict() == {'x': 1.0, 'y': 1.0}


def test_oscillator_can_make_points(identity_oscillator):  

    osc = identity_oscillator
    osc._sr = 10

    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [1.0, 2.0, 3.0, 4.0, 5.0]

    points = osc._make_points(x,y)

    for i,p in enumerate(points): 
        assert isinstance(p, Point)
        assert x[i] == points[i].x
        assert y[i] == points[i].y

def test_oscillator_calculates_the_correct_sampling_index(identity_oscillator):

    osc = identity_oscillator
    osc._sr = 10
    idx = osc._calculate_sampling_index(1)

    assert idx == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    idx = osc._calculate_sampling_index(2)
    assert idx == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 
        0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
    
    osc._sr = 20 

    idx = osc._calculate_sampling_index(1)
    assert idx == [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 
        0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]

    
    osc._sr = 40 
    idx = osc._calculate_sampling_index(1)
    assert idx == [0.0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 
        0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 
        0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 
        0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 
        0.875, 0.9, 0.925, 0.95, 0.975]


def test_oscillator_makes_correct_calls_with_default_input(mocker, identity_oscillator): 

    osc = identity_oscillator

    normalize_spy = mocker.spy(module_one._05_oscillator, 'normalize') # assert not called
    assure_pos_spy = mocker.spy(module_one._05_oscillator, 'assure_positive')
    samp_idx_spy = mocker.spy(osc, '_calculate_sampling_index')
    gen_wavefrom_spy = mocker.spy(osc, '_generate_waveform')
    make_points_spy = mocker.spy(osc, '_make_points')

    osc._sr = 10
    osc.calc()

    fake_data = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    osc._calculate_sampling_index = mocker.MagicMock(osc._calculate_sampling_index, return_value=fake_data)
    osc._generate_waveform = mocker.MagicMock(osc._generate_waveform, return_value=fake_data)


    normalize_spy.assert_not_called()
    assure_pos_spy.assert_called_once_with(1.0, 1.0, 1.0)
    samp_idx_spy.assert_called_once_with(1.0)
    gen_wavefrom_spy.assert_called_once_with(fake_data, 1.0, 1.0)
    make_points_spy.assert_called_once_with(fake_data, fake_data)

    

def test_oscillator_calls_normalized_with_out_of_bounds_input(mocker, identity_oscillator): 
    
    osc = identity_oscillator
    normalize_spy = mocker.spy(module_one._05_oscillator, 'normalize')

    fake_data = [42.0,42.0,-42.0]
    osc._generate_waveform = mocker.MagicMock(osc._generate_waveform, return_value=fake_data)
    osc.calc()

    normalize_spy.assert_called_once_with(fake_data, -1.0, 1.0)



def test_sine_osc_calc_generates_correct_waveform(sine_wave): 

    osc = Sine(sr=1000)

    points = osc.calc()
    data = [p.as_dict() for p in points] 
    
    assert sine_wave == data


def test_triangle_osc_calc_generates_correct_waveform(triangle_wave): 

    osc = Triangle(sr=1000)
    points = osc.calc()
    
    data = [p.as_dict() for p in points]
    assert triangle_wave == data


def test_waveform_returns_specified_types(): 

    points = [ 
        Point(1.0,1.0), 
        Point(2.0,2.0),
        Point(3.0,3.0)
    ]

    wf = Waveform(points)

    assert wf.points() == points 
    assert wf.points() is not points 
    assert wf.points('tuples') == [
        (1.0,1.0),
        (2.0,2.0), 
        (3.0,3.0)
    ]
    assert wf.points('records') == [
        {'x': 1.0, 'y': 1.0},
        {'x': 2.0, 'y': 2.0},
        {'x': 3.0, 'y': 3.0},
    ]

def test_waveform_raies_error_on_invalid_type(): 

    wf = Waveform([]) 
    with pytest.raises(ValueError): 
        wf.points('something')


def test_wavefactory_makes_correct_calls(mocker): 

    osc = Sine()
    set_sr_spy = mocker.spy(osc, 'set_samplerate')
    calc_spy = mocker.spy(osc, 'calc')

    factory = WaveFactory()   
    waveform = factory.create(42,1,2,3, osc)
    assert isinstance(waveform, Waveform)


    set_sr_spy.assert_called_once_with(42)
    calc_spy.assert_called_once_with(1,2,3)
