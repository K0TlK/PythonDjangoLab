from django.shortcuts import render, redirect
from .forms import SupplyForm
import csv
from django.http import HttpResponse
from .models import Supply


def supply_list(request):
    supplies = Supply.objects.all()
    return render(request, 'supply_list.html', {'supplies': supplies})


def contact(request):
    return render(request, 'contact.html')


def export_supplies_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="supplies.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Quantity', 'Delivery Date'])

    supplies = Supply.objects.all()
    for supply in supplies:
        writer.writerow([supply.name, supply.quantity, supply.delivery_date])

    return response


def add_supply(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some-view')
    else:
        form = SupplyForm()

    return render(request, 'add_supply.html', {'form': form})


def home_view(request):
    return render(request, 'index.html')
