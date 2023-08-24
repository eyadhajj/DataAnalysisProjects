import pandas as pd
data = pd.read_csv("C:\\Users\\Administrator\\Desktop\\Coding\\Python\\Data Analytics\\Data Analysis with Python\\Project 2 - Car Data Analysis\\CarsDataset.csv")

"""
Questions in this project are in the form of instructions!
"""

# Q. 1) Instruction ( For Data Cleaning ) - Find all Null Values in the dataset. If there is any null value in any column, then fill it with the mean of that column.

null_values_sum = data.isnull().sum()
# sum of null values is 2 in the 'Cylinders' column

data['Cylinders'].fillna(data['Cylinders'].mean(), inplace = True)
null_values_sum = data.isnull().sum() # Upated null values



# Q. 2) Question ( Based on Value Counts )- Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data ?
types_makes = data['Make'].unique()

"""
The unique types of makes in the data set are:
['Acura' 'Audi' 'BMW' 'Buick' 'Cadillac' 'Chevrolet' 'Chrysler' 'Dodge'
 'Ford' 'GMC' 'Honda' 'Hummer' 'Hyundai' 'Infiniti' 'Isuzu' 'Jaguar'
 'Jeep' 'Kia' 'Land Rover' 'Lexus' 'Lincoln' 'MINI' 'Mazda'
 'Mercedes-Benz' 'Mercury' 'Mitsubishi' 'Nissan' 'Oldsmobile' 'Pontiac'
 'Porsche' 'Saab' 'Saturn' 'Scion' 'Subaru' 'Suzuki' 'Toyota' 'Volkswagen'
 'Volvo']
"""

make_occurance = data['Make'].value_counts()

"""
Answer:
Make
Toyota           28
Chevrolet        27
Mercedes-Benz    26
Ford             23
BMW              20
Audi             19
Honda            17
Nissan           17
Volkswagen       15
Chrysler         15
Dodge            13
Mitsubishi       13
Volvo            12
Jaguar           12
Hyundai          12
Subaru           11
Pontiac          11
Mazda            11
Lexus            11
Kia              11
Buick             9
Mercury           9
Lincoln           9
Saturn            8
Cadillac          8
Suzuki            8
Infiniti          8
GMC               8
Acura             7
Porsche           7
Saab              7
Land Rover        3
Oldsmobile        3
Jeep              3
Scion             2
Isuzu             2
MINI              2
Hummer            1
"""

# Q. 3) Instruction ( Filtering ) - Show all the records where Origin is Asia or Europe.

origin_asia_europe = data[data['Origin'].isin(['Asia', 'Europe'])]

"""
Answer:
      Make                    Model   Type  Origin DriveTrain     MSRP  Invoice  ...  Cylinders  Horsepower  MPG_City  MPG_Highway  Weight  Wheelbase  Length
0    Acura                      MDX    SUV    Asia        All  $36,945  $33,337  ...        6.0         265        17           23    4451        106     189
1    Acura           RSX Type S 2dr  Sedan    Asia      Front  $23,820  $21,761  ...        4.0         200        24           31    2778        101     172
2    Acura                  TSX 4dr  Sedan    Asia      Front  $26,990  $24,647  ...        4.0         200        22           29    3230        105     183
3    Acura                   TL 4dr  Sedan    Asia      Front  $33,195  $30,299  ...        6.0         270        20           28    3575        108     186
4    Acura               3.5 RL 4dr  Sedan    Asia      Front  $43,755  $39,014  ...        6.0         225        18           24    3880        115     197
..     ...                      ...    ...     ...        ...      ...      ...  ...        ...         ...       ...          ...     ...        ...     ...
423  Volvo  C70 LPT convertible 2dr  Sedan  Europe      Front  $40,565  $38,203  ...        5.0         197        21           28    3450        105     186
424  Volvo  C70 HPT convertible 2dr  Sedan  Europe      Front  $42,565  $40,083  ...        5.0         242        20           26    3450        105     186
425  Volvo               S80 T6 4dr  Sedan  Europe      Front  $45,210  $42,573  ...        6.0         268        19           26    3653        110     190
426  Volvo                      V40  Wagon  Europe      Front  $26,135  $24,641  ...        4.0         170        22           29    2822        101     180
427  Volvo                     XC70  Wagon  Europe        All  $35,145  $33,112  ...        5.0         208        20           27    3823        109     186
"""



# Q. 4) Instruction ( Removing unwanted records ) - Remove all the records (rows) where Weight is above 4000.

unwanted_car_weight = data[--data['Weight'] > 4000]



# Q. 5) Instruction ( Applying function on a column ) - Increase all the values of 'MPG_City' column by 3.

data['MPG_City'] = data['MPG_City'] + 3

print(data.head(2))