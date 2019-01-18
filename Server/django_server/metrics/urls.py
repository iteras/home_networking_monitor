from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sbc_id>', views.sbc_temperature, name="sbc_temperature"),
    path('<int:sbc_id>/data', views.sbc_temperature_data, name="sbc_temperature_data")
]