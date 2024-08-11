# Generated by Django 5.0.7 on 2024-08-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_blog_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="category",
        ),
        migrations.AddField(
            model_name="blog",
            name="categories",
            field=models.ManyToManyField(to="blog.category"),
        ),
    ]
