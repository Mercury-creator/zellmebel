from django.contrib import admin
from .models import Category, Furniture, AdditionalImages
# Register your models here.

admin.site.register(Category)
admin.site.register(Furniture)
admin.site.register(AdditionalImages)
