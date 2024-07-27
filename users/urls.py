from django.urls import path
from . import views

urlpatterns = [
    path('send_sms_via_email/', views.send_sms_via_email, name='send_sms_via_email'),
    
    
    path('events', views.event,name='events'),
    path('mainLogin', views.mainLogin, name='mainLogin'),
    path('mainDashboard', views.mainDashboard, name='mainDashboard'),
    path('inputData', views.inputData, name='inputData'),
    path('approveAccount', views.approveAccount, name='approveAccount'),
    
    path('<int:event_id>/removeEvent/', views.removeEvent, name='removeEvent'),
    path('<int:user_id>/removeUser/', views.removeUser, name='removeUser'),
    path('acceptUser/<int:user_id>/', views.acceptUser, name='acceptUser'),
    path('declineUser/<int:user_id>/', views.declineUser, name='declineUser'),
    
    path('event/<int:event_id>/like/', views.likeEvent, name='like_event'),
    path('event/<int:event_id>/dislike/', views.dislikeEvent, name='dislike_event'),
    
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('register', views.register, name='register'),

    path('seniorsEvent', views.seniorsEvent, name='seniorsEvent'),
    path('seniorResponse', views.seniorResponse, name='seniorResponse'),
    path('seniorDashboard', views.seniorDashboard, name='seniorDashboard'),
    
    path('logoutUser', views.logoutUser, name='logoutUser'),
]