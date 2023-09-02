from django.db import models
from user.models import Etudiant, Enseignant
    

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='course_videos/')

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='course_files/')

    def __str__(self):
        return self.title
    
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    student = models.ManyToManyField(Etudiant)
    thumbnail = models.ImageField(upload_to='course_thumbnails/')
    video = models.ManyToManyField(Video)
    file = models.ManyToManyField(File)
    
    def __str__(self):
        return self.title