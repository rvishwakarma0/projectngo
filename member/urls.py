from django.urls import path
from member import views


app_name = 'member'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout')
]
