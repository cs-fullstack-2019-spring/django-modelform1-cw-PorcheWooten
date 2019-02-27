from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewBlog


# Create your views here.
# check validation and saves data , sends form to index
def index(request):
    newForm = NewBlog()

    if request.method == "POST":
        print("Got it!!")
        newForm = Blog(request.POST)
        if newForm.is_valid():
            newForm.save()
        else:
            print("Try Again")
    return render(request, "blogApp/index.html", {"form":newForm})