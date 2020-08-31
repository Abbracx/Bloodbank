from  django.urls import path
from bloodrequestapp import views


app_name = "bloodrequestapp"
urlpatterns = [
	path('donate/', views.donate, name='donate'),
    path('request/', views.request, name='request'),
    path('refer/', views.refer, name='refer'),
   
]
