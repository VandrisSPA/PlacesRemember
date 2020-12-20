from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MyModel
from .forms import MyModelForm
# Create your views here.


def login(request):
    return render(request, 'login.html')


@login_required
def index(request):
    data = MyModel.objects.all().filter(author=request.user)
    context = {'data': data}
    return render(request, 'index.html', context)


@login_required
def index1(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        form.instance.author = request.user

        if form.is_valid():
            form.save()
            context = {'data': MyModel.objects.all()}
            return render(request, 'index.html', context)
    else:
        form = MyModelForm()

    return render(request, 'add_form.html', {'form': form})
