from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dateTime',]