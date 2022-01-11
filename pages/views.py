from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices,price_choices,bedroom_choices

def index(request):
  
  shows = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

  context = {
      'shows': shows,
      'state_choices':state_choices,
      'price_choices':price_choices,
      'bedroom_choices':bedroom_choices
  }

  return render(request,'pages/index.html',context)

def about(request):
  realtors = Realtor.objects.order_by(
        '-hire_date')

  mvp_reltors = Realtor.objects.all().filter(is_mvp=True)

  context = {
      'shows': realtors,
      'showmvp': mvp_reltors
  }
  return render(request,'pages/about.html',context)
