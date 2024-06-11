from . import views
from django.urls import path

urlpatterns = [
        path('add/',views.add_intake,name='add'),
         path('list/',views.intake_list,name='list'),
         path('update/<int:id>/',views.intake_update,name='updateintake'),
         path('delete/<int:id>/',views.intake_delete,name='deleteintake'),
         
        
        ]