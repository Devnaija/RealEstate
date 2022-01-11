from django.shortcuts import render
from .models import Realtor
# Create your views here.


def realtors(request):


  context = {
 
  }
  return render(request, 'pages/about.html',context)
