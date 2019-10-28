from redminelib import Redmine

class RedmineIssue(object):
    def __init__(self):
        self.redmine = Redmine('https://task.finch.fm', username='ik ', password='A1s2d3f4')

    def get(self, id: int):
        return self.redmine.issue.get(id)

    def create(self, issueName: str, issueDescription: str):
        result = self.redmine.issue.create(project_id='premier-main', subject=issueName, description=issueDescription)
        return result

    def createSubTasks(self, issueName: str, parentId: int, listSubProjects: list):
        result = []
        for project in listSubProjects:
            result.append(self.redmine.issue.create(project_id=project, subject=issueName, parent_issue_id=parentId))
        return(result)
