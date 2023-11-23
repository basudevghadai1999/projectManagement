from django.db import models

# Create your models here.

class usermanager(models.Model):
  name = models.CharField(max_length=200)
  emp_id = models.CharField(max_length=200)
  emp_role = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

# {
#   "name":"user1",
#   "emp_id":"1234",
#   "emp_role":"Manager",
#   "password":"abc123",
#   "completed":False
# }