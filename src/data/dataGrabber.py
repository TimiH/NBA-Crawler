import pandas as pd
import requests
import time

#helperfunctions
#----------------------

#gets all tables from basketball-reference.com for a certain year and team 
def getTeamYear(team, year):
    print("debug12")
    print(team,year)

    link = 'https://www.basketball-reference.com/teams/' + str(team) + '/' + str(year) + '/gamelog/#sum:tgl_basic'
    request = requests.get(link)
    filename = 'C:\cygwin64\home\Tim\pythonstuff\cookiecutter-data-science\Predict_NBA\data\raw' + str(team) +str(year) + '.csv'
    if request.status_code == 200:
        sauce = pd.read_html(link, header = 0)
        for df in sauce:
            df.to_csv(filename , encoding='utf-8', index=False)
            return;
    else:
        print('Web page error')
        print(link)
    return;

#getTeamnames that are relevant during that year
def getAll():
    teams = pd.read_csv('teamNamesPerYear.csv',index_col=0)
    print("debug1")
    
    for index, row in teams.iterrows():
            getTeamYear(str(index),str(row))
            #print(row, index)
            time.sleep(1)
    
    return;
    

    
    
#script
teams = pd.read_csv('teamNamesPerYear.csv',index_col=0)

#getTeamYear(ATL,1980)

C:\cygwin64\home\Tim\pythonstuff\cookiecutter-data-science\Predict_NBA\data\raw