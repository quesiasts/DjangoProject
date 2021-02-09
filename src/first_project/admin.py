import sys
sys.path.append('.')
from django.contrib import admin
from first_project.models import Team, Sport, Product, Customer

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'phone')


admin.site.register(Team)
admin.site.register(Sport)
admin.site.register(Product)
admin.site.register(Customer)