from django.shortcuts import render_to_response

from mainsite.models import Project

def home(request):
    context = {}
    return render_to_response('home.html', context)