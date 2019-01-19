from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sbc', views.sbc_linechart, name="sbc_linechart"),
    path('<int:sbc_id>/data', views.sbc_temperature_data, name="sbc_temperature_data")
]