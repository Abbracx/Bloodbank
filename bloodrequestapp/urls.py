from  django.urls import path
from bloodrequestapp import views


app_name = "bloodrequestapp"
urlpatterns = [
	path('donate/', views.blood_donate, name='blood_donate'),
    path('request/', views.blood_request, name='blood_request'),
    path('refer/', views.blood_refer, name='blood_refer'),
   
]
