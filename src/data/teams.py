import pandas as pd

#reading file and transposing
df = pd.read_csv('NBA Teamz.csv')
df = df.T
df

#creating final dataframe that will be exported as an object
final = []

#Initialising variable to count while
x=1
while x!=38: #start at 1 and do all years
    y = []   #array for teams
    for p in range(0,40):  #test for all p in teams for year x
        if df.iloc[x, p] == 1:
            y.append(str(df.iloc[0,p])) #add string
    final.append(y) #add to final frame
    x=x+1

output = pd.DataFrame(final, index=df.index, columns=df.columns, dtype=None, copy=False)
output.pd.to_csv(teamsclean.csv, encoding='utf-8', index=False)
