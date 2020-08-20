from django.db import models



class post(models.Model):
    content = models.TextField(blank=True, null=True)
    image =  models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.content
    