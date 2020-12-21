from django.db import models
from django.contrib.gis.db import models as g_models
from django.conf import settings
# Create your models here.


class MyModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feelings = models.CharField(max_length=100)
    location = g_models.PointField()

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Model: User: {self.author}, Remember: {self.feelings}, location: {self.location} created: {self.created}>"
