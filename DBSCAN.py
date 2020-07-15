#=============================IMPORTING REQUIRED LIBRARIES========================
import numpy as np 
from sklearn.cluster import DBSCAN 
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt 
import csv
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap
from pylab import rcParams
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
df_sample = pdf.head(5)
print(df_sample)



#==============================DATA PREPARATION================================

#=============================Cleaning the data==============================
pdf = pdf[pd.notnull(pdf["Tm"])]
pdf = pdf.reset_index(drop=True)
pdf.head(5)


#=============================DATA VIZUALIZATION===============================
rcParams['figure.figsize'] = (14,10)

llon=-140
ulon=-50
llat=40
ulat=65

pdf = pdf[(pdf['Long'] > llon) & (pdf['Long'] < ulon) & (pdf['Lat'] > llat) &(pdf['Lat'] < ulat)]

my_map = Basemap(projection='merc',
            resolution = 'l', area_thresh = 1000.0,
            llcrnrlon=llon, llcrnrlat=llat, #min longitude (llcrnrlon) and latitude (llcrnrlat)
            urcrnrlon=ulon, urcrnrlat=ulat) #max longitude (urcrnrlon) and latitude (urcrnrlat)

my_map.drawcoastlines()
my_map.drawcountries()
# my_map.drawmapboundary()
my_map.fillcontinents(color = 'white', alpha = 0.3)
my_map.shadedrelief()

# To collect data based on stations        
xs,ys = my_map(np.asarray(pdf.Long), np.asarray(pdf.Lat))
pdf['xm']= xs.tolist()
pdf['ym'] =ys.tolist()

#Visualization1
for index,row in pdf.iterrows():
#   x,y = my_map(row.Long, row.Lat)
    my_map.plot(row.xm, row.ym,markerfacecolor =([1,0,0]),  marker='o', markersize= 5, alpha = 0.75)
#plt.text(x,y,stn)
plt.show()


