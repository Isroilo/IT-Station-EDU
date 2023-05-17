from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Student
        fields = "__all__"


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Director
        fields = "__all__"


class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Reception
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Group
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Payment
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Course
        fields = "__all__"


class TeacherSalarySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = TeacherSalary
        fields = "__all__"




