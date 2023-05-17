from django.urls import path
from .views import *
urlpatterns = [
    # director
    path("director-create/", create_director),
    path("director-update/<int:pk>/", update_director),
    path("director-delete/<int:pk>/", delete_director),

    #reception
    path("reception-create/", create_reception),
    path("reception-update/<int:pk>/", update_reception),
    path("reception-delete/<int:pk>/", delete_reception),

    #teacher
    path("teacher-create/", create_teacher),
    path("teacher-update/<int:pk>/", update_teacher),
    path("teacher-delete/<int:pk>/", delete_teacher),

    # student
    path("student-create/", create_student),
    path("student-update/<int:pk>/", update_student),
    path("student-delete/<int:pk>/", delete_student),

    # group
    path("group-create/", create_group),
    path("group-update/<int:pk>/", update_group),
    path("group-delete/<int:pk>/", delete_group),

    # course
    path("course-create/", create_course),
    path("course-update/<int:pk>/", update_course),
    path("course-delete/<int:pk>/", delete_course),
]