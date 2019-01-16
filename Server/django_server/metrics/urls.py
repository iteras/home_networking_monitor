from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sbc_id>',views.sbc_temperature,name="detail")
]