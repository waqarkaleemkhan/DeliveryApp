from django.urls import path
from .views.Index import Index
from .views.About import About

urlpatterns=[
    path('',Index.as_view(),name="index"),
    path('about',About.as_view(),name='about')
]