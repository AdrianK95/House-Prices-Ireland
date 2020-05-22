library(readxl)
Real_estate_valuation_data_set <- read_excel("Real estate valuation data set.xlsx")
View(Real_estate_valuation_data_set)

# plot latitude and longitude vs price per unit 
plot(Real_estate_valuation_data_set$`X5 latitude`, Real_estate_valuation_data_set$`Y house price of unit area`)
plot(Real_estate_valuation_data_set$`X6 longitude`, Real_estate_valuation_data_set$`Y house price of unit area`)
plot(Real_estate_valuation_data_set$`X6 longitude`, Real_estate_valuation_data_set$`Y house price of unit area`, main = "Longitude Vs House Price Per Unit Area")
# plot latitude and longitude vs price per unit 
plot(Real_estate_valuation_data_set$`X5 latitude`, Real_estate_valuation_data_set$`Y house price of unit area`, main = "Latitude vs House Price Per Unit of Area", xlab = "Latitude Position", ylab = "House price per unit Area")
plot(Real_estate_valuation_data_set$`X6 longitude`, Real_estate_valuation_data_set$`Y house price of unit area`, main = "Longitude Vs House Price Per Unit Area", xlab = "Longitude Position", ylab = "House Price Per Unit Area")
scatter.smooth(x= nearest_station, y= price_area, main="Distance from MRT vs House Price Per Unit", xlab = "Distance from MRT", ylab = "House Price per unti area")

#model of Real Estate Latitude, Longitude and Distance to nearest MTR against house price per unit area
model2= lm(Real_estate_valuation_data_set$`Y house price of unit area`~ Real_estate_valuation_data_set$`X5 latitude`+ Real_estate_valuation_data_set$`X3 distance to the nearest MRT station`+Real_estate_valuation_data_set$`X6 longitude`)
#model = lm(Real_estate_valuation_data_set$`X1 transaction date` + Real_estate_valuation_data_set$`X3 distance to the nearest MRT station` ~ Real_estate_valuation_data_set$`Y house price of unit area`)
summary(model2)
summary(model2)$r.squared
plot(model2)

newdata = data.frame(`X5 latitude` = 24.98034, `X6 longitude`=	121.5395, `X3 distance to the nearest MRT station` =306.59470, data = Real_estate_valuation_data_set)

predict(model2, data = newdata, interval = "confidence")





