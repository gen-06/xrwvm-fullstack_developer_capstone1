from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]


# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)
