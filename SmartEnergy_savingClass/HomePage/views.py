from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render(request, 'index.html')


def firstview(request):
    return render(request, 'index_v2.html')