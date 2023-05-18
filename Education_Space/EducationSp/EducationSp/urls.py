from django.contrib import admin
from django.urls import path, include
from Ed_app import views
urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('Ed_app/', include('Ed_app.urls')),
    path('logout/', views.Logout, name="logout"),
    path('special/', views.special, name="special"),
]
