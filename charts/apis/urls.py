from django.urls import path
from charts.apis import views as api_views

urlpatterns = [
    path('get-random-data/', api_views.get_random_chart_data, name='random-chart-data'),
]
