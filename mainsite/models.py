from django.db import models

class Project(models.Model):
    title = models.CharField()
    summary = models.CharField()
    active = models.BooleanField()
    slug = models.CharField()
    
    
class ProjectGoals(models.Model):
    project = models.ForeignKey(Project)
    item = models.CharField()
    

class ProjectContent(models.Model):
    project = models.ForeignKey(Project)
    content = models.CharField()
    
    