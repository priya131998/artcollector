from django.contrib import admin

# Register your models here.

from .models import Art, Exhibition, Buyer

# Register your models here
admin.site.register(Art)
admin.site.register(Exhibition)
admin.site.register(Buyer)