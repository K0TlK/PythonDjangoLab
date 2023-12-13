from .views import export_supplies_csv
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-supply/', views.add_supply, name='add-supply'),
    path('supply-list/', views.supply_list, name='supply-list'),
    path('contact/', views.contact, name='contact'),
    path('export-csv/', views.export_supplies_csv, name='export-csv'),
    path('', views.home_view, name='home'),
]
