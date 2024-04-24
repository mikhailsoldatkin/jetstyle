from django.urls import path

from fibo import views

urlpatterns = [
    path("fibonacci/", views.FibonacciTaskAPIView.as_view()),
    path("tasks/<str:uuid>/", views.FibonacciTaskDetailAPIView.as_view()),
]
