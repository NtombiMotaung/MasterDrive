from django.http import Http404
from django.shortcuts import render
from services.models import Service

# Create your views here.
def get_services(request):
    return render(request, "public/services/services.html")

def get_service(request, id):
    
    try:
        services = Service.objects.get(id = id)

    except:
        raise Http404("Service not found")

    context = {"request" : request, "services" : services} 


    return render(request, "public/services/get-services.html", context)

