from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # The FileField will not be stored on the database. Files must be save on the hard drive.
    image = models.FileField(upload_to="images")
