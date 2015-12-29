from django.contrib import admin

# Register your models here.
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "full_name"]
    class Meta(SignUp):
        model = SignUp
        
admin.site.register(SignUp, SignUpAdmin)
