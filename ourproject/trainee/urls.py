from django.urls import path

from .views import *
urlpatterns=[
    path('',alltrainee,name='alltrainee'),
    path('Update/<int:id>/', updatetrainee ,name='updatetrainee'),
    path('Insert/', inserttrainee,name='inserttrainee'),
    path('Delete/<int:id>/', deletetrainee ,name='deletetrainee'),
]