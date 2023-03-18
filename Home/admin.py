from django.contrib import admin

# Register your models here.
from .models import Submissions
admin.site.register(Submissions)
from .models import Contact
admin.site.register(Contact)
