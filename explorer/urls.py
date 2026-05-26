from django.urls import path
from .views import explore

urlpatterns = [
    path('', explore, name='home'),
    path('explore/<path:folder_path>/', explore, name='explore'),
]