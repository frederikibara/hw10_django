from django.contrib import admin 
from django.urls import path, include
from users.views import signupuser, loginuser, logoutuser 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('quotes.urls')),
    path('users/signup/', signupuser, name='signup'),  
    path('users/login/', loginuser, name='login'),      
    path('users/logout/', logoutuser, name='logout'),   
]
