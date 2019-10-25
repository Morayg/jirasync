import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import re


class DocsData(object):
    def __init__(self, config:dict):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', config.scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=config['sample_spreadsheet_id'],
                                    range=config['sample_range_name']).execute()
        self.values = result.get('values', [])

    def get(self):
        if not self.values:
            return(None)
        else:
            return(self.values)

    def listAllRedmineLink(self):
        if not self.values:
            return(None)
        else:
            listAllRedmineLink = []
            for item in self.values:
                if len(item) >= 6:
                    listAllRedmineLink.append(item[5])
            return(listAllRedmineLink)  

    def listIssueWithoutRedmineLink(self):
        if not self.values:
            return(None)
        else:
            issueWithoutRedmineLink = []
            for item in self.values:
                if len(item) < 6  and len(item) >= 4:
                    issueWithoutRedmineLink.append([item[3],item[2]])
            return(issueWithoutRedmineLink)  

    def __getNumberOnly__(self, values):
        result = []
        for value in values:

            if value[0] != None:
                match = re.search(r'[A-Z]+?-\d+?' , value[0])
                if match != None:
                    result.append(match[0])
        return result

    def listIssueNumberWithoutRedmineLink(self):
        result = self.__getNumberOnly__(self.listIssueWithoutRedmineLink())
        return result