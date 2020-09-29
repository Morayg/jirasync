from jira import JIRA
server = 'https://jira.zxz.su'
def jira (self, server, auth):
    self.jira = JIRA({'server': server}, auth=auth)

class JiraIssue(object):
    def __init__(self, auth):
        self.jira = JIRA({'server': server}, auth=auth)
    
    def getIssue(self, id: str):
        issue = self.jira.issue(id)
        return {'id': issue.key, 'name': issue.fields.summary ,'description':issue.fields.description}

class JiraList(object):
    def __init__(self, auth):
        self.jira (self, server, auth)
        