from redminelib import Redmine

class RedmineIssue(object):
    def __init__(self, login, password):
        self.redmine = Redmine('https://task.finch.fm', username=login, password=password)

    def get(self, id: int):
        return self.redmine.issue.get(id)

    def create(self, issueName: str, issueDescription: str, version: int):
        result = self.redmine.issue.create(project_id='premier-main', subject=issueName, description=issueDescription, fixed_version_id=version)
        return result

    def createSubTasks(self, issueName: str, parentId: int, listSubProjects: list):
        result = []
        for project in listSubProjects:
            result.append(self.redmine.issue.create(project_id=project, subject=issueName, parent_issue_id=parentId))
        return(result)

class RedmineVersion(object):
    def __init__(self, login, password):
       self.redmine = Redmine('https://task.finch.fm', username=login, password=password) 

    def check(self, project_id: str, name: str):
        versions = self.redmine.version.filter(project_id=project_id)
        for version in versions:
            print(version.name)
            if version.name == name:
                return version.id

    def create(self,project_id: str, name: str):
        result = self.redmine.version.create(project_id=project_id, name=name, sharing='descendants')
        return result