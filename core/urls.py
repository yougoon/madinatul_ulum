from django.urls import path
from . import views
from .views import admission
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('admission/', views.admission, name='admission'),
]




