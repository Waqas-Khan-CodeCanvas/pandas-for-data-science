import pandas as pd

# load the dataset
# df = pd.read_json("students.json")
df = pd.read_csv("students.csv")

# head() , tail()  show 5 row by default

print("display 10 rows first")
print(df.head(10))

print("display 10 rows last")
print(df.tail(10))


# print("displaying info of data set")
# print(df.info())


# Discribe methods in pandas
data = {
    "name":["waqas khan","shayan hassan " , "zaryab khan","hesham zaman", "umair khattak"],
    "age":[21,20 , 18,22,25],
    "city":["mardan","sawabi " , "peshawar", "swat" , "karak"]
}

df = pd.DataFrame(data)
print(df)

print("discriptive statistic about data set")
print(df.describe)


"""
    1 :- how big is your dataset
    2 :- what are the names of colums

    shape and columns
"""

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj","ali khan"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)
print(f"shape :{df.shape}")
print(f"column names : {df.columns}")


"""
    1 :- select specific column
    2 :- filter rows
    3 :- combine multiple conditions

    1 :- square brackets
    2 :- boolean conditions

    selecting columns 
    1:- a series 
    2:- dataframe multiple columns of data 

    colum = df["column Name "]
    colums = df["column Name ","column Name ",......]

    filtring rows 
    boolean indexing


    selecting rows on a single condition
    filtered_rows = df[df["Salary"] > 50000]

    selecting rows on a multiple condition
    filtered_rows = df[(df["Salary"] > 50000) and (df["Salary"] < 90000)]
"""


data = {
    "Name": ["Ram","Shyam","Ghanshyam","Dhanshyam","Aditi","Jagdish","Raj","ali khan",],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89],
}


# selecting columns
df = pd.DataFrame(data)
print(df)
print(df["Name"])
print(df[["Name","Salary"]])


#  selecting rows
df = pd.DataFrame(data)
print(df[df["Salary"] > 50000])
print(df[(df["Salary"] > 50000) & (df["Age"] > 30)])
print(df[(df["Salary"] > 50000) | (df["Age"] > 30) | (df["Performance Score"] > 90)])
