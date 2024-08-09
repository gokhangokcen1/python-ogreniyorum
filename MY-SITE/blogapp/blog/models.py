from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False,blank=True, unique=True, db_index=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "blogs")
    description = RichTextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE) 
    #null=True, on_delete=SET_NULL bir kategori silindiğinde blog da silinmesin istersek böyle yapmamız gerekir.
    # ya da default=1, on_delete=model.SET_DEFAULT default bir kategoriye ata
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

