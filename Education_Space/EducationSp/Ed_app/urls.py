from django.urls import path
from Ed_app import views

app_name = 'Ed_app'

urlpatterns = [
    path('user_register/', views.User_register, name="user_registration"),
    path('course_register/', views.Course_register, name="course_registration"),
    path('login/', views.Login, name="login")
]