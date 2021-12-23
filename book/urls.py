from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingView.as_view(), name='book'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('cancel-confirm/<str:id>/', views.CancelConfirmView, name='cancel-confirm'),
]