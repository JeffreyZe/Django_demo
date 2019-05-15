from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):

    # return HttpResponse("<h1> Hello World </h1>")
    return render(request, 'home.html', {})

def people_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is our team',
        'my_slogon': 'Make data breach optional',
        'my_team': ['front end', 'back end', 'middleware'],
        'my_html': '<h3> Trying filter safe </h3>',
    }
    # return HttpResponse("<h1> Hello World </h1>")
    return render(request, 'people.html', my_context)
    
    
    
    # import os   
    # full_path = os.path.realpath(__file__)
    # x = os.path.dirname(full_path)[:-5]
    # img_path = 'src\dathena_logo.png'
    # return HttpResponse( "<h1>hello </h1> <img src=" + x + img_path +  "/>")
    