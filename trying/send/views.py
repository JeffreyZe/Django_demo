from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def index(request):

    send_mail("Testing", 'Hello World', 'noreply@dathena.io', ['xuze.wang@dathena.io'], fail_silently = False,)
    # 'Hello world. THis is testing for the mailhog',
    # 'test@test.com', #sender
    # ['xuze.wang@dathena.io'] #recipients
    
    
    return render(request, 'send/index.html')