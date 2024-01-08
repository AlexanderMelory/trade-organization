from django.urls import path
from organization import views

app_name = 'organization'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-list'),
    path('detail/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('update/', views.OrderUpdateView.as_view(), name='order-update'),
]