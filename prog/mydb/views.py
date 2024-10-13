from django.shortcuts import render
from .models import Users
from django.http import HttpResponse

# Create your views here.
async def puk(request):
    pas = await Users.objects.aget(login = "iPhone")
    ctx = {"password" : pas.password, "login" : pas.login}
    return render(request, "puk.html", ctx)
    