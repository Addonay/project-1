from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField()  # You can use this field to store the URL of the car's image.
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
