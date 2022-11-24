import pandas as pd

def examplo1():
    lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']

    df = pd.DataFrame(lst)
    print(df)

def examplo2():
    data = {'Name':['Amor', 'Jesus', 'Maria', 'José'],
        'Age':[20, 32, 43, 54]}

    df = pd.DataFrame(data)
    print(df)
    
def examplo3():
    data = {'Name':['Amor', 'Jesus', 'Maria', 'José'],
        'Age':[20, 32, 43, 54]}
    df = pd.DataFrame(data)
    print(df[['Name']])
    print(df[['Age']])
    print(df[['Age', 'Name']])
     
    
def exemplo4(): 
    path = "./pandas/data_frame/nba.csv"
    data = pd.read_csv(path, index_col="Name")

    first = data.loc["Avery Bradley"]
    second = data.loc["R.J. Hunter"]
    
    print(first, "\n\n\n", second)
    
def exemplo5():
    path = "./pandas/data_frame/nba.csv"
    data = pd.read_csv(path, index_col="Name")

    first = data["Age"]
    
    print(first) 
    
def exemplo6():
    
    data = pd.read_csv("./pandas/data_frame/nba.csv", index_col="Name")
    row2 = data.iloc[3]
    print(row2)

exemplo6()
