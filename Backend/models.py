from django.db import models

# Create your models here.

class Genredb(models.Model):
    Genre_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
class songdb(models.Model):
    Song_name=models.CharField(max_length=50,null=True,blank=True)
    Artist_name=models.CharField(max_length=50,null=True,blank=True)
    Genre=models.CharField(max_length=50,null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
    Song_Image=models.ImageField(upload_to="song_Images",null=True,blank=True)
    Song=models.FileField(upload_to="songs",null=True,blank=True)

class Eventdb(models.Model):
    Event_name=models.CharField(max_length=100,null=True,blank=True)
    Venue_hall=models.CharField(max_length=50,null=True,blank=True)
    Venue_address=models.CharField(max_length=300,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Event_Image=models.ImageField(upload_to="event_images",null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
    Date=models.DateField(null=True, blank=True)
    Time=models.CharField(max_length=50,null=True,blank=True)
    Performer1=models.CharField(max_length=100,null=True,blank=True)
    Performer2=models.CharField(max_length=100,null=True,blank=True)
    Performer3=models.CharField(max_length=100,null=True,blank=True)
    Performer4=models.CharField(max_length=100,null=True,blank=True)
    Performer1Image=models.ImageField(upload_to="Performer1image",null=True,blank=True)
    Performer2Image=models.ImageField(upload_to="Performer1image",null=True,blank=True)
    Performer3Image=models.ImageField(upload_to="Performer1image",null=True,blank=True)
    Performer4Image=models.ImageField(upload_to="Performer1image",null=True,blank=True)
    Performer1role=models.CharField(max_length=100,null=True,blank=True)
    Performer2role=models.CharField(max_length=100,null=True,blank=True)
    Performer3role=models.CharField(max_length=100,null=True,blank=True)
    Performer4role=models.CharField(max_length=100,null=True,blank=True)

