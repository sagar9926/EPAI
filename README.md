# Created By  : Sagar Agrawal

# EPAI : Session 5
"""
## time_it(fn, *args, repetitons= 1, **kwargs) :
"""
#### This module provides a simple way to time small bits of Python code. It takes function name as parameter along withe the arguments for the function. 

#### Another parameter is passed ehich is repetitons. This is by default set at 1. This denotes the iterations of a function performed to calculate the average execution time of the function.


## squared_power_list(number, start=0, end=5, repetitons=5):

#### It takes input a number as an argument and returns a list in which elements are the number raised to the power of values between start and end [Both Inclusive]

#### Throws Value error when parameter number is passed a string argument, also start and end must be positive satisfying start < end.

## polygon_area(side_length, sides = 3):

#### This function calculates and return the area of regular polygon with a precision upto 4 digits. It takes length of a side of polygon as an argument along with the number of sides of the polygon:

#### The sides must be an integer type value otherwise the function raises a ValueError

## temp_converter(temperature, temp_given_in = 'f'):

#### This function converts the value of temperature from Celcius to Farenheit or Farenheit to Celcius. This takes two arguments 

#### 1) . Temperature value to be converted to another scale

#### 2) . The scale of input temperature value (Celcius or Farenheit)

## speed_converter(speed_kmph, dist='km', time='min'):

#### The input speed to this function is kmph and converts speed to other units of measurements.
