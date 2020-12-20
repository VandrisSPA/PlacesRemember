from django.db import models
from django.contrib.gis.db import models as g_models
from django.conf import settings
# Create your models here.


class MyModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.IntegerField(default=-1)
    location = g_models.PointField()

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Model: {self.field1}, {self.field2}, {self.field3}, location: {self.location} created: {self.created}>"
