import uuid

from django.db import models
from django.db.models import TextField


# Create your models here.

class Offer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)
    name = models.CharField(max_length=100)
    beds_count = models.IntegerField(null=False)
    baths_count = models.IntegerField(null=False)
    area = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    image = models.ImageField(upload_to='img')
    description = models.TextField(max_length=500)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/properties/{self.slug}'

    class Meta:
        db_table = 'property_offers'