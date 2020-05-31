#-*- coding: utf-8 -*-
#importing tools that are needed

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
p_list = []
n_list = []
h_list = []
ba_list = []
be_list = []
all_var =[]

for page in range(20,1000,20):
    my_url = "https://www.daft.ie/ireland/property-for-sale/?offset=20".format(page)

#open connection and grab webpage
    uClient = uReq(my_url)
#store html in a variable
    page_html = uClient.read() 
#close web connection
    uClient.close()
#parse html
    soup = BeautifulSoup(page_html, "html.parser")
    print(soup)

#grabs listings house information
    listings = soup.findAll("div", {"class":"FeaturedCardPropertyInformation__detailsContainer"})
    
    for container in listings:
#extracting price
        price = container.div.div.strong.text
        price = price.strip('AMV: €')
        price = price.strip('Reserve: €')
        price = price.replace(',', "")
        price = int(price)
        p_list.append(price)
        
        #location
        location = container.div.find("a", {"class":"PropertyInformationCommonStyles__addressCopy--link"}).text
        n_list.append(location)
        #house type
        house = container.div.find("div", {"class":"QuickPropertyDetails__propertyType"}).text
        house = house.strip('for sale')
        h_list.append(house)
        #number of bathrooms
        bath_num = container.div.find("div", {"class":"QuickPropertyDetails__iconCopy--WithBorder"}).text
        #makes str and int
        bath_num = int(bath_num)
        ba_list.append(bath_num)
            #number of bedrooms
        bed_num = container.div.find("div", {"class":"QuickPropertyDetails__iconCopy"}).text
        bed_num = int(bed_num)
        be_list.append(bed_num)
        #makes str and int
        all_var.append((price, location, house, bath_num, bed_num))
        a_v = str(all_var)
        


import mysql.connector
import csv
#creating csv file
with open ('daftdata.csv','w') as file:
    #adding headers to csv file
   #writer = csv.DictWriter(file, fieldnames = ["Price","Address", "House Type", "bathrooms", "Bedrooms"])
   #writer.writeheader()
   #writing every row from the list into the csv file separately
   writer=csv.writer(file)
   for row in all_var:
      writer.writerow(row)
   file.close      
      
mydb = mysql.connector.connect(host='localhost',
    user='username',
    passwd='password',
    database='database')
#prepare cursor
cursor = mydb.cursor()

#Drop the table if it exists
#cursor.execute("DROP TABLE IF EXISTS daftdatabase")
#create database
#mycursor.execute("CREATE DATABASE daftdatabase")
#create table
#mycursor.execute("CREATE TABLE DaftTable(price Integer(10), location VARCHAR(250), type VARCHAR(35), bedrooms INTEGER(2),  bathrooms INTEGER(2))")


with open("daftdata.csv", "r") as infh:
    reader =csv.reader(infh)
#csv_data = csv.reader('daftdata.csv')
    for row in reader:
        if row != []:   
            print(row)
            cursor.execute("INSERT INTO  daftdatabase.dafttable(price, location, type, bedrooms, bathrooms)VALUES(%s, %s, %s,%s,%s)",row)
        
#close the connection to the database.
mydb.commit()
cursor.close()

