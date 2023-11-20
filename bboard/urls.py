from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.index, name='main'),
    path('aboutme', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('', views.courses_list, name='courses')
]