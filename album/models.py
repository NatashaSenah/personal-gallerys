from django.db import models
# import datetime as dt

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length =30,null=True)
    

    def __str__(self):
        return self.location_name



class Category(models.Model):
    category_name = models.CharField(max_length =30,null=True)
    
    def __str__(self):
        return self.category_name

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    # pub_date = models.DateTimeField(auto_now_add=True,null=True)
    image_image = models.ImageField(upload_to = 'image/')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    @classmethod
    def home(cls,date):
        album = cls.objects.all()
        return album
    @classmethod
    def search_by_image_name(cls,search_term):
        album = cls.objects.filter(image_name__icontains=search_term)
        return album
    def __str__(self):
        return self.image_name
    
