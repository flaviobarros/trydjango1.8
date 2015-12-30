from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "full_name"]
    form = SignUpForm

    #class Meta(SignUp):
     #   model = SignUp
        
admin.site.register(SignUp, SignUpAdmin)
