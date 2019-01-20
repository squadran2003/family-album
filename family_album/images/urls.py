from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:user_id>/', views.index, name='home'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail')

]
