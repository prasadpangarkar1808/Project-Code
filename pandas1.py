import pandas as pd
# s=pd.Series([1,3,5,7,9])
# print(s)

# data={'a':[1,2,3],'b':[4,5,6]}
# df=pd.DataFrame(data)
# print(df)

# a=[1,7,5]
# myvar=pd.Series(a)
# print(myvar[2])

# a=[1,7,5]
# myv=pd.Series(a, index=["x","y","z"])
# print(myv)

# calories={"day1":420,"day2":320,"day3":390}
# myvari=pd.Series(calories)
# print(myvari)

# data={
#     "calories":[420,380,390],
#     "duration":[50,40,45]
# }
# myvar=pd.DataFrame(data)
# print(myvar)

#

#Names Indexes
data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
df=pd.DataFrame(data,index=["day1","day2","day3"])
print(df)

#Locate Named Indexes
    #refer to the named index:
print(df.loc["day2"])

#Reading and Printing CSV Data
    #Readding the CSv file
df.read_csv('data.cvs')
    #Printing the DataFrame
print(df)
    #printing the first 5 rows
print(df.head())
    #priting the last 5 rows
print(df.tail())

df=pd.read_excel('data.xlsx')
print(df)
print(df.head())
print(df.tail())