from django.urls import path
from .import views
app_name='bank'
urlpatterns = [
        path('',views.index,name='index'),
        path('login/',views.login,name='login'),
        path('logout/',views.logout,name='logout'),
        path('register/',views.register,name='register'),
        path('bankform/', views.bankform, name='bankform'),
        path('get_branches/<int:district_id>/', views.get_branches, name='get_branches'),

]