from django.shortcuts import render
from .models import Destinatins
from django.conf import settings
# Create your views here.

#u = settings.N_URL

def index(request):

    # dest1 = Destinatins()
    # dest1.img = 'destination_1.jpg'
    # dest1.name = 'Rajasthan'
    # dest1.desc = 'Kuch'
    # dest1.price = 1000
    # dest1.offer = True
    #
    # dest2 = Destinatins()
    # dest2.img = 'destination_2.jpg'
    # dest2.name = 'Bangalore'
    # dest2.desc = 'Kuch Bhi'
    # dest2.price = 2000
    # dest2.offer = False
    #
    # dest3 = Destinatins()
    # dest3.img = 'destination_3.jpg'
    # dest3.name = 'Mumbai'
    # dest3.desc = 'Kuch Kuch'
    # dest3.price = 3000
    # dest3.offer = False
    #
    # dest4 = Destinatins()
    # dest4.img = 'destination_4.jpg'
    # dest4.name = 'Delhi'
    # dest4.desc = 'Kuch Kuch Bhi'
    # dest4.price = 500
    # dest4.offer = True

    dests = Destinatins.objects.all()

    return render(request,'index.html',{'dests':dests})