from django.db import models
from django.db import utils 

from django.template.defaultfilters import slugify #section 7.3

# Create your models here.


class ValidGame(models.Model):
    
    name = models.CharField(max_length = 64)
    short_name = models.CharField(max_length = 64)
    generic_data = models.CharField(max_length = 128, default = "")

    class Meta:
        managed = True
        db_table = "valid_game"
        app_label = "ccapp"
        
    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
        #self.slug = slugify(self.name)
        print("saving valid game")
        #self.slug = slugify(self.name) 
        super(ValidGame, self).save(*args, **kwargs)

class Weapon(models.Model):
    
    name = models.CharField(max_length = 50)
    slug = models.SlugField()
    
    class Meta:
        managed = True
        db_table = 'weapon'
        app_label = "ccapp"
        
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
        #self.slug = slugify(self.name)
        self.slug = slugify(self.name) 
    
