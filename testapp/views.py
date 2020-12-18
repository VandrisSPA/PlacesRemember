from django.shortcuts import render
from .models import MyModel
# Create your views here.


def index(request):
    data = MyModel.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)
