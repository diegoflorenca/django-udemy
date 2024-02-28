from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # ImageField requires an extra package
    # python3 -m pip install Pillow
    image = models.ImageField(upload_to="images")
