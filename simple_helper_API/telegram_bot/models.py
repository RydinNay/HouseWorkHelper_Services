from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField("Id", primary_key=True)
    name = models.CharField(max_length=30)
    telephone_number = models.CharField(max_length=15, unique=True, )
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name, self.telephone_number, self.city}"