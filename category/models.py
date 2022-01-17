from enum import unique
from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=90)
    description = models.CharField(max_length=255)
    cat_image = models.ImageField(upload_to='photos/categories',blank=True)





    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    def __str__(self) :
        return self.category_name

    def get_url(self):
        return reverse ('product_by_category',args=[self.slug])