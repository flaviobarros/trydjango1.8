from django.shortcuts import render

# Create your views here.
def home(request):

    title = 'Meu titulo'
    context = {
            "template_title": title,
            
            }

    return render(request, "home.html", context)
