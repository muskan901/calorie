from django.contrib import admin
from myapp.models import Contact
from myapp.models import User

# Register your models here.
admin.site.register(Contact)

admin.site.register(User)