from django.urls import path
from . import views

urlpatterns = [
      path('intakedifference/',views.listdifference,name='difference'),
     path('calculate/',views.calculate_difference,name='calculate'),
      path('list_intakes/',views.list_intakes,name='list_intakes'),
    
    
]