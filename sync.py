from __future__ import print_function
from classes.DocsData import DocsData
from classes.Redmine import RedmineIssue
from classes.Redmine import RedmineVersion
from classes.Jira import JiraIssue
import json
from pprint import pprint

def main():
    platform = 'Mobile'
    config = {
    'scopes': ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'], 
    #TODO: заменить на рабочий нейминг
    'sample_spreadsheet_id': '1_CjOSN8RnE3yW0Ta--TaZtIVB4jZzY1wQuojNJhZ3w4',
    'sample_range_name': platform + '!A1:J'
    }
    
    #список подпроектов в редмайне
    listProjects = [
        'preimer-ndroid',
        'premier-androidtv',
        'premier-appletv',
        'premier-ios'
    ]

    #задаем данные для авторизации в трекерах
    with open('auth.json', 'r') as f:
        distros_dict = json.load(f)
    auth = (distros_dict['jira']['login'], distros_dict['jira']['password'])
    redauth = {'login': distros_dict['redmine']['login'], 'password': distros_dict['redmine']['password']}

    #инициализация
    result = []
    docs = DocsData(config)
    redmineIssue = RedmineIssue()
    redmineIssue = RedmineIssue(redauth['login'], redauth['password'])
    redmineVersion = RedmineVersion(redauth['login'], redauth['password'])
    
    for issue in docs.get():
        pprint(issue)  

if __name__ == '__main__':
    main()
