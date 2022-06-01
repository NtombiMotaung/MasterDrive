from django.http import Http404
from django.shortcuts import render
from services.models import Service
from services.models import ContactImages, ServicesBackground


# Create your views here.
def get_services(request):
    image = ContactImages.objects.last()
    bg = ServicesBackground.objects.last()
    done = {
        "images": image,
        "bg" : bg,
    }
    return render(request, "public/services/services.html", done)


def get_service(request, id):
    try:
        services = Service.objects.get(id=id)

    except:
        raise Http404("Service not found")

    context = {"request": request, "services": services}

    return render(request, "public/services/get-services.html", context)
