from django.shortcuts import render

# Create your views here.
def mainview(request):
    return render(request, 'login_v2.html')