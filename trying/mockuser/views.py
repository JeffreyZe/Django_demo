from django.shortcuts import render

from .models import Mockuser

# Create your views here.
def mockuser_detail_view(request):
    obj = Mockuser.objects.get(id=1)
    # context = {
    #     'name': obj.name,
    #     'age': obj.age
    # }
    context = {
        'object' : obj
    }
    return render(request, 'mockuser/mockuser_detail.html', context)
