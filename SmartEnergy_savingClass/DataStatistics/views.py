import json

from django.shortcuts import render

# Create your views here.
from DataStatistics.models import TbLine


def dataview(request):
    data = TbLine.objects.order_by('date')
    tem1 = data[0].temp
    tem2 = data[1].temp
    tem3 = data[2].temp
    tem4 = data[3].temp
    tem5 = data[4].temp
    tem6 = data[5].temp
    tem7 = data[6].temp
    return render(request, 'graph_flot.html', {'Series1': tem1,
                                               'Series2': tem2,
                                               'Series3': tem3,
                                               'Series4': tem4,
                                               'Series5': tem5,
                                               'Series6': tem6,
                                               'Series7': tem7})
