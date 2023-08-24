import pandas as pd

data = pd.read_csv("C:\\Users\\Administrator\\Desktop\\Coding\\Python\\Data Analytics\\Data Analysis with Python\\Project 1 - Weather Dataset\\WeatherDataset.csv")


#=================Pandas commands============================#
#print(data.shape) #Shows the total number of rows and coloumns of a dataset

#print(data.index) #Shows the index of dataframe

#print(data.columns) #Shows the name of every column

#print(data.dtypes) #Shows data tyoes of columns

#print(data['Weather'].unique()) #Shows the unique values of a specific column

#print(data.nunique()) #Shows the number of unique values of columns

#print(data.count()) #Counts number of normal values (can be applied to specific column or whole dataframe)

#print(data['Weather'].value_counts) #Counts unique values within a specific column

#print(data.info) #Provied basic information about the given dataframe
#============================================================#

# Question 1: Find the unique values of 'Wind Speed' in the dataset

unique_windspeed_values = data['Wind Speed_km/h'].unique()

uniqueWSV_List = [4, 7, 6, 9, 15, 13, 20, 22, 19, 24, 30, 35, 39, 32, 33, 26, 44, 43, 48, 37, 28, 17, 11, 0, 83, 70, 57, 46, 41, 52, 50, 63, 54, 2]

"""
Answer:
[ 4  7  6  9 15 13 20 22 19 24 30 35 39 32 33 26 44 43 48 37 28 17 11 0 83 70 57 46 41 52 50 63 54 2]
34 unique values of Wind Speed in the dataset.
"""

# Question 2: Find the number of times when the weather is exactly "Clear"
valuecounts_weather = data.Weather.value_counts()

"""
Answer:
Clear  1326
"""

# Question 3: Find the number of times when the Wind Speed was exactly 4km/h
valuecounts_windspeed = data[data['Wind Speed_km/h'] == 4]
#print(valuecounts_windspeed)


VC_WindSpeed = data['Wind Speed_km/h'] == 4
#print(VC_WindSpeed)

# Another approach with a for loop
x = 0
for values in data['Wind Speed_km/h']:
    if values == 4:
        x = x + 1
#print(x)


"""
Answer:
4     474
""" 

# Question 4: Find out all the Null Values in the data
null_vals = data.isnull().sum()
# print(null_vals)
"""
Answer:
There are no null values in the data set
"""

# Question 5: Rename the column name 'Weather' to 'Weather Condition'

data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)
#print(data.head(1))

# Question 6: What is the mean of 'Visibility'?
mean_visibility = data.Visibility_km.mean()

"""
Answer:
Mean of Visibility = 27.664446721311478
"""

# Question 7: What is the Standard Deviation of 'Pressure' in this data?
stdv_pressure = data.Press_kPa.std()

"""
Answer:
Standard Deviation of Pressure = 0.8440047459486483
"""

# Question 8: What is the Variance of 'Relative Humidity' in this data?

variance_relativeHumidity = data['Rel Hum_%'].var()

"""
Answer:
Varience of Relative Humidity = 286.24855019850196
"""


# Question 9: Find all instances of when 'Snow' was recorded

snow_value = 0
for values in data['Weather Condition']:
    if values == 'Snow':
        snow_value = snow_value + 1


"""
Answer:
Instances of Snow = 390
"""

# Question 10: Fine all instances when Wind Speed is above 24 and Visibility is 25

y = 0

for index, row in data.iterrows():
        if row['Wind Speed_km/h'] > 24 and row['Visibility_km'] == 25:
            y = y + 1


"""
Answer: 
Instances Wind Speed > 24 & Visibility == 25: 308
"""




# Question 11: What is the Mean value of each column against each 'Weather Condition'?

#weather_condition_means = data.groupby('Weather Condition').mean()



# Question 12: What is the minimum and maximum value of each column against each 'Weather Condition'?

min_val = data.groupby('Weather Condition').min()
max_val = data.groupby('Weather Condition').max()
"""
                                            Date/Time  Temp_C  Dew Point Temp_C  Rel Hum_%  Wind Speed_km/h  Visibility_km  Press_kPa
Weather Condition
Clear                                      1/11/2012 1:00   -23.3             -28.5         20                0           11.3      99.52
Cloudy                                     1/1/2012 17:00   -21.4             -26.8         18                0           11.3      98.39
Drizzle                                   1/23/2012 21:00     1.1              -0.2         74                0            6.4      97.84
Drizzle,Fog                               1/23/2012 20:00     0.0              -1.6         85                0            1.0      98.65
Drizzle,Ice Pellets,Fog                   12/17/2012 9:00     0.4              -0.7         92               20            4.0     100.79
Drizzle,Snow                             12/17/2012 15:00     0.9               0.1         92                9            9.7     100.63
Drizzle,Snow,Fog                         12/18/2012 21:00     0.3              -0.1         92                7            2.4      97.79
Fog                                         1/1/2012 0:00   -16.0             -17.2         80                0            0.2      98.31
Freezing Drizzle                          1/13/2012 10:00    -9.0             -12.2         78                6            4.8      98.44
Freezing Drizzle,Fog                        1/1/2012 2:00    -6.4              -9.0         82                6            3.6      98.74
Freezing Drizzle,Haze                      2/1/2012 11:00    -5.8              -8.3         81                9            2.0     100.28
Freezing Drizzle,Snow                      1/13/2012 3:00    -8.3             -10.4         79                6            2.4      99.19
Freezing Fog                               1/22/2012 6:00   -19.0             -22.9         71                0            0.2     101.97
Freezing Rain                             1/13/2012 11:00    -6.5              -9.0         81                7            2.8      98.22
Freezing Rain,Fog                         1/17/2012 23:00    -6.1              -8.7         82                7            2.8      98.32
Freezing Rain,Haze                         2/1/2012 14:00    -4.9              -7.5         82                6            2.0     100.34
Freezing Rain,Ice Pellets,Fog             12/17/2012 3:00    -2.6              -3.7         92               28            8.0     100.95
Freezing Rain,Snow Grains                  1/13/2012 9:00    -5.0              -7.3         84               32            4.8      98.56
Haze                                      1/22/2012 12:00   -11.5             -16.0         68                0            4.8     100.35
Mainly Clear                              1/10/2012 11:00   -22.8             -28.0         20                0           12.9      98.67
Moderate Rain,Fog                         12/10/2012 8:00     1.7               0.8         94               17            6.4      99.98
Moderate Snow                             1/12/2012 15:00    -6.3              -7.6         83               26            0.6      99.88
Moderate Snow,Blowing Snow               12/27/2012 10:00    -5.5              -6.6         92               39            0.6     100.50
Mostly Cloudy                              1/1/2012 16:00   -23.2             -28.5         18                0           11.3      98.36
Rain                                       1/1/2012 18:00     0.3              -5.7         40                0            4.0      97.52
Rain Showers                               1/1/2012 22:00     1.6              -7.2         37                0            6.4      98.51
Rain Showers,Fog                          10/20/2012 3:00    12.8              12.1         96               13            6.4      99.83
Rain Showers,Snow Showers                  11/4/2012 8:00     2.1              -1.8         75               17           19.3     101.09
Rain,Fog                                  1/23/2012 18:00     0.0              -1.2         83                0            2.0      98.61
Rain,Haze                                  3/13/2012 7:00     4.0               1.0         81                7            4.0     100.50
Rain,Ice Pellets                          12/18/2012 5:00     0.6              -0.6         92               24            9.7     100.12
Rain,Snow                                  1/10/2012 5:00     0.6              -1.7         81               13            2.4      98.18
Rain,Snow Grains                          12/21/2012 0:00     1.9              -2.1         75               26           25.0     100.60
Rain,Snow,Fog                             12/8/2012 21:00     0.8               0.3         96                9            6.4     100.73
Rain,Snow,Ice Pellets                     12/21/2012 1:00     0.9              -0.7         88               17            4.8      99.85
Snow                                       1/10/2012 1:00   -16.7             -24.6         41                0            1.0      97.75
Snow Pellets                             11/24/2012 15:00     0.7              -6.4         59               35            2.4      99.70
Snow Showers                               1/12/2012 7:00   -13.3             -19.3         52                0            2.4      99.49
Snow Showers,Fog                          12/26/2012 9:00   -11.3             -12.7         89                7            4.0     100.63
          18.5         93               15            3.2     100.01
Thunderstorms,Rain                        5/25/2012 20:00    19.4              18.2         83                4           16.1     100.19
Thunderstorms,Rain Showers                5/29/2012 16:00    11.0               7.0         68                7            6.4      99.65
Thunderstorms,Rain Showers,Fog             6/29/2012 3:00    19.5              16.1         80                7            9.7      99.71
Thunderstorms,Rain,Fog                     7/17/2012 5:00    20.6              18.6         88               19            4.8     100.08
"""

# Question 13: Show all the records where Weather is fog 

fog_weather = data['Weather Condition'] == 'Fog'
"""
Answer:
0        True
1        True
2       False
3       False
4        True
        ...
8779    False
8780    False
8781    False
8782    False
8783    False
"""

# Question 14: Find all instances when 'Weather is Clear' or Visibility is above 40

z = 0

for index, row in data.iterrows():
        if row['Weather Condition'] == 'Clear' or row['Visibility_km'] > 40:
            z = z + 1

"""
Answer:
Instances = 3027
"""

# Question 15: Find all instances when:
instance = 0

for index, row in data.iterrows():
        if (row['Weather Condition'] == 'Clear' and row['Rel Hum_%'] > 50) or row['Visibility_km'] > 40:
            instance = instance + 1

print(instance)
