from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from core.models import Client, InventoryItem, Order
from django.db.models import F, Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import StaffOnlyMixin



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["low_stock_items"] = InventoryItem.objects.filter(quantity__lte=F("low_stock_threshold"))
        return context

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "core/client_list.html"
    context_object_name = "clients"

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Client.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        return Client.objects.all()

    def get_template_names(self):
        if self.request.headers.get('HX-Request'):
            return ['core/partials/client_list_partial.html']
        return ['core/client_list.html']


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "core/client_detail.html"
    context_object_name = "client"

class ClientCreateView(StaffOnlyMixin, CreateView):
    model = Client
    template_name = "core/client_form.html"
    fields = ["first_name", "last_name", "email", "phone", "company"]
    success_url = reverse_lazy("clients")

class ClientUpdateView(StaffOnlyMixin, UpdateView):
    model = Client
    template_name = "core/client_form.html"
    fields = ["first_name", "last_name", "email", "phone", "company"]
    success_url = reverse_lazy("clients")

class ClientModalUpdateView(StaffOnlyMixin, UpdateView):
    model = Client
    template_name = "core/client_modal_form.html"
    fields = ["first_name", "last_name", "email", "phone", "company"]
    success_url = reverse_lazy("clients")

class ClientDeleteView(StaffOnlyMixin, DeleteView):
    model = Client
    template_name = "core/client_confirm_delete.html"
    success_url = reverse_lazy("clients")



class InventoryItemListView(LoginRequiredMixin, ListView):
    model = InventoryItem
    template_name = "core/item_list.html"
    context_object_name = "items"

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return InventoryItem.objects.filter(
                Q(name__icontains=query) 
            )
        return InventoryItem.objects.all()

    def get_template_names(self):
        if self.request.headers.get('HX-Request'):
            return ['core/partials/item_list_partial.html']
        return ['core/item_list.html']

class InventoryItemDetailView(LoginRequiredMixin, DetailView):
    model = InventoryItem
    template_name = "core/item_detail.html"
    context_object_name = "item"

class InventoryItemCreateView(StaffOnlyMixin, CreateView):
    model = InventoryItem
    template_name = "core/item_form.html"
    fields = ["name", "description", "price", "quantity", "low_stock_threshold"]
    success_url = reverse_lazy("items")

class InventoryItemUpdateView(StaffOnlyMixin, UpdateView):
    model = InventoryItem
    template_name = "core/item_form.html"
    fields = ["name", "description", "price", "quantity", "low_stock_threshold"]
    success_url = reverse_lazy("items")

class InventoryItemModalUpdateView(StaffOnlyMixin, UpdateView):
    model = InventoryItem
    template_name = "core/item_modal_form.html"
    fields = ["name", "description", "price", "quantity", "low_stock_threshold"]
    success_url = reverse_lazy("items")


class InventoryItemDeleteView(StaffOnlyMixin, DeleteView):
    model = InventoryItem
    template_name = "core/item_confirm_delete.html"
    success_url = reverse_lazy("items")



class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "core/order_list.html"
    context_object_name = "orders"

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "core/order_detail.html"
    context_object_name = "order"

class OrderCreateView(StaffOnlyMixin, CreateView):
    model = Order
    template_name = "core/order_form.html"
    fields = ["client", "item", "quantity", "status"]
    success_url = reverse_lazy("orders")

class OrderUpdateView(StaffOnlyMixin, UpdateView):
    model = Order
    template_name = "core/order_form.html"
    fields = ["client", "item", "quantity", "status"]
    success_url = reverse_lazy("orders")

class OrderDeleteView(StaffOnlyMixin, DeleteView):
    model = Order
    template_name = "core/order_confirm_delete.html"
    success_url = reverse_lazy("orders")
