from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the firstapp index.")

class MyView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the firstapp index using a class-based view.")