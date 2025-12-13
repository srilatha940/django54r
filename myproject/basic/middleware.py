from django.http import JsonResponse
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
