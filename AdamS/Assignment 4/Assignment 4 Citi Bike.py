__author__ = 'asilver'

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('https://raw.githubusercontent.com/ga-students/DAT_20_NYC/master/Data/bikeshare.csv?token=AK6ldYwh173urQ63Wy78HnFFkKfEcSiLks5VJfhQwA%3D%3D').dropna()

#Reviewing the data:
#print data.shape[0]
#print data.head()

#Exploring the data by hour
data_grp_hr = data.groupby('hr')

print data_grp_hr['cnt'].mean()
print data_grp_hr['casual'].mean()
print data_grp_hr['registered'].mean()

#visualizing mean data by hour
plt.plot(data_grp_hr['cnt'].mean())
plt.xlabel("Hourly Mean Users")
plt.show()
#Conclusion: On average, volume peaks at 8AM and 4PM
#Casual users do not have multiple distinct peaks, they tend to use bikes during the daylight hours
#However, the relative volume of registered users means that distinct peaks are visible in the overall data

#Exploring the data by day
data_grp_day = data.groupby('weekday')

print data_grp_day['cnt'].mean()
print data_grp_day['casual'].mean()
print data_grp_day['registered'].mean()

#visualizing mean data by day
plt.plot(data_grp_day['cnt'].mean())
plt.xlabel("Daily Mean Users")
plt.show()
#Conclusion: Mean registered riders drops dramatically on the weekend
#Casual riders, however, are almost exclusively present on weekends

#Exploring the linear relationships with a scatter matrix
pd.scatter_matrix(data, figsize=[16, 16], alpha=0.2, diagonal='kde')
plt.show()
#Conclusion: All weather factors seem to have a more significant effect on casual riders
#Casual riders are less likely to ride in very humid or very cold conditions.
#Both groups, however, are equally effected by wind speed - neither group of riders will ride in high winds

#Business impact: The opportunity for acquiring more riders seems centered around casual riders. Barring a weather machine, Citi bike should do more to weatherproof bicycles.
#Low temparature seems to have the greatest effect on casual ridership, so heated grips/seats would likely help casual riders be more comfortable with cold weather.
#Also, Citi should offer promotions between 9AM and 4PM on weekdays, because that's when the majority of bikes are not in use by casual or registered riders
