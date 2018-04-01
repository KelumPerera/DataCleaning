# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 17:15:57 2018

@author: kelum
"""

# Parsing dates


# Get our environment set up
# Check the data type of our date column
# Convert our date columns to datetime
# Select just the day of the month from our column
# Plot the day of the month to check the date parsing


# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
earthquakes = pd.read_csv("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/Significant Earthquakes 1965-2016_database.csv")
landslides = pd.read_csv("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/Landslides After Rainfall2007-2016catalog.csv")
volcanos = pd.read_csv("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/Volcanic Eruptions in the Holocene Period database.csv")

# set seed for reproducibility
np.random.seed(0)

# print the first few rows of the date column
print(landslides['date'].head())

# check the data type of our date column
landslides['date'].dtype

# create a new column, date_parsed, with the parsed dates
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format = "%m/%d/%y")

# print the first few rows
landslides['date_parsed'].head()

# What if I run into an error with multiple date formats? when there are multiple date formats in a single column

landslides['date_parsed1'] = pd.to_datetime(landslides['date'], format = "%m/%d/%y", infer_datetime_format=True)

# try to get the day of the month from the date column
day_of_month_landslides = landslides['date_parsed1'].dt.day


# Plot the day of the month to check the date parsing (plot a histogram of the days of the month.)
# remove na's
day_of_month_landslides = day_of_month_landslides.dropna()

# plot the day of the month
sns.distplot(day_of_month_landslides, kde=False, bins=31)

