from django.urls import path
from app.homework import views

urlpatterns = [
    path('createuser/', views.UserView.as_view(), name='createuser')
]
