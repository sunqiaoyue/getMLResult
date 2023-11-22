from django.urls import path
from .views import getMLResult

urlpatterns = [
    path('getMLResult/', getMLResult.as_view(), name='get-ml-result'),
]
