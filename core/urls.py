from django.urls import path

from .views import show_number


urlpatterns = [
    path('number/', show_number, name='number')
]
