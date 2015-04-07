
# coding: utf-8

# In[31]:

get_ipython().magic(u'matplotlib inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()
        
data = pd.read_csv('https://raw.githubusercontent.com/ga-students/DAT_20_NYC/master/Data/bikeshare.csv?token=AK-cOWzSTyfaa_TSjQ3jADPoylPzPSo9ks5VJdMxwA%3D%3D', sep=',')
print "Number of rows: %i" % data.shape[0]
data.head(10)


# In[32]:

data_byhour = data.groupby('hr')

#Mean number of casual riders per hour

plt.plot(data_byhour['casual'].mean())
plt.xlabel("Hour")
plt.ylabel("Number of casual riders")


# In[33]:

#Mean number of registered riders per hour

plt.plot(data_byhour['registered'].mean())
plt.xlabel("Hour")
plt.ylabel("Number of registered riders")


# In[34]:

plt.plot(data_byhour['cnt'].mean())
plt.xlabel("Hour")
plt.ylabel("Total number of riders")


# In[35]:

data_grp_hr = data.groupby('hr')
print data_grp_hr['cnt'].mean()


# In[36]:

#Peak times of day are 8am and 5pm
#The peak times for all riders and registered riders is very similar. Let's see how it differs from casual riders


# In[37]:

data_grp_hr = data.groupby('hr')
print data_grp_hr['casual'].mean()


# In[38]:

#Peak hours for casual riders are 12pm-5pm.
#We could hypothesize that the peak times for registered and overall users is due to commuters.
#From a business perspective, there are a few things we can think about:
    #Marketing/promotions for casual riders might be best at off peak times(total) during the hours 12-5.
        #This is when most casual riders are active, but there are plenty of available bikes for others.
    #The company might want to look into where the bikes are and where they are being parked during peak times.
        #If peaks are due to commuting, they may be congested in work areas and emptier in tourist and residential areas where casual riders might be.


# In[48]:

data_byday = data.groupby('weekday')

plt.plot(data_byday['casual'].mean())
plt.xlabel("Day of Week")
plt.ylabel("Number of Casual Riders")



data_byday = data.groupby('weekday')

plt.plot(data_byday['registered'].mean())
plt.xlabel("Day of Week")
plt.ylabel("Number of Registered Riders")



data_byday = data.groupby('weekday')

plt.plot(data_byday['cnt'].mean())
plt.xlabel("Day of Week")
plt.ylabel("Total Number of Riders")


# In[40]:

#Jan 1, 2011 was a Saturday
# 0- Sunday
# 1- Monday
# 2- Tuesday
# 3- Wednesday
# 4- Thursday
# 5- Friday
# 6- Saturday


# In[41]:

#Bikes are most used on Thursday and Friday
#Casual riders ride more on weekends
#Registered riders ride more during the week
#One business application would be to have more stations in work areas for commuters.


# In[42]:

data_byseason = data.groupby('season')


# plt.hist(data.year, bins=np.arange(1950, 2013), color='#cccccc')
# plt.xlabel("Release Year")
# remove_border()


plt.hist(data_byseason['casual'].mean, bins=np.arange(1,2,3,4)
plt.xlabel("Season")
plt.ylabel("Number of Riders")


# In[47]:

pd.scatter_matrix(data, figsize=[20, 20], alpha=0.08, diagonal='kde')
plt.show()


# In[ ]:

#The best predictors of number of riders are:
    #Hour- for both casual and registered riders.
    #Weekday- More casual riders ride on the weekends, while registered riders ride on weekdays.

