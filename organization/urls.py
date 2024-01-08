from django.urls import path
from organization import views

app_name = 'organization'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-list'),
    path('detail/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('update/<int:pk>', views.OrderUpdateView.as_view(), name='order-update'),
    path('trade_points/', views.TradePointListView.as_view(), name='trade_points-list'),
    path('trade_points/<int:pk>/', views.TradePointDetailView.as_view(), name='trade_points-detail'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers-list'),
    path('suppliers/<int:pk>/', views.SupplierDetailView.as_view(), name='suppliers-detail'),
    path('organizations/', views.OrganizationListView.as_view(), name='organizations-list'),
    path('organizations/<int:pk>/', views.OrganizationDetailView.as_view(), name='organizations-detail'),
]