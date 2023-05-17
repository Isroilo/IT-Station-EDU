from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from .serializer import *



@api_view(['GET'])
def student_view(request):
    student = Student.objects.all().order_by('-id')
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def teacher_view(request):
    teacher = Teacher.objects.all().order_by('-id')
    serializer = TeacherSerializer(teacher, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def reception_view(request):
    reception = Reception.objects.all().order_by('-id')
    serializer = ReceptionSerializer(reception, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all().order_by('-id')
    serializer = DirectorSerializer(director, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def group_view(request):
    group = Group.objects.all().order_by('-id')
    serializer = GroupSerializer(group, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_student_by_group(request,pk):
    group = Group.objects.get(id=pk)
    student = Student.objects.filter(group=group)
    ser = StudentSerializer(student, many=True)
    return Response(ser.data)


@api_view(['POST'])
def filter_group_by_time(request,pk):
    start_time = request.POST.get('start_time').replace(':', '')
    end_time = request.POST.get('end_time').replace(':', '')
    course = Course.objects.get(id=pk)
    groups = Group.objects.filter(course=course).order_by('-id')
    l = 0
    for i in groups:
        s = str(i.start_time).replace(':', '')
        e = str(i.end_time).replace(':', '')
        times = []
        for x in range(int(start_time),int(end_time)):
            times.append(x)
        for r in range(int(s), int(e)):
            if r in times:
                return Response(False)
            else:
                return Response(True)





    # @api_view(['POST'])
    # def filter_group_by_time(request, pk):
    #     start_time = request.POST.get('start_time').replace('-', '')
    #     end_time = request.POST.get('end_time').replace('-', '')
    #     course = Course.objects.get(id=pk)
    #     groups = Group.objects.filter(course=course).order_by('-id')
    #     free = []
    #     for group in groups:
    #         group = group.room_order.all()
    #         dates = []
    #         xx = True
    #         for d in range(int(date_start), int(date_end) + 1):
    #             dates.append(d)
    #         if hotel_orders:
    #             return Response(False)
    #         else:
    #             return Response(True)

    # def filter_rooms_date(request, pk):
    #     date_start = request.POST.get('start').replace('-', '')
    #     date_end = request.POST.get('end').replace('-', '')
    #     hotel = Hotel.objects.get(pk=pk)
    #     rooms = Room.objects.filter(hotel=hotel)
    #     free_rooms = []
    #     for room in rooms:
    #         hotel_orders = room.room_order.all()
    #         dates = []
    #         xx = True
    #         for d in range(int(date_start), int(date_end) + 1):
    #             dates.append(d)
    #         if hotel_orders:
    #             for hotel_order in hotel_orders:
    #                 ds = str(hotel_order.start).replace('-', '')
    #                 de = str(hotel_order.end).replace('-', '')
    #                 for i in range(int(ds), int(de) + 1):
    #                     if i in dates:
    #                         xx = False
    #         if xx == True:
    #             free_rooms.append(room)
    #     if len(free_rooms) > 0:
    #         ser = RoomSerializer(free_rooms, many=True)
    #         return Response(ser.data)
    #     else:
    #         return Response({"message": "bu kunlarga bosh xonalarimiz yoq "})



