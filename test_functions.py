# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:34:34 2019

@author: brian
"""
from math import sqrt
def calculate_mean(price):
    Avg_Price = sum(price)/len(price)
    return Avg_Price

def test_calculate_mean():
    assert calculate_mean([1,2,3,4,5,6,7,8,9,10])==(5.5)
    

def calculate_median(bathroom):
    mid_index = int(len(bathroom))/2

    if len(bathroom) % 2 ==1:
        return bathroom[int(mid_index)]
    else:
        median = sum(bathroom[int(mid_index-1):int(mid_index+1)])/2
        return median
    
def test_calculate_median():
    assert calculate_median([1,2,3,4,5]) ==(3)
    
def calculate_mode(price):
    
    max_price = max(price)
    frequencies = [ price.count(x) for x in range(max_price+1)]    
    print("Price Frequency")
    for i in range(1, len(frequencies)):
        print(f"{i:>3}{frequencies[i]:>6}")

    max_frequency = max(frequencies)
    mode = frequencies.index(max_frequency)
    return mode

def test_calculate_mode():
    assert calculate_mode([1,2,3,4,2,3,4,2,5,2,6,2,7])==(2)
    
def standard_deviation(price):
    dev = [ (x - (sum(price)/len(price))) ** 2 for x in price]
    std_dev = sqrt(sum(dev)/(len(price)-1))
    return std_dev

def test_standard_deviation():
    assert standard_deviation([1,2,3,5])==(1.707825127659933)
    
def correlation_co(price,bedroom):
    mean_x = calculate_mean(price)
    mean_y = calculate_mean(bedroom)
    xdev = [x - mean_x for x in price]
    ydev = [y - mean_y for y in bedroom]

    xy_dev = [x*y for (x,y) in zip(xdev, ydev)]
    xstd_dev = [ (x - mean_x) ** 2 for x in price]
    ystd_dev = [ (y- mean_y) ** 2 for y in bedroom]
    return sum(xy_dev)/(sqrt(sum(xstd_dev))*(sqrt(sum(ystd_dev))))

def test_correlation_co():
    assert correlation_co([1,2,3,4],[5,6,7,8])==(0.9999999999999998)
    