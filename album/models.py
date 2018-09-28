from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    image_image = models.ImageField(upload_to = 'image/')
    @classmethod
    def album(cls):
        today = dt.date.today()
        album = cls.objects.filter(pub_date__date = today)
        return album

    @classmethod
    def past(cls,date):
        album = cls.objects.filter(pub_date__date = date)
        return album


    @classmethod
    def home(cls,date):
        album = cls.objects.all()
        return album
    @classmethod
    def search_by_image_name(cls,search_term):
        album = cls.objects.filter(image_name__icontains=search_term)
        return album
    
class Location(models.Model):
    location_name = models.CharField(max_length =30,null=True)
    image_location = models.ForeignKey(Image)

    def __str__(self):
        return self.name



class Category(models.Model):
    category_name = models.CharField(max_length =30,null=True)
    image_category = models.ForeignKey(Image)
    def __str__(self):
        return self.name