from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    rfid_tag = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    original_quantity = models.IntegerField(default=0)  # Set a default value, such as 0
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
