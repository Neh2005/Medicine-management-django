from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/', views.aboutUs, name='aboutus'),  # This maps 'aboutus/' to the aboutUs view
]
