from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):

    # return HttpResponse("<h1> Hello World </h1>")
    return render(request, 'home.html', {})
    
    
    
    # import os   
    # full_path = os.path.realpath(__file__)
    # x = os.path.dirname(full_path)[:-5]
    # img_path = 'src\dathena_logo.png'
    # return HttpResponse( "<h1>hello </h1> <img src=" + x + img_path +  "/>")
    