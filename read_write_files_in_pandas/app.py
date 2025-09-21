import pandas as pd

#  read data from CSV file into a dataframe
# df = pd.read_csv("students.csv",encoding="utf-8")
# df = pd.read_excel("url of excel dataset")
# df = pd.read_json("students.json")
# gcsfs # read data from cloud storage
# print(df)



#  now how to write data to excel file

data = {
    "name":["waqas khan","shayan hassan " , "zaryab khan"],
    "age":[21,20 , 18],
    "city":["mardan","sawabi " , "peshawar"],
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_excel("excelOutput.xlsx")
# df.to_json("jsonOutput.json")