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
    'sample_range_name': platform + '!A:J'
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
    
    #00. Изменить формат получения данных из таблицы

    #0. проверка наличия тасков в каждой из платформ, относительно жиры

    #1. синхронизация между платформами по названию

    #2. проверка уже существующего таска ???

    #3. Проверка  и Создание новых версий

    #4. создание новых тасков и необходимой декомпозиции (версионирование постановки подзадач)

    #5. обновление тасков внутри версий, обновление спринтов

    #6. Передача статуса по платформе на основе подзадач (в жиру и таблицу)

    #7. общий чек-ин

if __name__ == '__main__':
    main()
