import imp
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def contacts(request):
    return  render(request, "public/contacts/contacts.html")

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'surname': form.cleaned_data['surname'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, "admin@example.com", ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contacts:contacts")

    form = ContactForm()
    return render(request, "contacts/contacts.html", {"form":form})