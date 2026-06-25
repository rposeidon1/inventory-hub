from django.urls import path
from core import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="home"),
    path("client-list/", views.ClientListView.as_view(), name="clients"),
    path("client/<int:pk>/detail/", views.ClientDetailView.as_view(), name="client"),
    path("client-create/", views.ClientCreateView.as_view(), name="create_client"),
    path("client/<int:pk>/update/", views.ClientUpdateView.as_view(), name="update_client"),
    path("client/<int:pk>/delete/", views.ClientDeleteView.as_view(), name="delete_client"),
    path("item-list/", views.InventoryItemListView.as_view(), name="items"),
    path("item/<int:pk>/detail/", views.InventoryItemDetailView.as_view(), name="item"),
    path("item-create/", views.InventoryItemCreateView.as_view(), name="create_item"),
    path("item/<int:pk>/update/", views.InventoryItemUpdateView.as_view(), name="update_item"),
    path("item/<int:pk>/delete/", views.InventoryItemDeleteView.as_view(), name="delete_item"),
    path("order-list/", views.OrderListView.as_view(), name="orders"),
    path("order/<int:pk>/detail/", views.OrderDetailView.as_view(), name="order"),
    path("order-create/", views.OrderCreateView.as_view(), name="create_order"),
    path("order/<int:pk>/update/", views.OrderUpdateView.as_view(), name="update_order"),
    path("order/<int:pk>/delete/", views.OrderDeleteView.as_view(), name="delete_order"),
    path("client/<int:pk>/modal-update/", views.ClientModalUpdateView.as_view(), name="modal_update_client"),
    path("item/<int:pk>/modal-update/", views.InventoryItemModalUpdateView.as_view(), name="modal_update_item"),
]