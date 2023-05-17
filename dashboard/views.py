from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from main.models import *
from main.serializer import *

""""Director"""
@api_view(['POST'])
def create_director(request):
    user = request.POST['user']
    firs_name = request.POST['firs_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    address = request.POST['address']
    director = Director.objects.create(
                user_id = user,
                firs_name = firs_name,
                last_name = last_name,
                phone = phone,
                address = address,
            )
    ser = DirectorSerializer(director)
    return Response(ser.data)

@api_view(['PUT'])
def update_director(request,pk):
    director = Director.objects.get(id=pk)
    user = request.POST['user']
    firs_name = request.POST['firs_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    address = request.POST['address']
    director.user_id = user
    director.firs_name = firs_name
    director.last_name = last_name
    director.phone = phone
    director.address = address
    director.save()
    ser = DirectorSerializer(director)
    return Response(ser.data)

@api_view(['DELETE'])
def delete_director(request,pk):
    director = Director.objects.get(id=pk)
    director.delete()
    return Response("deleted")


"""" Reception """
@api_view(['POST'])
def create_reception(request):
    user = request.POST['user']
    firs_name = request.POST['firs_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    address = request.POST['address']
    reception = Reception.objects.create(
                user_id = user,
                firs_name = firs_name,
                last_name = last_name,
                phone = phone,
                address = address,
            )
    ser = ReceptionSerializer(reception)
    return Response(ser.data)

@api_view(['PUT'])
def update_reception(request,pk):
    reception = Reception.objects.get(id=pk)
    user = request.POST['user']
    firs_name = request.POST['firs_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    address = request.POST['address']
    reception.user_id = user
    reception.firs_name = firs_name
    reception.last_name = last_name
    reception.phone = phone
    reception.address = address
    reception.save()
    ser = ReceptionSerializer(reception)
    return Response(ser.data)

@api_view(['DELETE'])
def delete_reception(request,pk):
    reception = Reception.objects.get(id=pk)
    reception.delete()
    return Response("deleted")


"""" Teacher """
@api_view(['POST'])
def create_teacher(request):
    user = request.POST['user']
    firs_name = request.POST['firs_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    address = request.POST['address']
    percent = request.POST['percent']
    course = request.POST['course']
    teacher = Teacher.objects.create(
                user_id = user,
                firs_name = firs_name,
                last_name = last_name,
                phone = phone,
                address = address,
                percent = percent,
                course_id = course,
            )
    ser = TeacherSerializer(teacher)
    return Response(ser.data)


@api_view(['PUT'])
def update_teacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    user = request.POST['user']
    firs_name = request.POST['firs_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    address = request.POST['address']
    percent = request.POST['percent']
    course = request.POST['course']
    salary = request.POST.get('salary')
    teacher.user_id = user
    teacher.firs_name = firs_name
    teacher.last_name = last_name
    teacher.phone = phone
    teacher.address = address
    teacher.percent = percent
    teacher.course_id = course
    if salary is not None:
        teacher.salary = salary
    teacher.save()
    ser = TeacherSerializer(teacher)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_teacher(request,pk):
    reception = Teacher.objects.get(id=pk)
    reception.delete()
    return Response("deleted")


"""" Student """

@api_view(['POST'])
def create_student(request):
    firs_name = request.POST['firs_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    parent_phone = request.POST['parent_phone']
    group = request.POST['group']
    lap_top = request.POST['lap_top']
    source = request.POST['source']
    student = Student.objects.create(
                firs_name = firs_name,
                last_name = last_name,
                phone = phone,
                parent_phone = parent_phone,
                group_id = group,
                lap_top = lap_top,
                source = source,
            )
    ser = StudentSerializer(student)
    return Response(ser.data)


@api_view(['PUT'])
def update_student(request,pk):
    student = Student.objects.get(id=pk)
    firs_name = request.POST['firs_name']
    last_name = request.POST['last_name']
    phone = request.POST['phone']
    parent_phone = request.POST['parent_phone']
    group = request.POST['group']
    lap_top = request.POST['lap_top']
    source = request.POST['source']
    student.firs_name = firs_name
    student.last_name = last_name
    student.phone = phone
    student.parent_phone = parent_phone
    student.group_id = group
    student.lap_top = lap_top
    student.source = source
    student.save()
    ser = StudentSerializer(student)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_student(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response("deleted")


"""" Group """
@api_view(['POST'])
def create_group(request):
    name = request.POST['name']
    course = request.POST['course']
    teacher = request.POST['teacher']
    price = request.POST['price']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    status_day = request.POST['status_day']
    group = Group.objects.create(
                name = name,
                course_id = course,
                teacher_id = teacher,
                price = price,
                start_time = start_time,
                end_time = end_time,
                status_day = status_day,
            )
    ser = GroupSerializer(group)
    return Response(ser.data)


@api_view(['PUT'])
def update_group(request,pk):
    group = Group.objects.get(id=pk)
    name = request.POST['name']
    course = request.POST['course']
    teacher = request.POST['teacher']
    price = request.POST['price']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    status_day = request.POST['status_day']
    group.name = name
    group.course_id = course
    group.teacher_id = teacher
    group.price = price
    group.start_time = start_time
    group.end_time = end_time
    group.status_day = status_day
    group.save()
    ser = GroupSerializer(group)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_group(request,pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return Response("deleted")


"""" Course """

@api_view(['POST'])
def create_course(request):
    name = request.POST['name']
    course = Course.objects.create(
                name = name,
            )
    ser = CourseSerializer(course)
    return Response(ser.data)


@api_view(['PUT'])
def update_course(request,pk):
    course = Course.objects.get(id=pk)
    name = request.POST['name']
    course.name = name
    course.save()
    ser = CourseSerializer(course)
    return Response(ser.data)


@api_view(['DELETE'])
def delete_course(request,pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return Response("deleted")


