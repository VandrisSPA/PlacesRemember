from django.contrib.gis import forms as geoforms
from django import forms
from .models import MyModel


class MyModelForm(geoforms.Form, forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2', 'field3', 'location']
        widgets = {'location': geoforms.OSMWidget(attrs={'map_width': 800, 'map_height': 500})}
