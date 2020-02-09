from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from core.views import signup

urlpatterns = [
    path('', RedirectView.as_view(url='/number/', permanent=False)),
    path('admin/', admin.site.urls),
    path('number/', include('core.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('signup/', signup),
    path('logout/', auth_views.LogoutView.as_view()),
]
