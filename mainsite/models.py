from django.db import models

class Project(models.Model):
    title = models.CharField(max_length="100")
    summary = models.TextField()
    active = models.BooleanField()
    slug = models.CharField(max_length="20")
    
    
class ProjectGoals(models.Model):
    project = models.ForeignKey(Project)
    item = models.CharField(max_length="100")
    

class ProjectContent(models.Model):
    project = models.ForeignKey(Project)
    content = models.TextField()
    
    