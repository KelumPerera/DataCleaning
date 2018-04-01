# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:50:57 2018

@author: kelum
"""

#  Handling missing values


# 1. Import Required libraries and load the dataset
# 2. Take a first look at the data
# 3. See how many missing data points we have
# 4. Figure out why the data is missing
# 5. Drop missing values
# 6. Filling in missing values

# Import libraries

import pandas as pd
import numpy as np

# read in all our data
nfl_data = pd.read_csv("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/NFL Play by Play 2009-2017 (v4).csv")
sf_permits = pd.read_csv("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0)

# look at a few rows of the nfl_data file. I can see a handful of missing data already!
nfl_data.sample(5)
nfl_data.describe()
nfl_data.info()
print(nfl_data.shape)

# get the number of missing data points per column
missing_values_count = nfl_data.isnull().sum()

# look at the # of missing points in the first ten columns
missing_values_count[0:43]

# how many total missing values do we have?
print(nfl_data.shape)
total_cells = np.product(nfl_data.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
(total_missing/total_cells) * 100

#  Is this value missing becuase it wasn't recorded or becuase it dosen't exist?
#  If a value is missing becuase it doens't exist (like the height of the oldest child of someone who doesn't have any children) then it doesn't make sense to try and guess what it might be.
#  These values you probalby do want to keep as NaN.
#  if a value is missing becuase it wasn't recorded, then you can try to guess what it might have been based on the other values in that column and row. (This is called "imputation")

# remove all columns with at least one missing value
columns_with_na_dropped = nfl_data.dropna(axis=1)
columns_with_na_dropped.head()

# just how much data did we lose?
print("Columns in original dataset: %d \n" % nfl_data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])


# Try removing all the rows from the nfl_data dataset that contain missing values. How many are left?
nfl_data_columns_with_na_dropped = nfl_data.dropna(axis=0)
print("Rows in original dataset: %d \n" % nfl_data.shape[0])
print("Rows with na's dropped: %d" % nfl_data_columns_with_na_dropped.shape[0])

# get a small subset of the NFL dataset (first 5 rows of the columns from 'EPA' to 'Season')
subset_nfl_data = nfl_data.loc[:, 'EPA':'Season'].head()
subset_nfl_data

# 1. replace all NA's with 0
subset_nfl_data.fillna(0)

# 2. replace all NA's the value that comes directly after it in the same column, 
# then replace all the reamining na's with 0
subset_nfl_data.fillna(method = 'bfill', axis=0).fillna(0)

# 3.Replace with mean of each column

from sklearn.preprocessing import Imputer # scikit-learn contains amazing libraries to make ML models, so we import 'preprocesing' library that lot of classes, methods to preprocess any dataset, so we import 'Imputer' class which helps to handle missing data.

imputer = Imputer(missing_values='NaN',strategy = 'mean', axis=0) # create an object call inputer, press ctrl + i to inspeact the imputer class
imputer.fit(nfl_data.loc[:, 'EPA':'Season'])       # 'EPA':'Season' means we select column 'EPA'to 'Season'
nfl_data.loc[:, 'EPA':'Season'] = imputer.transform(nfl_data.loc[:, 'EPA':'Season']) # transform methode is used to replace NaN values
print(imputer)
print(nfl_data.loc[:, 'EPA':'Season'])

