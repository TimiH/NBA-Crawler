import pandas as pd
import requests
import time

def getTeamYear(team, year):
    "gets all tables from basketball-reference.com for a certain year and team "

    link = 'https://www.basketball-reference.com/teams/' + str(team) + '/' + str(year) + '/gamelog/#sum:tgl_basic'
    request = requests.get(link)
    filename = 'C:\\cygwin64\\home\\Tim\\pythonstuff\\' + str(team) +str(year) + '.csv'
    if request.status_code == 200:
        sauce = pd.read_html(link, header = 0)
        for df in sauce:
            df.drop_duplicates(subset=None,keep='first').to_csv('C:\\cygwin64\\home\\Tim\\pythonstuff\\data\\'+ str(team) +'_'+ str(year) + '.csv' , encoding='utf-8', index=False)
            return;
    else:
        print('Web site does not exist')
    return;



def getAllFromTo(start, end):
    teams = ['ATL','BOS','CHH','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MIA','MIL','MIN','NYK','ORL','PHI','PHO','POR','SAC','SAS','SEA','UTA','WSB']

    for t in teams:
        s = start
        e = end
        while s != e+1:
            try:
                getTeamYear(team = t,year = s)
            except Exception as e:
                print(e)
            getTeamYear(team = t,year = s)
            s = s+1
            time.sleep(1)
        print("Just done " + str(t))
