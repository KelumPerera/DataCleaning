# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:47:03 2018

@author: Kelum Perera
"""
# Scale and Normalize Data

 # Get our environment set up
 # Scaling vs. Normalization: What's the difference?
 # Practice scaling
 # Practice normalization
 
 
 # modules we'll use
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# read in all our data
kickstarters_2017 = pd.read_csv("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/ks-projects-201801.csv")

# set seed for reproducibility
np.random.seed(0)

# Scaling vs. Normalization: What's the difference?
# In both cases, you're transforming the values of numeric variables so that the transformed data points have specific helpful properties.
#  in scaling, you're changing the *range* of your data while in normalization you're changing the *shape of the distribution* of your data.

# By scaling your variables, you can help compare different variables on equal footing.

# generate 1000 data points randomly drawn from an exponential distribution
original_data = np.random.exponential(size = 1000)

# mix-max scale the data between 0 and 1
scaled_data = minmax_scaling(original_data, columns = [0])

# plot both together to compare
fig, ax=plt.subplots(1,2)
sns.distplot(original_data, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")

# Notice that the *shape* of the data doesn't change, but that instead of ranging from 0 to 8ish, it now ranges from 0 to 1


# Normalization
#  Normalization is a more radical transformation. The point of normalization is to change your observations so that they can be described as a normal distribution.
#  Normal distribution is also known as the "bell curve", this is a specific statistical distribution where a roughly equal observations fall above and below the mean, the mean and the median are the same, and there are more observations closer to the mean. The normal distribution is also known as the Gaussian distribution.
#  you'll only want to normalize your data if you're going to be using a machine learning or statistics technique that assumes your data is normally distributed.
#  t-tests, ANOVAs, linear regression, linear discriminant analysis (LDA) and Gaussian naive Bayes


# normalize the exponential data with boxcox
normalized_data = stats.boxcox(original_data)

# plot both together to compare
fig, ax=plt.subplots(1,2)
sns.distplot(original_data, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(normalized_data[0], ax=ax[1])
ax[1].set_title("Normalized data")

#  Practice scaling

# select the usd_goal_real column
usd_goal = kickstarters_2017.usd_goal_real

# scale the goals from 0 to 1
scaled_data = minmax_scaling(usd_goal, columns = [0])

# plot the original & scaled data together to compare
fig, ax=plt.subplots(1,2)
sns.distplot(kickstarters_2017.usd_goal_real, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")

# Practice normalization

# get the index of all positive pledges (Box-Cox only takes postive values)
index_of_positive_pledges = kickstarters_2017.usd_pledged_real > 0

# get only positive pledges (using their indexes)
positive_pledges = kickstarters_2017.usd_pledged_real.loc[index_of_positive_pledges]

# normalize the pledges (w/ Box-Cox)
normalized_pledges = stats.boxcox(positive_pledges)[0]

# plot both together to compare
fig, ax=plt.subplots(1,2)
sns.distplot(positive_pledges, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(normalized_pledges, ax=ax[1])
ax[1].set_title("Normalized data")


