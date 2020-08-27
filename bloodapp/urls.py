from  django.urls import path
from bloodapp import views


app_name = "bloodapp"
urlpatterns = [
	path('', views.homepage, name='homepage'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
     path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),
]