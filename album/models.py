from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to ='album/')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    
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