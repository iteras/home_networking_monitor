from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sbc', views.sbc_linechart, name="sbc_linechart"),
    path('sbc_post', views.sbc_post, name="sbc_post"),
    path('<int:sbc_id>/data', views.sbc_temperature_data, name="sbc_temperature_data"),
    path('re_post', views.re_post, name="re_post"),
    path('re/data', views.re_data_linechart, name="re_temperature_data")
]