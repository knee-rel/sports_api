from django.contrib import admin
from django.urls import path
from sports_api import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'sports_api'  # Add this line to specify the app_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sports/', views.sport_list, name='sport_list'),
    path('sports/<int:id>', views.sport_detail, name='sport_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
