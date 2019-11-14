import pandas as pd 

# Examples on how dataframes can be initialized.
# There are many other ways but this a good start,
# for more ways to make new dataframes you can checkout:
# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
data = [['tom', 10], ['nick', 15], ['juli', 14]]
example = pd.DataFrame(data, columns = ['Name','Age'])
data2 = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
example2 = pd.DataFrame(data2)

df = pd.read_csv("example.csv", index_col="Name")
df.loc["Elizabeth Slade"]
df.loc["Elizabeth Slade"]["Email"]


H4IMembers = pd.read_csv("example.csv")

# get all the column names
VarNames = list(H4IMembers)
VarNames2= list(H4IMembers.columns.values)

#Using conditionals to get certain entries
AgriWorksTeam = H4IMembers["Project"] == "Agriworks"
H4IMembers[AgriWorksTeam]

GradYear = H4IMembers["Class"] == 2022
AgriworkSoph= H4IMembers[AgriWorksTeam & GradYear]

CSmajors= H4IMembers[H4IMembers["Major"].isin(["CS"])]

#getting a particular entry

# Pulling out just one column
NameList = list(H4IMembers["Name"])

#adding new entries
newentries = {'Name': ["Tom", "Dick", "Harry"], 
'Email': ["Tom@bu.edu", "MobyDick@bu.edu", "HarryStyles@bu.edu"], 
'Class': [2020, 2021, 2025],
"Major": ["Questrom Snake", "Comm", "Performing Arts"], 
"Position": ["SE", "gen-mem", "Tech Lead"],
"Project" : ["Red-Cross", "CenteredApp", "Caties Closet"]
}

# Appending/adding new entries to a dataframe
NewMembers = pd.DataFrame(newentries)
H4IPlus = H4IMembers.append(newentries, ignore_index = True)
H4IPlus.drop([48,49,50])

# Adding new columns/Removing columns
Home = ["Seattle", "Shanghai", "India"]
NewMembers = NewMembers.assign(HomeCity = Home)
NewMembers = NewMembers.drop(columns = ["HomeCity"])

#mergingDataframes

newentries2 = {'Name': ["Tom", "Harry" ], "cool" : [True, False]}
coolness = pd.DataFrame(newentries2)
NewMembers.merge(coolness, how ='left'
