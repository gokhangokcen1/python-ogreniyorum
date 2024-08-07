from django.db import models
from django.utils.text import slugify

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    name = models.CharField(max_length=150)
<<<<<<< HEAD
    slug = models.SlugField(null=False,blank=True, unique=True, db_index=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
=======
>>>>>>> 0c3b106d28164c73b2d76ee04e21d0756c93713f
    
    def __str__(self):
        return self.name