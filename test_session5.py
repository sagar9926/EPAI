import pytest
import random
import string
import session5
import os
import inspect
import re
import math
from session5 import squared_power_list, polygon_area,temp_converter,speed_converter

README_CONTENT_CHECK_FOR = [
    
    "time_it",
    "squared_power_list",
    "polygon_area",
    "temp_converter",
    "speed_converter"
        ]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding = "utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 260, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding = "utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = "utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        print(space)
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_time_it_negative_repetitions():
    with pytest.raises(ValueError):
        session5.time_it(print, 1,2,3,4, sep='-', end= ' ***\n', repetitons=-1)

def test_time_it_float():
    assert isinstance(session5.time_it(print, 1,2,3,4, sep='-', end= ' ***\n', repetitons=10),float), "The average time output must be a float value"
    
def test_squared_power_list_negative_start_and_end():
    with pytest.raises(ValueError):
        session5.time_it(squared_power_list,5,start = -1,end = 10, repetitons = 10)
    with pytest.raises(ValueError):
        session5.time_it(squared_power_list,5,start = 0,end = -10, repetitons = 10)

def test_squared_power_list_start_less_than_end():
    with pytest.raises(ValueError):
        session5.time_it(squared_power_list,5,start = 10,end = 3, repetitons = 10)
        
def test_squared_power_list_number():
    with pytest.raises(ValueError):
        session5.time_it(squared_power_list,"Sagar",start = 0,end = 10, repetitons = 10)


def test_squared_power_list_implementation():
    number = random.randint(1,10)
    start = 0
    end = random.randint(1,8)
    assert session5.squared_power_list(number = number, start=start, end=end) == [number**i for i in range(end - start + 1)] ,"Implementation of squared_power_list is incorrect " 

def test_polygon_area_negative_side_length():
    with pytest.raises(ValueError):
        session5.time_it(polygon_area,-1, sides = 3)
 
def test_polygon_area_invalid_sides():
    with pytest.raises(ValueError):
        session5.time_it(polygon_area,3, sides = 2)

def test_polygon_area_sides_less_than_7():
    with pytest.raises(ValueError):
        session5.time_it(polygon_area,7, sides = 7)
        
def test_polygon_area_non_integer_sides():
    with pytest.raises(ValueError):
        session5.time_it(polygon_area,3,sides = 5.5)
   
def test_polygon_area():
    side_length = random.randint(1,100)
    
    # Regular Triangle
    assert session5.polygon_area(side_length,3) == round(math.sqrt(3)/4*side_length**2,4) , "Polygon area function is not able to compute area of Regular Triangle"
    
    # Regular Square
    assert session5.polygon_area(side_length,4) == round(side_length**2,4) , "Polygon area function is not able to compute area of Regular Square"
    
    # Regular Pentagon
    assert session5.polygon_area(side_length,5) == round(1/4*(math.sqrt(5 * ( 5 + 2*math.sqrt(5))))*side_length**2,4) , "Polygon area function is not able to compute area of Regular Pentagon"
    
    # Regular Hexagon
    assert session5.polygon_area(side_length,6) == round(3*math.sqrt(3)/2*side_length**2,4) , "Polygon area function is not able to compute area of Regular Hexagon"

def test_temp_converter_illegal_temp_given_in():
    with pytest.raises(ValueError):
        session5.time_it(temp_converter,temperature = 30, temp_given_in = 'd', repetitons = 10)
        
def test_temp_converter_temperature_type_check():
    with pytest.raises(ValueError):
        session5.time_it(temp_converter,temperature = "FortyThree", temp_given_in = 'c', repetitons = 10)


def test_temp_converter_Celcius_to_Farenheit():
    # Celcius to Farenheit
    Celsius = random.randint(10,100)
    assert round(session5.temp_converter(temperature = Celsius,temp_given_in = 'c'),3)  == round(((Celsius * 9/5) + 32),3) , "Error while converting temperature from Celcius to Farenheit"
  
def test_temp_converter_Farenheit_to_Celcius():
    Fahrenheit = random.randint(10,100)
    # Farenheit to Celcius
    assert session5.temp_converter(temperature = Fahrenheit,temp_given_in = 'f') == ((Fahrenheit - 32) * 5/9 ) , "Error while converting temperature from Farenheit to Celcius"

def test_speed_converter_invalid_speed():
    with pytest.raises(ValueError):
        session5.time_it(speed_converter,speed_kmph= -5,dist='km', time='min')

def test_speed_converter_Kmpph_to_ft_per_min():
    assert  session5.speed_converter(speed_kmph= 20,dist='ft', time='min') == round(20*54.680664917,4)
    
def test_speed_converter_numerator_unit():
    with pytest.raises(ValueError):
        session5.time_it(speed_converter,speed_kmph= 20,dist='sagar', time='min')
        
def test_speed_converter_denominator_unit():
    with pytest.raises(ValueError):
        session5.time_it(speed_converter,speed_kmph= 20,dist='km', time='EPAI')
