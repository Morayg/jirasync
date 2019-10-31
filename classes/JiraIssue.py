from jira import JIRA

class JiraIssue(object):
    def __init__(self, auth):
        options = {'server': 'https://jira.zxz.su'}
        self.jira = JIRA(options, auth=auth)
    
    def getIssue(self, id: str):
        issue = self.jira.issue(id)
        return {'id': issue.key, 'name': issue.fields.summary ,'description':issue.fields.description}