
from django.urls import path,include
from user import views

urlpatterns = [
    path('', views.greeting,name='home'),
     path('signup/', views.signup_page,name='signup'),
     path('login/', views.login_page,name='login'),
     path('logout/', views.logout_view,name='logout'),
      path('intake/', include('intake.urls')),
       path('intakeajax/', include('intakeajax.urls')),

]

