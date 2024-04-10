from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('<int:id>', views.PostView.as_view()),
]
