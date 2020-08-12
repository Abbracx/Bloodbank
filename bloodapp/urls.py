from  django.urls import path
from bloodapp import views


app_name = "users"
urlpatterns = [
	path('', views.homepage, name='homepage')
    path('profile/<int:user_id>/', view.profile, name='user-profile'),
    
]