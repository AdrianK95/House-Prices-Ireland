# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:35:00 2019

"""
from math import sqrt
import mysql.connector as mysql
data = {}
price = []
name = []
house = []
bathroom = []
bedroom = []
#opening connection to database
try: 
    db = mysql.connect(host = "localhost", user = "root", password = "TotoPanda1", database = "daftdatabase", )

    cursor = db.cursor()

    cursor.execute("select* from dafttable")
    
    info = cursor.fetchall()
    print("Total number of rows in dafttable is:", cursor.rowcount)
    
    print("\nPrinting each laptop record")
    for row in info:
        #gathering price information and adding to list
        Price = row[0]
        price.append(Price)
        print(row)
        print("Price =", row[0],)
        #gathering house location and adding to a list called name
        Name = row[1]
        name.append(Name)
        print("Name =",row[1])
        #gathering house type information and adding to a list called house
        House = row[2]
        house.append(House)
        print("House =", row[2])
        #gathering bathroom information and adding to a list called bathroom
        Bathroom = row[3]
        bathroom.append(Bathroom)
        print("Bathroom=", row[3])
        #gathering bedroom information and adding to a list called bedroom
        Bedroom = row[4]
        bedroom.append(Bedroom)
        print("Bedroom=", row[4])
    
except FileNotFoundError as x:
    print("Error reading data from MYSQL table", x)
#closing connection to database
finally:
    if db.is_connected(): db.close
    cursor.close
    print("MySQL connection is closed")

#calculating statistics
def calculate_mean(price):
    Avg_Price = sum(price)/len(price)
    return Avg_Price

if __name__ =="__main__":
    print("The average house price is:" , calculate_mean(price))
    print("The average number of bedrooms is:" , calculate_mean(bedroom))
    print("The average number of bathrooms is:" , calculate_mean(bathroom))
#median
def calculate_median(bathroom):
    mid_index = int(len(bathroom))/2

    if len(bathroom) % 2 ==1:
        return bathroom[int(mid_index)]
    else:
        median = sum(bathroom[int(mid_index-1):int(mid_index+1)])/2
        return median

if __name__ == "__main__":
    print("The median bedroom number is",calculate_median(bedroom))
    print("The median bathroom number is", calculate_median(bathroom))
    print("The median house price is", calculate_median(price))
#mode 
def calculate_mode(price):
    
    max_price = max(price)
    frequencies = [ price.count(x) for x in range(max_price+1)]    
    print("Price Frequency")
    for i in range(1, len(frequencies)):
        print(f"{i:>3}{frequencies[i]:>6}")

    max_frequency = max(frequencies)
    mode = frequencies.index(max_frequency)
    return mode

        
if __name__=="__main__":
    #print("Most common price length:", calculate_mode(price))
    print("Most common bathroom length:", calculate_mode(bathroom))
    print("Most common bedroom length:", calculate_mode(bedroom))
 #calculate Standard deviation
def standard_deviation(price):
    dev = [ (x - ((sum(price)/len(price)))) ** 2 for x in price]
    std_dev = sqrt(sum(dev)/(len(price)-1))
    return std_dev

if __name__=="__main__":
    print("The Standard deviation of price is:", standard_deviation(price))
    
    #print("The Standard deviation of the number of bathrooms is:", standard_deviation(bathroom))
    #print("The Standard deviation of the number of bedrooms is:", standard_deviation(bedroom))
#creating a correlation between house price and bedroom number
def correlation_co(price,bedroom):
    mean_x = calculate_mean(price)
    mean_y = calculate_mean(bedroom)
    xdev = [x - mean_x for x in price]
    ydev = [y - mean_y for y in bedroom]

    xy_dev = [x*y for (x,y) in zip(xdev, ydev)]
    xstd_dev = [ (x - mean_x) ** 2 for x in price]
    ystd_dev = [ (y- mean_y) ** 2 for y in bedroom]
    return sum(xy_dev)/(sqrt(sum(xstd_dev))*(sqrt(sum(ystd_dev))))

if __name__=="__main__":
    print("The r correlation coefficiant between price and bedroom is:", correlation_co(price,bedroom))
    print("The r correlation coefficiant between price and bedroom is:", correlation_co([1,2,3,4,5],[1,2,3,4,5]))
#pip install collections
#plotting using ggplot
#plotting a bar chart of the number of house types against eachother
from collections import Counter
Counter_type = Counter(house)
    
import matplotlib.pylab as plt

import collections


l = house
w = collections.Counter(l)
fig, ax = plt.subplots()
ax.set_title("Bar Graph of Number of Each house type for sale")
ax.set_xlabel("House type")
ax.set_ylabel("Number of House type")
fig.autofmt_xdate()
ax.bar(w.keys(), w.values())
fig.savefig("barhousetype.png", bbox_inches = "tight")

#plotting price vs bathroom
fig, ax = plt.subplots()
ax.set_title("Scatter Graph of Price vs Number Of Bedrooms")
ax.set_xlabel("Number of Bedrooms")
ax.set_ylabel("House Price")
fig.autofmt_xdate()
ax.scatter(bedroom, price)
fig.savefig("bedroomvsprice.png", bbox_inches = "tight")

#pie chart
location = name
Location = collections.Counter(location)
fig, ax = plt.subplots()
ax.set_title("Pie Chart Of Houses For Sale in Each County")
ax.pie(Location.values(),labels = Location.keys())
fig.savefig("piechart.png", bbox_inches = "tight")
