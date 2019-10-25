from __future__ import print_function
from classes.DocsData import DocsData
from classes.RedmineIssue import RedmineIssue
from classes.JiraIssue import JiraIssue
from pprint import pprint


def main():
    config = {
    'scopes': ['https://www.googleapis.com/auth/spreadsheets.readonly'], 
    'sample_spreadsheet_id': '1_CjOSN8RnE3yW0Ta--TaZtIVB4jZzY1wQuojNJhZ3w4',
    'sample_range_name': 'публикация 29.10 !C3:H'
    }
    
    result = []
    docs = DocsData(config)
    jiraissue = JiraIssue()

    for issue in docs.listIssueNumberWithoutRedmineLink():
        result.append({**jiraissue.getIssue(issue), **docs.getIssueByJiraId(issue)})

    pprint(result)

if __name__ == '__main__':
    main()