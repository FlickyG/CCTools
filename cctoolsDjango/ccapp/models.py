from django.db import models

from django.template.defaultfilters import slugify #section 7.3

# Create your models here.


class Weapon():
    
    name = models.CharField(max_length = 50)
    slug = models.SlugField()
    
    class Meta:
        managed = True
        db_table = 'weapon'
        app_label = "ccap"
        
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
        #self.slug = slugify(self.name)
        self.slug = slugify(self.name) 
    
