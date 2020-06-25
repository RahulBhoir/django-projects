from django.db import models

# Create your models here.


class TodoItems(models.Model):
    content = models.TextField(max_length=255)
    content_date = models.DateField(auto_now='True')
