from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
