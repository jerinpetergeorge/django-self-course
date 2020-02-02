from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include(('charts.apis.urls', 'charts'), namespace='chart-api')),
    path('chart/', include(('charts.urls', 'charts'), namespace='chart')),
    path('admin/', admin.site.urls),
]
