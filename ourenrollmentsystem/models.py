from django.db import models

class Level(models.Model):
    level_id = models.BigAutoField(primary_key=True, blank=False)
    level = models.CharField(max_length=55, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'level'

class Students(models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False)
    first_name = models.CharField(max_length=55, blank= False)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=False)
    age = models.IntegerField(blank=False)
    birth_date  = models.DateField(blank=False)
    gender = models.CharField(max_length=55,blank=False)
    course = models.CharField(max_length=55,blank=False)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    username = models.CharField(max_length=55, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Students'