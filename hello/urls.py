from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hello/', views.your_view, name='myView'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



