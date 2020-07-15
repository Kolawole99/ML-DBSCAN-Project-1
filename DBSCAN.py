#=============================IMPORTING REQUIRED LIBRARIES========================
import numpy as np 
from sklearn.cluster import DBSCAN 
from sklearn.datasets.samples_generator import make_blobs 
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt 
import csv
import pandas as pd
import numpy as np
#%matplotlib inline #for jupyter notebooks

#====================================DATA====================================

#=============================Data object keys==========================
# Stn_Name	    Station Name
# Lat	        Latitude (North+, degrees)
# Long	        Longitude (West - , degrees)
# Prov	        Province
# Tm	        Mean Temperature (°C)
# DwTm	        Days without Valid Mean Temperature
# D	            Mean Temperature difference from Normal (1981-2010) (°C)
# Tx	        Highest Monthly Maximum Temperature (°C)
# DwTx	        Days without Valid Maximum Temperature
# Tn	        Lowest Monthly Minimum Temperature (°C)
# DwTn	        Days without Valid Minimum Temperature
# S	            Snowfall (cm)
# DwS	            Days without Valid Snowfall
# S%N	            Percent of Normal (1981-2010) Snowfall
# P	            Total Precipitation (mm)
# DwP	            Days without Valid Precipitation
# P%N	            Percent of Normal (1981-2010) Precipitation
# S_G	            Snow on the ground at the end of the month (cm)
# Pd	            Number of days with Precipitation 1.0 mm or more
# BS	            Bright Sunshine (hours)
# DwBS	        Days without Valid Bright Sunshine
# BS%	            Percent of Normal (1981-2010) Bright Sunshine
# HDD	            Degree Days below 18 °C
# CDD	            Degree Days above 18 °C
# Stn_No	        Climate station identifier (first 3 digits indicate drainage basin, last 4 characters are for sorting alphabetically).
# NA	            Not Available

#==============================Reading the data in================================
filename='weather-stations20140101-20141231.csv'
#Read csv
pdf = pd.read_csv(filename)
pdf.head(5)

