from django.urls import path

from . import views

app_name = 'signups'

urlpatterns = [
    path('signup/', views.Signup.as_view(),name='signup'),

]
