from functools import partial
import json
from django.shortcuts import render,HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from datetime import datetime
import csv
from django.contrib.auth.models import User
from .Capture import Sendata

# Create your views here.
@csrf_exempt
def student_data(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        # print('PYTHONDATA',pythondata)
        roll=str(pythondata['rollnumber'])
        # print('Roll is ->',roll)
        stu=Student.objects.get(rollnumber=roll)
        # print('STUDENT IS ->',stu)
        # print('Attendance is ->',stu.attendance)
        stu.attendance=stu.attendance+1 #AttendanceUpdated
        print('----------------------END-------------------------')
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated !!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        

            
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance.csv"'

    writer = csv.writer(response)
    writer.writerow(['Roll_Number', 'Name', 'Last_Name', 'Attendance','Time_Of_Attendance'])

    Attendance = Student.objects.all().values_list('rollnumber', 'name', 'lname', 'attendance','time_of_attendance')
    for user in Attendance:
        writer.writerow(user)

    return response


def home(request):
    return render(request,'app/home.html')

# def attendance(request):
#     return render(request,'app/attendance.html')

def data(request):
    Sendata.call()
    return render(request,'app/attendance.html')