
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('contact', views.contact),
    path('vehicle', views.vehicle),
    path('admission' , views.admission),
    # path('donate', views.donate),
    path('query', views.query)

]
