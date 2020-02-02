from django.urls import path
from charts import views as chart_views

urlpatterns = [
    path('', chart_views.index, name='chart-home')

]
