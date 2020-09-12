from  django.urls import path
from bloodrequestapp import views


app_name = "bloodrequestapp"
urlpatterns = [
	path('donate/', views.blood_donate, name='blood_donate'),
    path('request/', views.blood_request, name='blood_request'),
    path('refer/', views.blood_refer, name='blood_refer'),
    path('incoming_request/', views.incoming_request, name='incoming_request'),
    path('<uuid:user_id>/all-sent-request', views.list_of_request, name='user_requests'),
   
]
