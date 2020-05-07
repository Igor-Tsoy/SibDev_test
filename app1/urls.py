from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('handle/<str:fmt>', views.HandleView.as_view(), name='handle')
]
