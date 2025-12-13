from django.http import JsonResponse
import re,json
class basicMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/student/"):
            # print(request,"hello")
            print(request.method,"method")
            print(request.path)
        response=self.get_response(request)
        return response

class basicMiddleware2:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/greet/"):
            print(request.method,"method")
            print(request.path)
        response=self.get_response(request)
        return response

class SscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["/job1/","/job2/"]):
            ssc_result=request.GET.get("ssc")
            print(ssc_result,"hello")
            if(ssc_result !='True'):
                return JsonResponse({"error":"You should qualify atleast ssc for qualifying this job"},status=400)
        return self.get_response(request)


class MedicalFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=='job1/'):
            medical_fit_result=request.GET.get("medically_fit")
            if(medically_fit!='True'):
                return JsonResponse({"error":"You are medically not fit"},status=400)
        return self.get_response(request)


class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ['/job1','/job2/']):
            age_checker=int(request.GET.get("age",56))
            if(age_checker>25 and age_checker<18):
                return JsonResponse({"error":"Yor are not eligible according to your age"},status=400)
        return self.get_response(request)


class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path=='/signup/'):
            data=json.loads(request.body)
            username=data.get("username","")
            # checks username is empty or not
            if not username:
                return JsonResponse({"error":"username is required"},status=400)
            # checks length
            if len(username)<3 or len(username)>20:
                return JsonResponse({"error":"username should contain 3 to 20 characters"},status=400)
            # checks starts with and ends with
            if username[0] in "._" or username[-1] in "._":
                return JsonResponse({"error":"username should not starts or ends with . or _"},status=400)
            # checks allowed characters
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
                return JsonResponse({"error":"username should contain letters,numbers,digits,.,_"},status=400)
            # checks .. and __
            if ".." in username or "__" in username:
                return JsonResponse({"error":"cannot have .. __"},status=400)
        return self.get_response(request)


# class EmailMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):

# class PasswordMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request)
