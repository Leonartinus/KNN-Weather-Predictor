# KNN-Weather-Predictor
## Description

The project is a academic project that examine the performance of the k-nearest neighbors (KNN) algorithm in rain perdiction.
KNN algorithm is a non-parametric supervised learning method that is used for classification, find k nearest neighbors of a data point, and check the probabilities that it belong to specific categories.

In this project, the model is trained using the datasets from YVR weather station, including the fields such as temperature, humidity, wind direction and weathre etc.
The model is able to predict if it will rain in the next hour at YVR, given the current climate data and the current weather.

The accuracy of the prediction is maximized (99.86%) when k = 5.

## Method
- The historical climate data were selected from the Vancouver International Airport Weather Station downloaded from the government of Canada official website. https://climate.weather.gc.ca/historical_data/search_historic_data_stations_e.html?searchType=stnName&timeframe=1&txtStationName=VANCOUVER+INTL+A&searchMethod=contains&optLimit=yearRange&StartYear=1840&EndYear=2024&Year=2024&Month=3&Day=3&selRowPerPage=25
- Read and Write csv.py reorganized the data into training and testing datasets.
- The KNN algorithm was trained and tested by using the datasets in the previous step.
- The previous step had been repeated several times using different K values.
- The accuracy of the algorithm with different K was calculated.

## Result
![image](https://github.com/Leonartinus/KNN-Weather-Predictor/assets/124462427/4e726f07-b828-4de5-a1e2-1ed6eeea754a)


The accuracy of the prediction is maximized (99.86%) when k = 5.
