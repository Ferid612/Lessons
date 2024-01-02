# pip install pandas
import pandas as pd

#! Exmple 1 
# import pandas

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pandas.DataFrame(mydataset)

# print(myvar)



#! Version 
# print(pd.__version__)



#! Pandas series || One dimensional array
# a = [1, 7, 2]

# myvar = pd.Series(a)

# print(myvar) 


#! Specific indexing
# myvar = pd.Series(a, index = ["x", "y", "z"])


#! Dict to series 

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)



#! Dataframs || Multi dimensional array 
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data)

# # print(myvar)

#! Indexing vs loc
# print(df["calories"])
# print(df["calories"][0])


#! refer to the row index:
# print(df.loc[0])


#! Multi index in loc
# print(df.loc[[0,1]])

#! Example loc
# df.loc[0:4, ['Name', 'Age', 'State']]

#! Dataframe with index

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df) 


#! Indexing with Loc 
#refer to the named index:
# print(df.loc["day2"])


#! CSV 
# Reading csv

df = pd.read_csv('Codes/Lesson Subjects/data.csv')

# print(df.to_string()) 

# pd.options.display.max_rows = 100
# pd.set_option('display.max_rows', x)


# pd.options.display.min_rows = 100
# print(df) 

#! get.options to return the current value
# pd.get_option("display.max_rows")


#! Read json
# df = pd.read_json('Codes/Lesson Subjects/data.json')
# print(df.to_string()) 

#! Dict as json
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)

# print(df) 


#! Analyzing
#! Top 5 rows
# print(df.head()
# print(df.head(10))

#! Last 5 rows
# print(df.tail())
# print(df.tail(10))


#! Print information about the data:
# df.info()


#! Data cleaning
# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

#! Cleaning null data
# new_df = df.dropna()
# print(new_df.to_string())

#! inplace True
# df.dropna(inplace = True)

#! Replace Empty Values
# df.fillna(130, inplace = True)


#! Replace Only For Specified Columns
# df["Calories"].fillna(130, inplace = True)


#! Replace Using Mean, Median, or Mode
# x = df["Calories"].mean()
# x = df["Calories"].median()
# x = df["Calories"].mode()[0]

# df["Calories"].fillna(x, inplace = True)



#! Pandas - Cleaning Data of Wrong Format

# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())


#! Removing wrong format Rows
# df.dropna(subset=['Date'], inplace = True)


#! Replacing values 
# df.loc[7, 'Duration'] = 45

#! Example replacing wrong data
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120

#! Removing wrong data
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)


#! Duplicates
# print(df.duplicated())


# Remove all duplicates:
# df.drop_duplicates(inplace = True)


#! Dataframe size
# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
# print(df.size)


#! Shape
# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4],'col3': [5, 6]})
# print(df.shape)



#! Append 

# data1 = {
#   "age": [16, 14, 10],
#   "qualified": [True, True, True]
# }
# df1 = pd.DataFrame(data1)

# data2 = {
#   "age": [55, 40],
#   "qualified": [True, False]
# }
# df2 = pd.DataFrame(data2)

# newdf = df1.append(df2)



#! Add is not equal to append
# data = {
#   "points": [100, 120, 114,116],
#   "total": [350, 340, 402,404]
# }

# df = pd.DataFrame(data)

# print(df.add(15))


#! For data analyse
# print(df)
# print(df.describe())

# count: Hər sütundakı non-null (boş olmayan) dəyərlərin sayı.
# mean: Hər sütundakı sayısal dəyərlərin ortalaması.
# std: Hər sütundakı dəyərlərin standart sapması.
# min: Hər sütundakı ən küçük dəyər.
# 25%: Verilerin alt çeyreği (alt %25'lik dilimdeki dəyər).
# 50% (veya median): Hər sütundakı medyan dəyəri (orta dəyər).
# 75%: Verilerin üst çeyreği (üst %25'lik dilimdeki dəyər).
# max: Hər sütundakı ən büyük dəyər.


#! Value counts
# df['points'].value_counts()


#! data_1.groupby(by='State').Salary.mean()


#! data_1.merge(data_2, on='Name', how='left')

#! data_1.sort_values(by='Name', inplace=True)
