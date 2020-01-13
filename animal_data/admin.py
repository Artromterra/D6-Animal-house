from django.contrib import admin
from animal_data.models import Pets, TypeOfAnimal

# admin.site.register(Pets)
# admin.site.register(TypeOfAnimal)

@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_animal')
    fields = ('name', 'breed', 'description', 'age', 'type_of_animal', 'image')

@admin.register(TypeOfAnimal)
class TypeOfAnimalAdmin(admin.ModelAdmin):
    pass

# Register your models here.
