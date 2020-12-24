from django.contrib.gis import forms as geoforms
from django import forms
from .models import MyModel


class MyModelForm(geoforms.Form, forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['feelings', 'name', 'location']
        attrs = {
            'default_lon': 92.9,
            'default_lat': 56.05,
            'default_zoom': 12,
            # 'map_width': 700,
            # 'map_height': 450,
        }
        widgets = {'location': geoforms.OSMWidget(attrs=attrs)}
