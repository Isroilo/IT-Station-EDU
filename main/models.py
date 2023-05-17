from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_director = models.BooleanField(default=False)
    is_reception = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, blank=True,null=True)
    address = models.CharField(max_length=255, blank=True,null=True)
    percent = models.IntegerField()
    course = models.ForeignKey('Course', on_delete=models.SET_NULL,null=True,blank=True)
    salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, blank=True,null=True)
    parent_phone = models.CharField(max_length=13)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL,null=True,blank=True)
    lap_top = models.BooleanField(default=False)
    STATUS_CHOICES = (
        ('unpaid', 'Unpaid'),
        ('full_paid', 'Full Paid'),
        ('low_paid', 'Low Paid'),
        ('excess_amount_choisec', 'Excess Amount'),
    )
    SOURCE_CHOICES = (
        (1, 'Social Network'),
        (2, 'Acquaintances'),
        (3, 'Advertising'),
        (4, 'Other'),
    )
    source = models.IntegerField(choices=SOURCE_CHOICES,blank=True, null=True)
    pay_amount = models.IntegerField(default=0,null=True,blank=True)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES, default='unpaid',blank=True, null=True)

    def __str__(self):
        return self.firs_name


class Director(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return self.user.username


class Reception(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True,blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    STATUS_CHOICES = (
        (1, "Active"),
        (2, "Pending"),
        (3, "Full"),
        (4, "Completed"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    status_day = models.CharField(max_length=50, choices=DAY_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    pay_type = (
        (1, "Naqd"),
        (2, "Plastik"),
    )
    type = models.IntegerField(default=0, choices=pay_type)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    summa = models.PositiveIntegerField()
    from_date = models.TimeField()
    to_date = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.summa}"


class TeacherSalary(models.Model):
    pay_type = (
        (1, "Naqd"),
        (2, "Plastik"),
    )
    type = models.IntegerField(default=0, choices=pay_type)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    summa = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.user.username} {self.summa}"