from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home(request):

    title = 'Meu titulo'
    context = {
            "template_title": title,
            
            }

    return render(request, "home.html", context)

def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():

        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')

        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'flaviommbarros@gmail.com'] 
        contact_message = '''
        %s: %s via %s
        '''%(form_full_name, form_message, form_email)

        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)
    context = {
            
            "form": form,
            }

    return render(request, "forms.html", context)
