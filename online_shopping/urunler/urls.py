from django.urls import path, include
from .views import UrunListApiView, UrunDetailApiView, SaticiDetailApiView, SaticiListApiView

urlpatterns = [
    path('urunler/', UrunListApiView.as_view()),
    path('urunler/<int:pk>', UrunDetailApiView.as_view()),
    path('saticilar/<int:pk>', SaticiDetailApiView.as_view()),
    path('saticilar/', SaticiListApiView.as_view()),
]
