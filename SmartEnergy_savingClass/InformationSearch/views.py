from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from InformationSearch.models import Search



@csrf_exempt
def infoview(request):
    if request.method == 'POST':
        tim = request.POST.get("time")
        data = Search.objects.filter(time=tim)
    return render(request, 'projects.html',locals())



