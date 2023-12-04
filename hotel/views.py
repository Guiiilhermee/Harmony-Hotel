from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    """ A view to return the home page """
    return render(request, 'home.html')
