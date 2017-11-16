import pandas as pd

path = "C:\cygwin64\home\Tim\pythonstuff\cookiecutter-data-science\Predict_NBA\data\interim"
final = "C:\cygwin64\home\Tim\pythonstuff\cookiecutter-data-science\Predict_NBA\data\processed\\final.csv"
df = pd.read_csv(path + "\duplicates.csv", header = 0)

#dropping emptysperator tab
df = df.drop(['G', 'Unnamed: 24'], axis=1)

#replacing Away
df['Away'] = df['Away'].replace('@', '1')
df['Away'] = df['Away'].fillna(0)

#Replacing WinLoss 0 == Team1 won, 1== Team2 won
df['Result'] = df['Result'].replace('L',1)
df['Result'] = df['Result'].replace('W',0)

#Renaming column for Team 2
df.columns = ['Date', 'Away', 'Team 1', 'Team 2', 'Result', 'Score 1', 'Score 2', 'FG', 'FGA',
       'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'TRB', 'AST',
       'STL', 'BLK', 'TOV', 'PF', 'FG_O', 'FGA_O', 'FG%_O', '3P_O', '3PA_O',
       '3P%_O', 'FT_O', 'FTA_O', 'FT%_O', 'ORB_O', 'TRB_O', 'AST_O', 'STL_O',
       'BLK_O', 'TOV_O', 'PF_O']

#Creating Big4 Factors
#Effective Field Goal Percentage=(Field Goals Made) + 0.5*3P Field Goals Made))/(Field Goal Attempts)
#Turnover Rate=Turnovers/(Field Goal Attempts + 0.44*Free Throw Attempts + Turnovers)
#Offensive Rebounding Percentage = (Offensive Rebounds)/[(Offensive Rebounds)+(Opponent’s Defensive Rebounds)]
#Free Throw Rate=(Free Throws Made)/(Field Goals Attempted) or Free Throws Attempted/Field Goals Attempted

#Team1
df['EFFFG_R'] = (df['FG'] + 0.5 *df['3P'])/df['FGA']
df['TOV_R'] = df['TOV'] / (df['FGA'] + 0.44 * df['FTA'] + df['TOV'])
df['ORB_R'] = df['ORB'] / ( df['ORB'] + df['ORB_O'])
df['FT_R'] = df['FT'] / (df['FTA'])
#Team2
df['EFFFG_R_O'] = (df['FG_O'] + 0.5 *df['3P_O'])/df['FGA_O']
df['TOV_R_O'] = df['TOV_O'] / (df['FGA_O'] + 0.44 * df['FTA_O'] + df['TOV_O'])
df['ORB_R_O'] = df['ORB_O'] / (df['ORB_O'] + df['ORB'])
df['FT_R_O'] = df['FT_O'] / (df['FTA_O'])

#saving
df.to_csv(final, encoding='utf-8', index=False)
