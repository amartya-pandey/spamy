from django.urls import path
from .views import classify_email_view

urlpatterns = [
    path('classify/', classify_email_view, name='classify-email'),
]