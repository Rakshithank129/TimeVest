from django.db import models

# Create your models here
class tasks(models.Model):
    task_id = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100)
    Assigned_by = models.CharField(max_length=100)
    Assigned_to = models.CharField(max_length=100)
    Review = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    