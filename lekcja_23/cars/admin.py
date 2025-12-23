from django.contrib import admin, messages
from .models import Car, Dealer

#zadanie1: admin.site.register(Car)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'is_available', 'full_name',)
    search_fields = ('brand', 'model',)
    list_filter = ('is_available', 'year',)
    ordering = ('-year',)
    readonly_fields = ('year',)
    actions = ["mark_as_unavailable",]

    def mark_as_unavailable(self, request, queryset):
        rows_updated = queryset.update(is_available = False)

        self.message_user(request, f'{rows_updated} linii zostało zaktualizowanych', messages.SUCCESS)

    mark_as_unavailable.short_description = 'Oznacz jako niedostępne'
    
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"
    full_name.short_description = 'Pełna nazwa'

class CarInLine(admin.TabularInline):
    model = Car 
    extra = 1

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [CarInLine]




