from django.contrib import admin

# Register your models here.
from .models import IshHolati, Stansiyalar, Yulak

admin.site.register(IshHolati)
admin.site.register(Stansiyalar)
admin.site.register(Yulak)