from django.urls import path
from medical_center import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('about/', views.about_view, name='about'),
    path('service/', views.service_view, name='service'),
    path('contact/', views.contact_view, name='contact'),

]