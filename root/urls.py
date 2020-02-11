from django.contrib import admin
from django.urls import path, include
from django_select2.views import select2, AlbumAutoCompleteView

urlpatterns = [
    path('', select2, name='select2-test'),
    path('api/v1/albums/', AlbumAutoCompleteView.as_view(), name='albums'),
    path('api/v1/', include(('charts.apis.urls', 'charts'), namespace='chart-api')),
    path('chart/', include(('charts.urls', 'charts'), namespace='chart')),
    path('admin/', admin.site.urls),
]
