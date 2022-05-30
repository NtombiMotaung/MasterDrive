from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from gallery.models import ContactImages

# Create your views here.
def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  
        if form.is_valid():
            subject = "Website Inquiry"
            form.save() 

            try:
                send_mail(subject, "message", "admin@example.com", ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contacts:get-contacts-page")


    images = ContactImages.objects.last()

    form = ContactForm()

    context = {
        "form":form,
        "images": images,
    }
    return render(request, "public/contacts/contacts.html", context)