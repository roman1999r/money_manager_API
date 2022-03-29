from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib import admin

class TransactionAdmin(admin.ModelAdmin):
    fields = ('amount', 'user', 'category')

class CategoryAdmin(admin.ModelAdmin):
    fields = ('title',)


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)