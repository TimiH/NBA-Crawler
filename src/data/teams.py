import pandas as pd

#reading file that has been compiled by hand
df = pd.read_csv('NBA_teams.csv')

#creating final dataframe that will be exported as an object
current = 1980
final = []

#iterates over all years since 1980
for column in df.columns[1::]:
    y = [current]                               
    for row in range(0,len(df)):
        if df.loc[row, column] == 1:
            y.append(df.loc[row,"Team/Year"])
    current = current +1
    final.append(y)

#cleaning up Dataframe and outputting to csv
output = pd.DataFrame(final).T
output.columns = output.iloc[0]
output = output.drop(0)
output.to_csv('TeamNamesPerYear.csv', encoding='utf-8', index=True)
