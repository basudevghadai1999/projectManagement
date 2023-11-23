from django.db import models

# Create your models here.

class Project(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  startdate = models.DateField(max_length=20)
  enddate = models.DateField(max_length=20)
  projectmanager_id = models.IntegerField()
  
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.name


# {
#   "name":"Data extraction",
#   "description":"some value need to be extracted",
#   "startdate":"21/11/2023",
#   "enddate":"30/12/2023",
#   "projectmanager_id":1234
# }
