from django.urls import path
from.views import *
urlpatterns=[
    path('Login/',Login),
    path('Logout/',Logout),
    path('Register/',Register),
]