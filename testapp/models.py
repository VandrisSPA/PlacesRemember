from django.db import models

# Create your models here.


class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.IntegerField(default=-1)

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Model: {self.field1}, {self.field2}, {self.field3}, created: {self.created}>"
