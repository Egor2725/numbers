from django.urls import path

from .views import show_number


urlpatterns = [
    path('', show_number, ),
]
