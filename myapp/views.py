from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from myapp.serializers import Studentserializers
from . models import Student

@csrf_exempt

def studentAPI(request,id=0):
    if request.method=='GET':
        student=Student.objects.all()
        student_serializers=Studentserializers(student,many=True)
        return JsonResponse(student_serializers.data,safe=False)
    
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializers=Studentserializers(data=student_data)
        if student_serializers.is_valid():
            student_serializers.save()
            return JsonResponse ('Added successfully',safe=False)
        return JsonResponse ('Failed to add',safe=False)
    
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(id=id)
        student_serializers=Studentserializers(student,data=student_data)
        if student_serializers.is_valid():
            student_serializers.save()
            return JsonResponse ('Upadte successfully',safe=False)
        return JsonResponse ('Failed to Update')
    
    elif request.method =='DELETE':
        student=Student.objects.get(id=id)
        student.delete()
        return JsonResponse (" deleted",safe=False)
        
    
    
        


