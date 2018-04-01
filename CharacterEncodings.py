# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 17:35:46 2018

@author: kelum
"""

# Character Encodings


# Get our environment set up
# What are encodings?
# Reading in files with encoding problems
# Saving your files with UTF-8 encoding


# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import chardet

# set seed for reproducibility
np.random.seed(0)


# What are encodings?

# These are  are specific sets of rules for mapping from raw binary byte strings (that look like this: 0110100001101001) to characters that make up human-readable text (like "hi").

# start with a string
before = "This is the euro symbol: €"

# check to see what datatype it is
type(before)

# encode it to a different encoding, replacing characters that raise errors
after = before.encode("utf-8", errors = "replace")

# check the type
type(after)

# take a look at what the bytes look like
after

# That's because bytes are printed out as if they were characters encoded in ASCII. (ASCII is an older character encoding that doesn't really work for writing any language other than English.) Here you can see that our euro symbol  has been replaced with some mojibake that looks like "\xe2\x82\xac" when it's printed as if it were an ASCII string.

# convert it back to utf-8
print(after.decode("utf-8"))

# try to decode our bytes with the ascii encoding
print(after.decode("ascii"))



# start with a string
before = "This is the euro symbol: €"

# encode it to a different encoding, replacing characters that raise errors
after = before.encode("ascii", errors = "replace")

# convert it back to utf-8
print(after.decode("ascii"))


#  Reading in files with encoding problems

# try to read in a file not in UTF-8
kickstarter_2016 = pd.read_csv("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/ks-projects-201801.csv")

# look at the first ten thousand bytes to guess the character encoding
with open("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/ks-projects-201801.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(1000000))

# check what the character encoding might be
print(result)

# read in the file with the encoding detected by chardet
kickstarter_2016 = pd.read_csv("E:/MyData/LearningVideos/DataSets/DataSets4DataCleaning/ks-projects-201801.csv", encoding='utf-8')

# look at the first few lines
kickstarter_2016.head()

# Your Turn! Trying to read in this file gives you an error. Figure out
# what the correct encoding should be and read in the file. :)
police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv")


#  Saving your files with UTF-8 encoding

# save our file (will be saved as UTF-8 by default!)
kickstarter_2016.to_csv("ks-projects-201801-utf8.csv")

