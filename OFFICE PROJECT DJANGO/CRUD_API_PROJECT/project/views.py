from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data Inserted !!!...'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')



# Model Object & Single Student Data
def student_info_one(request, pk=None):
    stu_data = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu_data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# Query Set - All Student Data
def student_info_all(request):
    stu_data = Student.objects.all()
    serializer = StudentSerializer(stu_data, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    