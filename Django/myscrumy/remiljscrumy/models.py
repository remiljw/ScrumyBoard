from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return self.status_name
    class Meta:
        verbose_name_plural = "Goal Status"


class ScrumProject(models.Model):
    name = models.CharField(max_length=50)
    project_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Scrum Project"




class ScrumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)

    
    def __str__(self):
        return self.nickname
    
    class Meta:
        ordering = ['nickname']
        verbose_name_plural = "Scrum User"


class ScrumProjectRole(models.Model):
    role = models.CharField(max_length=50,default=None)
    # roles = models.CharField(max_length=30, default=None)
    user = models.ForeignKey(ScrumUser, on_delete=models.CASCADE)
    project = models.ForeignKey(ScrumProject, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.role
    class Meta:
        ordering = ['project']
        verbose_name_plural = "Scrum Project Role"


class ScrumyGoals(models.Model):
    visible = models.BooleanField(default=True)
    moveable = models.BooleanField(default=True)
    goal_name= models.CharField(max_length=200)
    # goal_id= models.IntegerField()
    # created_by = models.CharField(max_length=200)
    # moved_by = models.CharField(max_length=200)
    # owner = models.CharField(max_length=200)
    goal_project_id = models.IntegerField(default=0)
    project = models.ForeignKey(ScrumProject, on_delete=models.CASCADE)
    user=models.ForeignKey(ScrumProjectRole, on_delete=models.CASCADE)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    # status = models.IntegerField(default=-1)
    

    def __str__(self):
        return self.goal_name

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Scrumy Goals"


class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_from = models.CharField(max_length=200)
    moved_to = models.CharField(max_length=200)
    time_of_action = models.DateTimeField(auto_now=False, auto_now_add=False)
    goal=models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

    
    def __str__(self):
         return self.created_by
    class Meta:
        verbose_name_plural = "Scrumy History"

# class ScrumRole(models.Model):
#     role=models.CharField(max_length=50)


#     def __str__(self):
#         return self.role
#     class Meta:
#         verbose_name_plural = "Scrum Role"