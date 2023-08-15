from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # include all default authentication url
    path("", include('django.contrib.auth.urls')),
    # include registration urls
    path('registration', views.register, name='register'),

]
