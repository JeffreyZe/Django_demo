from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Mockdata
from .serializers import MockdataSerializer

class MockdataView(viewsets.ModelViewSet):
    queryset  = Mockdata.objects.all()
    serializer_class = MockdataSerializer



# Create your views here.
# def home_view():
#     return HttpResponse("<h1> Hello World")

# from .forms import MockdataForm

# from .models import Mockdata

# def mockdata_create_view(request):
#     form = MockdataForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context = {
#         'form': form
#     }
#     return  render(request, 'mockdata/mockdara_create.html', context)