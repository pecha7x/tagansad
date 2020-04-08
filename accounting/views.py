from django.shortcuts import get_object_or_404, render

from .models import Plant


def index(request):
    plants = Plant.objects.order_by('name')
    context = {'plants': plants}
    return render(request, 'plants/index.html', context)


def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})
