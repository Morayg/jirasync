from __future__ import print_function
from classes.DocsData import DocsData
from classes.RedmineIssie import RedmineIssie
from pprint import pprint


def main():
    config = {
    'scopes': ['https://www.googleapis.com/auth/spreadsheets.readonly'], 
    'sample_spreadsheet_id': '1_CjOSN8RnE3yW0Ta--TaZtIVB4jZzY1wQuojNJhZ3w4',
    'sample_range_name': 'публикация 29.10 !C3:H'
    }
    
    # docsData = DocsData(config).listIssueNumberWithoutRedmineLink()
    # pprint(docsData)

    response = RedmineIssie().get(23541)
    # response = RedmineIssie().create("Тестовый таск", "Описание")
    pprint(response)

if __name__ == '__main__':
    main()