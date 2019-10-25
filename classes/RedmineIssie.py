from redminelib import Redmine

class RedmineIssie(object):
    def __init__(self):
        self.redmine = Redmine('https://task.finch.fm', username='ik ', password='A1s2d3f4')

    def get(self, id: int):
        return self.redmine.issue.get(id)

    def create(self, issueName: str, issueDescription: str):
        result = self.redmine.issue.create(project_id='premier-main', subject=issueName, description=issueDescription)
        return result
