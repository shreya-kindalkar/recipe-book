from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("Dinner", "Dinner"),
        ("Snacks", "Snacks"),
        ("Desserts", "Desserts"),
        ("Healthy", "Healthy"),
        ("Beverages", "Beverages"),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    ingredients=models.TextField()
    instructions=models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image=models.ImageField(upload_to='recipes/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title