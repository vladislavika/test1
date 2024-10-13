from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.login
