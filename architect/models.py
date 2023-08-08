from django.db import models

# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects')
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.name
