from django.shortcuts import render

# Create your views here.
from UserInformation.models import TbUser


def userview(request):
    users = TbUser.objects.all()
    return render(request, 'table_basic.html', locals())


