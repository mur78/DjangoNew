from datetime import datetime

from django.shortcuts import render
# Create your views here.
from django.views import View
# from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

class IndexView(View):
   def get(self, request):
       return render(request, "common/index.html")


