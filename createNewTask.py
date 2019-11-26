from __future__ import print_function
from classes.DocsData import DocsData
from classes.Redmine import RedmineIssue
from classes.Redmine import RedmineVersion
from classes.Jira import JiraIssue
from pprint import pprint
import json


def main():
    version = 'публикация 08.11 '
    with open('auth.json', 'r') as f:
        distros_dict = json.load(f)
    auth = (distros_dict['jira']['login'], distros_dict['jira']['password'])
    redauth = {'login': distros_dict['redmine']['login'], 'password': distros_dict['redmine']['password']}
    config = {
    'scopes': ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'], 
    'sample_spreadsheet_id': '1_CjOSN8RnE3yW0Ta--TaZtIVB4jZzY1wQuojNJhZ3w4',
    'sample_range_name': version + '!C3:H'
    }
    listProjects = [
        'preimer-ndroid',
        'premier-androidtv',
        'premier-appletv',
        'premier-ios'
    ]
    
    result = []
    docs = DocsData(config)
    jiraissue = JiraIssue(auth)
    redmineIssue = RedmineIssue(redauth['login'], redauth['password'])
    redmineVersion = RedmineVersion(redauth['login'], redauth['password'])

    for issue in docs.listIssueNumberWithoutRedmineLink():
        result.append({**jiraissue.getIssue(issue), **docs.getIssueByJiraId(issue)})
    
    for issue in result:
        if redmineVersion.check('premier-main', version) == None:
            versionId = redmineVersion.create('premier-main', version)
        else:
            versionId = redmineVersion.check('premier-main', version)

        response = redmineIssue.create(issue['docsDescription'], issue['name'] + ': \n' + issue['description'], versionId)
        redmineIssue.createSubTasks(issue['name'], response.id, listProjects)
        result = docs.addRmLinkByJiraId(issue['id'], response.url, version)


if __name__ == '__main__':
    main()
