from django.db import models

class Disability(models.Model):
    typeof=models.CharField(max_length=200)
    description=models.CharField(max_length=200,default='hello')
    pic=models.ImageField(upload_to='Disability/',default='blindkid.jpg')
    myurl = models.URLField(max_length = 200, default='mute.html/')
    audio=models.FileField(upload_to='media/',default='mute.mp3')
  
    def __str__(self):
        return self.typeof
        return self.description
        return self.myurl
class Subject(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='InternalPics/',default='blindkid.jpg')
    def __str__(self):
        return self.name