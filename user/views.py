from django.shortcuts import render
from django.http import HttpResponse
from user.forms import CreateUserForm
# Create your views here.

def register(request):
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(" regiter success")
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {"form":form})

