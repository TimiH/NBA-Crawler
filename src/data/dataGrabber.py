import pandas as pd
import requests
import os.path

#helperfunctions
#----------------------
#https://www.basketball-reference.com/teams/ATL/1992/gamelog/#sum:tgl_basic

#gets all tables from basketball-reference.com for a certain year and team 
def getTeamYear(team, year):
    print(team,year)

    link = 'https://www.basketball-reference.com/teams/' + str(team) + '/' + str(year) + '/gamelog/#sum:tgl_basic'
    print(link)
    request = requests.get(link)
    filename = 'C:\\cygwin64\\home\\Tim\\pythonstuff\\cookiecutter-data-science\\Predict_NBA\\data\\raw\\' + str(team) +str(year) + '.csv'
    
    if os.path.isfile(filename) == 0:    
        if request.status_code == 200:
            try: 
                sauce = pd.read_html(link, header = 0)
                for df in sauce:
                    df.to_csv(filename, encoding='utf-8', index=False)
                    return;
            
            except ValueError:
                print("No tables at:",link)
        else:
            print('Web page error')
            print(link)
        return;

#getTeamnames that are relevant during that year
def getAll():
    teams = pd.read_csv('teamNamesPerYear.csv',index_col=0).T
    
    for row in teams.iterrows():
        year = str(row[0])
        series = row[1]
        for team in series:
            if pd.isnull(team) == 0 :   
                getTeamYear(team,year)
    return;
    

    
    
#script 
getAll()


    