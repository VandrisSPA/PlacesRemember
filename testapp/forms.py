from django import forms


class MyModelForm(forms.Form):
    field1 = forms.CharField(label='Field1', max_length=100)
    field2 = forms.CharField(label='Field2', max_length=100)
