from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  status = models.BooleanField(default=False, blank=True, null=True) 
  due_date = models.DateField(max_length=20)
  priority = models.CharField(max_length=200)
  projectAssociation = models.CharField(max_length=200)
      
  def __str__(self):
    return self.title