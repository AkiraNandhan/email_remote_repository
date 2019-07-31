from django.db import models

class SignUpData(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email_id=models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)



