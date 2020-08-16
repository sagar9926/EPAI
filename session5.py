from time import perf_counter
import math

def time_it(fn, *args, repetitons= 1, **kwargs):
    if repetitons <= 0:
        raise ValueError(f"repetitons value cannot be zero or negetive")
    time_start = perf_counter()
    for i in range(repetitons):
        fn(*args,**kwargs)
    time_end = perf_counter()
    return((time_end - time_start)/repetitons)

def squared_power_list(number, start=0, end=5):
    if isinstance(number,str):
        raise ValueError(f"Invalid argument for number parameter")
    if start < 0 or end < 0:
        raise ValueError(f'{"start" if start < 0 else "end"} value cannot be negetive')
    elif end < start :
        raise ValueError("End value must be greater than Start")
    else:
        result = [number**i for i in range(end - start + 1)]
        print(result)
    return(result)

def polygon_area(side_length, sides = 3):
    if not isinstance(sides,int):
        raise ValueError("Number of sides of a polygon must be an integer")
    if side_length <= 0:
        raise ValueError(f"side_length value cannot be zero or negetive")    
    if sides < 3 :
        raise ValueError(f"Number of sides of any polygon is always greater than 3 ")        
    if sides > 6 :
        raise ValueError(f"Maximum Number of sides of polygon for this area implementation code must be <=6 ")        
    area = (side_length**2 * sides)/(4 * math.tan(math.pi/sides)) 
    return(round(area,4))

def temp_converter(temperature, temp_given_in = 'f'):
    if isinstance(temperature,str):
        raise ValueError("Temperature can't be a string value")
    if temp_given_in == 'f' :
        # convert to celcius
        temp_celcius = (temperature - 32)*5/9
        return(temp_celcius)
    elif temp_given_in == 'c' :
        # convert to celcius
        temp_farenht = 9/5*temperature + 32
        return(temp_farenht)
    else:
        raise ValueError(f"Invalid input given for temp_given_in, valid inputs are f (Farenheit), c (Celcius)")

def speed_converter(speed_kmph, dist='km', time='min'):
    if speed_kmph <= 0:
        raise ValueError(f"speed value cannot be zero or negetive")
    if dist not in ["km","meter","ft","yrd"]:
        raise ValueError(f"Enter the correct unit for distance conversion")
    if time not in ["msec","sec","min","hr","day"]:
        raise ValueError(f"Enter the correct unit for distance conversion")
    dist_map = {"km" : 1 ,"meter" : 1000, "ft" :3280.84 ,"yrd" : 1093.6132983377 }    
    time_map = {"msec" : 60*60 * 10**3, "sec" : 60*60, "min" : 60 ,"hr" : 1 , "day" : 1/(24) }
    return(round(speed_kmph*dist_map[dist] / time_map[time],4))
