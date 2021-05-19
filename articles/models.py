from django.db import models

#Create you models here

class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default="default.jpg",blank=True)
    # author=
    



    def __str__(self):
        return(self.title)
    

    def snippet(self):
        return self.body[:50]+"........."

class Sample(models.Model):
    data=models.CharField(max_length=100)
# remenber to makemigrations (python manage.py makemigrations)
# remember to migrate (python manage.py migrate)

