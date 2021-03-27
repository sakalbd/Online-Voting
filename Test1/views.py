from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

#def show_test_home_page(request):
#    return HttpResponse("This is test1 home page")

def show_test_home_page(request):
    return render(request,'Test1/home.html')


def show_test1_info_page(request):
    return HttpResponse("This is test1 info page")