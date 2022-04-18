from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField()
    link = models.URLField()
    publisher = models.CharField(max_length=100)
    uid = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.title} written by {self.publisher} on {self.pub_date}"

