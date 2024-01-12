from django.contrib import admin
from .models import Category, Drink, About, Contact

# Register your models here.


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'images')
    list_editable = ('price',)
    search_fields = ('name', )


admin.site.register(Category)
admin.site.register(About)
admin.site.register(Contact)
