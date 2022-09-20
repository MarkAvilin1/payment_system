from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField()
    price = models.SmallIntegerField()
    quantity = models.SmallIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def get_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name
