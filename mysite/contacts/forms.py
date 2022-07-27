from django import forms
# from contacts.models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
            "class": "w-full bg-gray-300 text-red-500 font-black border-4 rounded border-black ",
            "placeholder": "Please enter your name"
        }
    ))

    surname = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
            "class": "w-full bg-gray-300 border-4 rounded border-black ",
            "placeholder": "Please enter your surname"
        }
    ))

    email = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
            "class": "w-full bg-gray-300 border-4 rounded border-black ",
            "placeholder": "Please enter your email"
        }
    ))

    message = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
            "class": "w-full h-20 bg-gray-300 border-4 rounded border-black ",
            "placeholder": "Please enter your message"
        }
    ))


    class Meta:
        # model = Contact
        fields = (
            "name",
            "surname",
            "email",
            "message",
        )
