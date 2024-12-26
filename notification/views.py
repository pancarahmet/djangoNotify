from django.shortcuts import render,redirect
from .bildirimgonder import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from .form import *

# Create your views here.

@receiver(post_save,sender=User)
def hosGeldinBildirimi(sender,instance,created,**kwargs):
    if created:
        bildirimGonder(instance,"Hoş geldiniz. Yeni Üyemiz")


def index(request):
    return render(request,"index.html")

def bildirimGor(request):
    bildirimler=Notification.objects.filter(user=request.user)
    print(bildirimler)
    context={
        "bildirimler":bildirimler
    }
    return render(request,"bildirimler.html",context)

def register(request):
    form=UserCreateForm()
    if request.method=="POST":
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bildirimler")

    context={
        "form":form
    }
    return render(request,"register.html",context)
