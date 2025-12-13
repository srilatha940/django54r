from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student,Insta
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

# to test database connection through api
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
            return JsonResponse({"status":'ok',"db":'connected'})
    except Exception as e:
        return JsonResponse({'status':'error','db':str(e)})

@csrf_exempt
def addStudent(request):
    print(request.method)
    if request.method=='POST':
        data=json.loads(request.body)
        student=Student.objects.create(
        name=data.get('name'),
        age=data.get("age"),
        email= data.get("email")
        )
        return JsonResponse({"status":"success","id":student.id},status=200)

    elif request.method=="GET":
        result=list(Student.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)

    elif request.method=="PUT":
        data=json.loads(request.body)
        ref_id=data.get('id')   #getting id 
        new_email=data.get("email")     #getting name
        existing_student=Student.objects.get(id=ref_id) #fetched the object as per the id
        # print(existing_student)
        existing_student.email=new_email  #updating with new name
        existing_student.save()
        updated_data=Student.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status":"data updated successfully","updated_data":updated_data},status=200)

    elif request.method=="DELETE":
        data=json.loads(request.body)
        ref_id=data.get('id')   #getting id
        to_be_delete=Student.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status":"success","message":"student record deleted successfully"},status=200)
    return JsonResponse({"error":"Use post method"},status=400)






@csrf_exempt
def Instapost(request):
    print(request.method)
    if request.method=="POST":
        data=json.loads(request.body)
        post=Insta.objects.create(
        post_name=data.get("post_name"),
        post_type=data.get("post_type"),
        post_date=data.get("post_date"),
        post_description=data.get("post_description")
        )
        return JsonResponse({"status":"success","id":post.id,"message":'post created successfully'},status=200)
    return JsonResponse({'error':"use post method"},status=200)

def job1(request):
    return JsonResponse({"message":"You have successfully applied for job1"},status=200)
def job2(request):
    return JsonResponse({"message":"You have successfully applied for job2"},status=200)