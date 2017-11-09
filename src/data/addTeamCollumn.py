import pandas as pd
import glob

location = 'C:\\cygwin64\\home\\Tim\\pythonstuff\\cookiecutter-data-science\\Predict_NBA\\data\\raw\\'
newlocation = 'C:\\cygwin64\\home\\Tim\\pythonstuff\\cookiecutter-data-science\\Predict_NBA\\data\\interim\\'

for filename in glob.iglob(location + "*.csv" , recursive=True):
    #getting teamnames from filename
    name = filename.split('\\')[-1]
    teamname = name[0:3]
    year = name[3:7]
    #inserting home Team collumn and saving to /data/interim
    table = pd.read_csv(filename, header = 1)
    table.insert(4,'Home Team',teamname)
    table.to_csv(newlocation + teamname + year + '_int.csv', encoding='utf-8', index=False)
