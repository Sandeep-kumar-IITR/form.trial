from datetime import datetime

from django.shortcuts import render, HttpResponse
from datetime import datetime


# Create your views here.
from home.models import url_v


def index(request):
    if request.method == "POST":
        # url = 'https://www.youtube.com/c/filmigaane'
        url = request.POST.get('url')
        url_vt = url_v(url=url,date=datetime.today())
        url_vt.save()



    return render(request, 'index.html')
