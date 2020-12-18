from django.shortcuts import render
from .models import MyModel
from .forms import MyModelForm
# Create your views here.


def index(request):
    data = MyModel.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)


def index1(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)

        if form.is_valid():
            form.save()
            context = {'data': MyModel.objects.all()}
            return render(request, 'index.html', context)
    else:
        form = MyModelForm()

    return render(request, 'add_form.html', {'form': form})