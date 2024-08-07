from django.contrib import admin
from .models import Blog, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ("title", "is_active","is_home","slug",)
    list_editable = ("is_active", "is_home",)
    search_fields = ("title", "description",)
    readonly_fields = ("slug",)
=======
    list_display = ("title", "is_active","is_home",)
    list_editable = ("is_active", "is_home",)
    search_fields = ("title", "description",)
    # readonly_fields = ("description",)
>>>>>>> 0c3b106d28164c73b2d76ee04e21d0756c93713f

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)