from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def sample(request):
    return HttpResponse("hello world")

def sample1(request):
    return HttpResponse("Welcome")

def sampleInfo(request):
    # data={"name":"sri","age":21,"city":"hyd"}
    # return JsonResponse(data)
    data=[2,3,4,5,6]
    return JsonResponse(data,safe=False)

def dynamicResponse(request):
    name=request.GET.get("name","")
    city=request.GET.get('city','hyd')
    return HttpResponse(f"hello {name} from {city}")