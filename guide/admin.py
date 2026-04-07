from django.contrib import admin
from .models import Booking
from .models import Contact
from .models import Brand

admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Brand)